#!/usr/bin/env python3
"""公開収録MDファイルをNotionページに同期するスクリプト"""

import os
import re
import json
import urllib.request
import urllib.error
import urllib.parse

NOTION_API_KEY = os.environ.get("NOTION_API_KEY", "")
PARENT_PAGE_ID = "30979bfe-0a45-805e-9a20-e7f11dfbb3b0"
GITHUB_RAW_BASE = "https://raw.githubusercontent.com/sasuumaker/koukai-shuuroku/main"
NOTION_API = "https://api.notion.com/v1"
HEADERS = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}

MD_DIR = os.path.dirname(os.path.abspath(__file__))


def api_request(method: str, endpoint: str, data: dict | None = None) -> dict:
    url = f"{NOTION_API}{endpoint}"
    body = json.dumps(data).encode() if data else None
    req = urllib.request.Request(url, data=body, headers=HEADERS, method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        err_body = e.read().decode()
        print(f"  API Error {e.code}: {err_body}")
        raise


def get_existing_children(page_id: str) -> list[dict]:
    """親ページ直下の子ページ一覧を取得"""
    results = []
    start_cursor = None
    while True:
        endpoint = f"/blocks/{page_id}/children?page_size=100"
        if start_cursor:
            endpoint += f"&start_cursor={start_cursor}"
        resp = api_request("GET", endpoint)
        results.extend(resp.get("results", []))
        if not resp.get("has_more"):
            break
        start_cursor = resp.get("next_cursor")
    return results


def find_existing_pages(page_id: str) -> dict[str, str]:
    """既存の子ページをタイトルで検索し {title: block_id} を返す"""
    children = get_existing_children(page_id)
    pages = {}
    for block in children:
        if block.get("type") == "child_page":
            title = block.get("child_page", {}).get("title", "")
            pages[title] = block["id"]
    return pages


def md_to_notion_blocks(md_content: str) -> list[dict]:
    """MarkdownをNotionブロックに変換"""
    blocks = []
    lines = md_content.split("\n")
    i = 0
    in_code_block = False
    code_lines = []
    code_lang = ""
    in_table = False
    table_rows = []

    while i < len(lines):
        line = lines[i]

        # コードブロック
        if line.startswith("```"):
            if not in_code_block:
                in_code_block = True
                code_lang = line[3:].strip() or "plain text"
                code_lines = []
            else:
                in_code_block = False
                blocks.append({
                    "object": "block",
                    "type": "code",
                    "code": {
                        "rich_text": [{"type": "text", "text": {"content": "\n".join(code_lines)}}],
                        "language": code_lang,
                    },
                })
            i += 1
            continue

        if in_code_block:
            code_lines.append(line)
            i += 1
            continue

        # テーブル
        if "|" in line and not in_table:
            # テーブル開始チェック
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) >= 2:
                in_table = True
                table_rows = [cells]
                i += 1
                continue

        if in_table:
            if "|" in line:
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                # セパレーター行をスキップ
                if all(re.match(r"^[-:]+$", c) for c in cells):
                    i += 1
                    continue
                table_rows.append(cells)
                i += 1
                continue
            else:
                # テーブル終了
                if table_rows:
                    width = max(len(r) for r in table_rows)
                    notion_rows = []
                    for row in table_rows:
                        # 列数を揃える
                        padded = row + [""] * (width - len(row))
                        notion_rows.append({
                            "object": "block",
                            "type": "table_row",
                            "table_row": {
                                "cells": [
                                    [{"type": "text", "text": {"content": cell}}]
                                    for cell in padded
                                ]
                            },
                        })
                    blocks.append({
                        "object": "block",
                        "type": "table",
                        "table": {
                            "table_width": width,
                            "has_column_header": True,
                            "has_row_header": False,
                            "children": notion_rows,
                        },
                    })
                in_table = False
                table_rows = []
                # この行は次の処理へ（fallthrough）

        # 空行
        if line.strip() == "":
            i += 1
            continue

        # 水平線
        if line.strip() == "---":
            blocks.append({"object": "block", "type": "divider", "divider": {}})
            i += 1
            continue

        # 画像 ![alt](path)
        img_match = re.match(r"^!\[([^\]]*)\]\(([^)]+)\)$", line.strip())
        if img_match:
            alt = img_match.group(1)
            path = img_match.group(2)
            # ローカルパスをGitHub raw URLに変換
            img_url = f"{GITHUB_RAW_BASE}/{urllib.parse.quote(path)}"
            blocks.append({
                "object": "block",
                "type": "image",
                "image": {
                    "type": "external",
                    "external": {"url": img_url},
                    "caption": [{"type": "text", "text": {"content": alt}}] if alt else [],
                },
            })
            i += 1
            continue

        # 見出し（h1はページタイトルなのでスキップ）
        h_match = re.match(r"^(#{1,3})\s+(.+)$", line)
        if h_match:
            level = len(h_match.group(1))
            text = h_match.group(2)
            if level == 1:
                # h1はページタイトルとして使うのでスキップ
                i += 1
                continue
            h_type = f"heading_{level}"
            blocks.append({
                "object": "block",
                "type": h_type,
                h_type: {
                    "rich_text": parse_inline(text),
                },
            })
            i += 1
            continue

        # 引用（blockquote）
        if line.startswith("> "):
            text = line[2:]
            blocks.append({
                "object": "block",
                "type": "quote",
                "quote": {
                    "rich_text": parse_inline(text),
                },
            })
            i += 1
            continue

        # リスト
        li_match = re.match(r"^(\s*)[-*]\s+(.+)$", line)
        if li_match:
            text = li_match.group(2)
            blocks.append({
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {
                    "rich_text": parse_inline(text),
                },
            })
            i += 1
            continue

        # 番号付きリスト
        ol_match = re.match(r"^(\s*)\d+\.\s+(.+)$", line)
        if ol_match:
            text = ol_match.group(2)
            blocks.append({
                "object": "block",
                "type": "numbered_list_item",
                "numbered_list_item": {
                    "rich_text": parse_inline(text),
                },
            })
            i += 1
            continue

        # 通常の段落
        blocks.append({
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": parse_inline(line),
            },
        })
        i += 1

    # テーブルが末尾で終わった場合
    if in_table and table_rows:
        width = max(len(r) for r in table_rows)
        notion_rows = []
        for row in table_rows:
            padded = row + [""] * (width - len(row))
            notion_rows.append({
                "object": "block",
                "type": "table_row",
                "table_row": {
                    "cells": [
                        [{"type": "text", "text": {"content": cell}}]
                        for cell in padded
                    ]
                },
            })
        blocks.append({
            "object": "block",
            "type": "table",
            "table": {
                "table_width": width,
                "has_column_header": True,
                "has_row_header": False,
                "children": notion_rows,
            },
        })

    return blocks


def parse_inline(text: str) -> list[dict]:
    """インラインMarkdown（太字、コード、リンク）をNotion rich_textに変換"""
    result = []
    pattern = re.compile(
        r"(\*\*(.+?)\*\*)"       # 太字
        r"|(`([^`]+?)`)"          # インラインコード
        r"|(\[([^\]]+)\]\(([^)]+)\))"  # リンク
    )
    pos = 0
    for m in pattern.finditer(text):
        # マッチ前のプレーンテキスト
        if m.start() > pos:
            result.append({"type": "text", "text": {"content": text[pos:m.start()]}})

        if m.group(2):  # 太字
            result.append({
                "type": "text",
                "text": {"content": m.group(2)},
                "annotations": {"bold": True},
            })
        elif m.group(4):  # インラインコード
            result.append({
                "type": "text",
                "text": {"content": m.group(4)},
                "annotations": {"code": True},
            })
        elif m.group(6):  # リンク
            result.append({
                "type": "text",
                "text": {"content": m.group(6), "link": {"url": m.group(7)}},
            })
        pos = m.end()

    # 残りのテキスト
    if pos < len(text):
        result.append({"type": "text", "text": {"content": text[pos:]}})

    if not result:
        result.append({"type": "text", "text": {"content": text}})

    return result


def extract_title(md_content: str) -> str:
    """MDの最初のh1からタイトルを取得"""
    for line in md_content.split("\n"):
        m = re.match(r"^#\s+(.+)$", line)
        if m:
            return m.group(1)
    return "Untitled"


def delete_block(block_id: str):
    api_request("DELETE", f"/blocks/{block_id}")


def create_page(parent_id: str, title: str, blocks: list[dict]) -> str:
    """子ページを作成（100ブロックずつ分割）"""
    # 最初の100ブロックでページ作成
    first_batch = blocks[:100]
    data = {
        "parent": {"type": "page_id", "page_id": parent_id},
        "properties": {
            "title": [{"type": "text", "text": {"content": title}}]
        },
        "children": first_batch,
    }
    resp = api_request("POST", "/pages", data)
    page_id = resp["id"]

    # 残りのブロックを追加
    remaining = blocks[100:]
    while remaining:
        batch = remaining[:100]
        remaining = remaining[100:]
        api_request("PATCH", f"/blocks/{page_id}/children", {"children": batch})

    return page_id


def sync_file(filepath: str, existing_pages: dict[str, str]):
    """1つのMDファイルを同期"""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    title = extract_title(content)
    blocks = md_to_notion_blocks(content)

    print(f"  {os.path.basename(filepath)} → {title}")
    print(f"    ブロック数: {len(blocks)}")

    # 既存ページがあれば削除して再作成
    if title in existing_pages:
        print(f"    既存ページを削除中...")
        delete_block(existing_pages[title])

    page_id = create_page(PARENT_PAGE_ID, title, blocks)
    print(f"    作成完了: {page_id}")


def get_md_files() -> list[str]:
    """第X回_*.md ファイルを番号順で取得"""
    files = []
    for f in os.listdir(MD_DIR):
        if re.match(r"^第\d+回_.*\.md$", f):
            files.append(os.path.join(MD_DIR, f))

    def sort_key(path):
        m = re.search(r"第(\d+)回", os.path.basename(path))
        return int(m.group(1)) if m else 999

    return sorted(files, key=sort_key)


def main():
    if not NOTION_API_KEY:
        print("エラー: NOTION_API_KEY 環境変数を設定してください")
        print("  export NOTION_API_KEY='ntn_xxxxx'")
        return

    print("=== 公開収録 → Notion 同期 ===\n")

    md_files = get_md_files()
    print(f"対象ファイル: {len(md_files)}件\n")

    print("既存ページを確認中...")
    existing = find_existing_pages(PARENT_PAGE_ID)
    print(f"  既存ページ: {len(existing)}件\n")

    print("同期開始...\n")
    for filepath in md_files:
        try:
            sync_file(filepath, existing)
        except Exception as e:
            print(f"  エラー: {e}")
        print()

    print("=== 同期完了 ===")


if __name__ == "__main__":
    main()
