# 第9回 画像生成プロンプト一覧

## 共通実行コマンド

```bash
source /Users/sasou/root/scripts/.venv/bin/activate
python /Users/sasou/root/scripts/generate_image.py \
  --type diagram \
  --no-character \
  --prompt "（各プロンプト）" \
  --output "/Users/sasou/root/公開収録/images/第9回/XX-name.png" \
  --timeout 120
```

---

## 01-goal.png — このレッスンのゴール

### YAML

```yaml
image_id: "ep09_01_goal"
concept_title: "文章の修正 — トーン変更・校正・書き換え"
narrative:
  type: "journey"
  story: "1つのビジネスメールから、トーン変更・校正・翻訳と様々な変身ができるゴールへの道のり"
visual_elements:
  element_1:
    object: "ビジネスメール文書"
    detail: "白い便箋に堅い文章が3行書かれた手紙アイコン、封筒から半分出ている状態、黒い縦書き文字の線"
    position: "左下"
  element_2:
    object: "棒人間（笑顔）"
    detail: "Stick figure with confident smile, one hand pointing right toward the goal, standing next to the letter"
    position: "左下、メールの横"
  element_3:
    object: "上向きの階段"
    detail: "3段の階段、各段に青/緑の水彩グラデーション、ラフな手描き線"
    position: "中央を斜めに横断"
  element_4:
    object: "変身した文書3種"
    detail: "階段の各段にアイコン：(1)ハートマーク付きカジュアル文書 (2)赤ペンチェック付き校正文書 (3)地球儀マーク付き英語文書"
    position: "階段の各段"
  element_5:
    object: "ゴールの旗"
    detail: "Orange flag with sparkle marks, waving at the top of the stairs"
    position: "右上"
  element_6:
    object: "ターミナル画面（小）"
    detail: "Small black terminal window with '@ メール.txt' in green text"
    position: "左端、棒人間の後ろ"
  element_7:
    object: "キラキラ装飾"
    detail: "Sparkle stars scattered around the goal flag, yellow/orange crayon texture"
    position: "右上周辺"
text_elements:
  labels:
    - text: "トーン変更"
      attached_to: "element_4の1段目"
    - text: "校正"
      attached_to: "element_4の2段目"
    - text: "翻訳"
      attached_to: "element_4の3段目"
    - text: "自由自在！"
      attached_to: "element_5"
composition_and_emphasis:
  layout_structure: "Diagonal staircase from bottom-left to top-right"
  focal_point: "ゴールの旗"
  emphasis_technique: "Orange flag, sparkle marks, watercolor stairs"
  color_accents: "Blue/green watercolor gradient on staircase steps"
  frame_rule: "全ての要素をフレーム内に余裕をもって収めること"
style_application_notes:
  texture_focus: "Watercolor wash on stairs, marker outlines, crayon sparkles"
  mood_direction: "Accomplished / Excited"
```

### 変換プロンプト

```
左下から右上への階段構図の手書きスケッチ。
左下に封筒から半分出たビジネスメールの便箋があり、堅い文章が3行書かれている。その横に笑顔の棒人間が右を指さしている。棒人間の後ろに小さな黒いターミナル画面があり、緑色の文字で「@メール.txt」と表示されている。
中央を斜めに横切る3段の階段があり、青/緑の水彩グラデーションで塗られている。
階段の1段目にハートマーク付きの文書アイコンがあり「トーン変更」のラベル。2段目に赤ペンチェック付きの文書アイコンがあり「校正」のラベル。3段目に地球儀マーク付きの文書アイコンがあり「翻訳」のラベル。
右上に大きなオレンジの旗がはためいており、周りにキラキラマークが3つ。旗の横に「自由自在！」のラベル。
紙テクスチャの背景。マーカーペンで描いたようなラフな線。青/緑の水彩風アクセント。全ての要素をフレーム内に余裕をもって収めること。
```

---

## 02-recap.png — 第2回の具体例をやってみよう

### YAML

```yaml
image_id: "ep09_02_recap"
concept_title: "前回の復習 — @ファイル名で修正指示"
narrative:
  type: "before-after"
  story: "堅いメールが@指示で一瞬でカジュアルに生まれ変わる"
visual_elements:
  element_1:
    object: "堅いビジネスメール"
    detail: "White document with formal text lines, stiff border, gray/dark tone, '拝啓' visible at top"
    position: "左側"
  element_2:
    object: "太い矢印"
    detail: "Large bold hand-drawn arrow pointing right, orange crayon texture, with sparkle effect"
    position: "中央"
  element_3:
    object: "カジュアルなメール"
    detail: "White document with relaxed text lines, rounded edges, cheerful tone, small heart marks"
    position: "右側"
  element_4:
    object: "ターミナル画面"
    detail: "Black terminal screen below the arrow with green text showing '@ メール.txt をカジュアルに'"
    position: "中央下"
  element_5:
    object: "棒人間（指さし）"
    detail: "Stick figure pointing at the terminal with a smile, speech bubble with '!'mark"
    position: "中央下の右"
  element_6:
    object: "要約と修正の対比ラベル"
    detail: "Small note showing '前回: 短くする → 今回: 質を変える' with blue underline"
    position: "下端"
text_elements:
  labels:
    - text: "堅いメール"
      attached_to: "element_1"
    - text: "カジュアルに！"
      attached_to: "element_3"
    - text: "質を変える"
      attached_to: "element_6"
    - text: "@ファイル名"
      attached_to: "element_4"
composition_and_emphasis:
  layout_structure: "Left-to-Right before-after with terminal below"
  focal_point: "カジュアルなメール（右側）"
  emphasis_technique: "Orange arrow, heart marks on casual mail, sparkle effect"
  color_accents: "Blue underline on comparison note, green watercolor splash behind casual mail"
  frame_rule: "全ての要素をフレーム内に余裕をもって収めること"
style_application_notes:
  texture_focus: "Marker outlines, crayon arrow, watercolor splash"
  mood_direction: "Curious / Excited"
```

### 変換プロンプト

```
左から右へのビフォーアフター構図の手書きスケッチ。
左側に堅いビジネスメールの文書があり、堅い罫線の枠で囲まれ、上部に「拝啓」の文字、灰色がかった堅い雰囲気。文書の下に「堅いメール」のラベル。
中央に太いオレンジのクレヨン矢印が右を指しており、キラキラ効果が付いている。
矢印の下に黒いターミナル画面があり、緑の文字で「@メール.txt をカジュアルに」と表示。ターミナルの左に「@ファイル名」のラベル。
右側に角丸の柔らかい文書があり、小さなハートマークが2つ付いている。背景に緑の水彩スプラッシュ。文書の下に「カジュアルに！」のラベル。
ターミナルの右横に笑顔の棒人間が指をさしている。
下端に小さな注釈で「質を変える」のラベルに青いアンダーライン。
紙テクスチャの背景。マーカーペンで描いたようなラフな線。青/緑の水彩風アクセント。全ての要素をフレーム内に余裕をもって収めること。
```

---

## 03-create-sample.png — 練習用ファイルを用意する

### YAML

```yaml
image_id: "ep09_03_create_sample"
concept_title: "ファイルを作成する手順"
narrative:
  type: "multi-step-process"
  story: "ターミナルを開く→claudeを起動→指示を出す→ファイルができる"
visual_elements:
  element_1:
    object: "ターミナルアイコン"
    detail: "Black terminal icon with '>' prompt symbol, rounded rectangle"
    position: "左端"
  element_2:
    object: "手描き矢印①"
    detail: "Hand-drawn arrow pointing right, thin marker style"
    position: "element_1とelement_3の間"
  element_3:
    object: "claude起動画面"
    detail: "Black terminal screen with '$ claude' typed in green, cursor blinking, small Claude logo mark"
    position: "中央左"
  element_4:
    object: "手描き矢印②"
    detail: "Hand-drawn arrow pointing right, thin marker style"
    position: "element_3とelement_5の間"
  element_5:
    object: "吹き出し（指示文）"
    detail: "Speech bubble with handwritten text showing the instruction, blue accent border"
    position: "中央右"
  element_6:
    object: "手描き矢印③"
    detail: "Hand-drawn arrow pointing right, orange with sparkle"
    position: "element_5とelement_7の間"
  element_7:
    object: "テキストファイルアイコン"
    detail: "White document icon labeled 'メール下書き.txt' with lines of text visible, sparkle marks, yellow folder on desktop"
    position: "右端"
  element_8:
    object: "棒人間（ガッツポーズ）"
    detail: "Stick figure with arms raised in celebration, small '!' above head"
    position: "右端下"
text_elements:
  labels:
    - text: "起動"
      attached_to: "element_3"
    - text: "指示を出す"
      attached_to: "element_5"
    - text: "ファイル完成！"
      attached_to: "element_7"
    - text: "Allow"
      attached_to: "element_6の上（小さな緑のバッジ）"
composition_and_emphasis:
  layout_structure: "Left-to-Right 4-step flow"
  focal_point: "完成したファイルアイコン with sparkles"
  emphasis_technique: "Orange final arrow, sparkle marks on file, green Allow badge"
  color_accents: "Blue accent on speech bubble border, green watercolor behind completed file"
  frame_rule: "全ての要素をフレーム内に余裕をもって収めること"
style_application_notes:
  texture_focus: "Marker arrows, crayon sparkles, watercolor background splash"
  mood_direction: "Accomplished"
```

### 変換プロンプト

```
左から右への4段階フロー手順図の手書きスケッチ。
左端に黒いターミナルアイコンがあり「>」のプロンプト記号が表示されている。
右への手描き矢印の先に、黒いターミナル画面があり緑の文字で「$ claude」と表示されカーソルが点滅。「起動」のラベル。
さらに右への矢印の先に、青い枠線の吹き出しがあり手書き文字で指示内容が書かれている。「指示を出す」のラベル。
さらに右へのオレンジの矢印にキラキラ効果。矢印の上に小さな緑のバッジで「Allow」の文字。
右端に白い文書アイコンがあり「メール下書き.txt」と書かれ、テキスト行が見え、キラキラマークが3つ。背景に緑の水彩スプラッシュ。「ファイル完成！」のラベル。
ファイルの下に万歳する棒人間、頭の上に「！」マーク。
紙テクスチャの背景。マーカーペンで描いたようなラフな線。青/緑の水彩風アクセント。全ての要素をフレーム内に余裕をもって収めること。
```

---

## 04-save-original.png — 元ファイルを守る方法

### YAML

```yaml
image_id: "ep09_04_save_original"
concept_title: "別名保存で元ファイルを守る"
narrative:
  type: "comparison"
  story: "左: 上書き=元が消える(NG) vs 右: 別名保存=両方残る(OK)"
visual_elements:
  element_1:
    object: "元のファイル（左上）"
    detail: "White document icon with text lines, labeled 'メール下書き.txt'"
    position: "左上"
  element_2:
    object: "上書き結果（NG）"
    detail: "Same document but with red X mark overlay, original text crossed out, sad face, red warning color"
    position: "左下"
  element_3:
    object: "中央の仕切り線"
    detail: "Vertical dashed line with 'VS' in orange circle"
    position: "中央"
  element_4:
    object: "元のファイル（右上、保持）"
    detail: "White document icon intact, small green checkmark, labeled 'メール下書き.txt'"
    position: "右上"
  element_5:
    object: "修正版ファイル（右下、新規）"
    detail: "White document icon with blue sparkle marks, labeled 'メール_修正版.txt', small star"
    position: "右下"
  element_6:
    object: "棒人間（右側、笑顔）"
    detail: "Stick figure with thumbs up and smile, blue/green watercolor splash behind"
    position: "右端"
  element_7:
    object: "棒人間（左側、困り顔）"
    detail: "Stick figure with worried face, sweat drop"
    position: "左端"
text_elements:
  labels:
    - text: "上書き NG"
      attached_to: "element_2"
    - text: "別名保存 OK"
      attached_to: "element_5"
    - text: "元も残る！"
      attached_to: "element_4"
    - text: "比べられる"
      attached_to: "element_6"
composition_and_emphasis:
  layout_structure: "Comparison split (left NG vs right OK)"
  focal_point: "右側の2ファイル並列"
  emphasis_technique: "Red X on left, green check + blue sparkle on right, VS circle"
  color_accents: "Blue/green watercolor splash behind happy stick figure, green checkmark"
  frame_rule: "全ての要素をフレーム内に余裕をもって収めること"
style_application_notes:
  texture_focus: "Marker outlines, red crayon X, blue watercolor splash"
  mood_direction: "Left: Worried → Right: Relieved"
```

### 変換プロンプト

```
左右対比構図の手書きスケッチ。中央に縦の点線があり、オレンジの丸に「VS」の文字。
左側：上に白い文書アイコン「メール下書き.txt」がある。下向き矢印の先に同じ文書だが赤い大きな×印が重なり、元の文字が取り消し線で消されている。困り顔の棒人間が汗マーク付きで立っている。「上書き NG」の赤いラベル。
右側：上に白い文書アイコン「メール下書き.txt」が緑のチェックマーク付きで残っている。「元も残る！」のラベル。その下にもう1つの文書アイコン「メール_修正版.txt」が青いキラキラマーク付きで並んでいる。「別名保存 OK」のラベル。右端にサムズアップする笑顔の棒人間がおり、背景に青/緑の水彩スプラッシュ。「比べられる」のラベル。
紙テクスチャの背景。マーカーペンで描いたようなラフな線。青/緑の水彩風アクセント。全ての要素をフレーム内に余裕をもって収めること。
```

---

## 05-lets-try.png — やってみよう（トーンを変える）

### YAML

```yaml
image_id: "ep09_05_lets_try"
concept_title: "トーンを変える実践"
narrative:
  type: "before-after"
  story: "堅いビジネスメールが「丁寧」にも「カジュアル」にも自在に変身する"
visual_elements:
  element_1:
    object: "堅いメール（中央上）"
    detail: "Formal document with rigid border, '拝啓' at top, dark gray tone, serious face stamp"
    position: "中央上"
  element_2:
    object: "下向き分岐矢印2本"
    detail: "Two hand-drawn arrows branching down-left and down-right from the formal mail, orange crayon"
    position: "中央"
  element_3:
    object: "丁寧版メール"
    detail: "Document with soft rounded border, pastel blue accent, gentle smile face stamp, warm tone"
    position: "左下"
  element_4:
    object: "カジュアル版メール"
    detail: "Document with wavy casual border, heart marks, big smile face stamp, 'お疲れさま！' text peek"
    position: "右下"
  element_5:
    object: "ターミナル吹き出し（左）"
    detail: "Small terminal-style bubble showing '丁寧なトーンに' in green text"
    position: "左の矢印上"
  element_6:
    object: "ターミナル吹き出し（右）"
    detail: "Small terminal-style bubble showing 'カジュアルに' in green text"
    position: "右の矢印上"
  element_7:
    object: "棒人間（驚き顔）"
    detail: "Stick figure with amazed expression, both hands on cheeks, small sparkles around"
    position: "右端"
text_elements:
  labels:
    - text: "堅いメール"
      attached_to: "element_1"
    - text: "丁寧に"
      attached_to: "element_3"
    - text: "カジュアルに"
      attached_to: "element_4"
    - text: "同じ内容！"
      attached_to: "element_7"
composition_and_emphasis:
  layout_structure: "Top-center branching down to left and right"
  focal_point: "2つの変身結果"
  emphasis_technique: "Orange branching arrows, contrasting document styles, sparkle on stick figure"
  color_accents: "Blue watercolor accent on polite version, green watercolor accent on casual version"
  frame_rule: "全ての要素をフレーム内に余裕をもって収めること"
style_application_notes:
  texture_focus: "Marker borders, crayon arrows, watercolor document backgrounds"
  mood_direction: "Amazed / Curious"
```

### 変換プロンプト

```
上から下への分岐構図の手書きスケッチ。
中央上に堅いビジネスメール文書があり、堅い枠線、上部に「拝啓」の文字、真面目な顔スタンプ。「堅いメール」のラベル。
そこから2本のオレンジのクレヨン矢印が左下と右下に分岐している。
左の矢印の上に小さなターミナル風の吹き出しで緑文字の「丁寧なトーンに」。左下に丁寧版メール文書があり、柔らかい丸い枠線、パステルブルーのアクセント、穏やかな笑顔スタンプ。「丁寧に」のラベル。青い水彩アクセントが背景に。
右の矢印の上に小さなターミナル風の吹き出しで緑文字の「カジュアルに」。右下にカジュアル版メール文書があり、波線の枠、ハートマーク2つ、大きな笑顔スタンプ、「お疲れさま！」の文字がちらり。「カジュアルに」のラベル。緑の水彩アクセントが背景に。
右端に驚き顔の棒人間が両手を頬に当てており、キラキラマーク。「同じ内容！」のラベル。
紙テクスチャの背景。マーカーペンで描いたようなラフな線。青/緑の水彩風アクセント。全ての要素をフレーム内に余裕をもって収めること。
```

---

## 06-proofread.png — 校正する

### YAML

```yaml
image_id: "ep09_06_proofread"
concept_title: "誤字脱字チェック — 校正"
narrative:
  type: "multi-step-process"
  story: "文章を渡す→AIが間違いを発見→赤ペンで修正→きれいな文章に"
visual_elements:
  element_1:
    object: "間違いのある文書"
    detail: "White document with text lines, some characters circled in red showing errors, wavy red underlines"
    position: "左側"
  element_2:
    object: "虫眼鏡"
    detail: "Large magnifying glass hovering over the document, lens showing enlarged text with error highlighted"
    position: "左中央"
  element_3:
    object: "太い矢印"
    detail: "Bold hand-drawn arrow pointing right, orange marker texture"
    position: "中央"
  element_4:
    object: "修正済み文書"
    detail: "Clean white document with neat text lines, green checkmarks next to corrected lines, sparkle marks"
    position: "右側"
  element_5:
    object: "赤ペン"
    detail: "Red pen with ink mark trail, angled as if just finished marking"
    position: "左下"
  element_6:
    object: "棒人間（安心顔）"
    detail: "Stick figure with relieved smile, both hands together, small blue/green watercolor cloud behind"
    position: "右下"
text_elements:
  labels:
    - text: "間違い発見"
      attached_to: "element_2"
    - text: "赤ペンで修正"
      attached_to: "element_5"
    - text: "きれいな文章"
      attached_to: "element_4"
    - text: "送信前に！"
      attached_to: "element_6"
composition_and_emphasis:
  layout_structure: "Left-to-Right 3-panel flow"
  focal_point: "修正済み文書 with checkmarks"
  emphasis_technique: "Red circles/underlines on left, green checks on right, orange arrow"
  color_accents: "Blue/green watercolor cloud behind happy stick figure"
  frame_rule: "全ての要素をフレーム内に余裕をもって収めること"
style_application_notes:
  texture_focus: "Red marker circles, green crayon checks, watercolor cloud"
  mood_direction: "Relieved / Accomplished"
```

### 変換プロンプト

```
左から右への3段階フロー手順図の手書きスケッチ。
左側に白い文書があり、テキスト行のいくつかに赤い丸印と赤い波線のアンダーラインが付いて間違い箇所を示している。その上に大きな虫眼鏡がかぶさり、レンズの中にエラー箇所が拡大表示されている。「間違い発見」のラベル。左下に赤ペンがインクの跡を残して斜めに置かれている。「赤ペンで修正」のラベル。
中央にオレンジのマーカーで描かれた太い矢印が右を指している。
右側にきれいな白い文書があり、修正された行の横に緑のチェックマークが3つ並び、キラキラマークが付いている。「きれいな文章」のラベル。
右下に安心した笑顔の棒人間が手を合わせており、背景に青/緑の水彩の雲。「送信前に！」のラベル。
紙テクスチャの背景。マーカーペンで描いたようなラフな線。青/緑の水彩風アクセント。全ての要素をフレーム内に余裕をもって収めること。
```

---

## 07-rewrite-for-audience.png — 読者に合わせて書き換える

### YAML

```yaml
image_id: "ep09_07_rewrite_audience"
concept_title: "読者に合わせた書き換え"
narrative:
  type: "comparison"
  story: "左の難しい文章が、右では小学生にも分かるやさしい言葉に変わる"
visual_elements:
  element_1:
    object: "難しい文書"
    detail: "Document with dense small text, kanji-heavy, formal stamp, gray/dark border, intimidating look"
    position: "左側"
  element_2:
    object: "大人の棒人間（困惑）"
    detail: "Stick figure with confused face, question marks above head, reading the difficult document"
    position: "左側下"
  element_3:
    object: "太い矢印"
    detail: "Large bold orange arrow with small terminal icon above showing '@ファイル やさしく'"
    position: "中央"
  element_4:
    object: "やさしい文書"
    detail: "Document with large friendly text, rounded shapes, colorful highlights, flower/star doodles in margins"
    position: "右側"
  element_5:
    object: "子どもの棒人間（笑顔）"
    detail: "Smaller stick figure with big smile and light bulb above head, reading happily"
    position: "右側下"
  element_6:
    object: "変換の吹き出し"
    detail: "Small callout showing 'ご検討のほど → 考えてみてね' with blue highlight"
    position: "中央上"
text_elements:
  labels:
    - text: "むずかしい"
      attached_to: "element_1"
    - text: "やさしい！"
      attached_to: "element_4"
    - text: "わかった！"
      attached_to: "element_5"
    - text: "考えてみてね"
      attached_to: "element_6"
composition_and_emphasis:
  layout_structure: "Left-to-Right comparison split"
  focal_point: "やさしい文書 + 笑顔の子ども棒人間"
  emphasis_technique: "Orange arrow, light bulb icon, colorful highlights on easy version"
  color_accents: "Blue highlight in conversion callout, green watercolor splash behind happy child"
  frame_rule: "全ての要素をフレーム内に余裕をもって収めること"
style_application_notes:
  texture_focus: "Marker outlines, crayon doodles, watercolor splash"
  mood_direction: "Left: Overwhelmed → Right: Relieved"
```

### 変換プロンプト

```
左右対比構図の手書きスケッチ。
左側に漢字だらけの堅い文書があり、小さく密な文字、堅い枠線、暗い灰色のトーン。「むずかしい」のラベル。その下に困惑顔の棒人間がおり、頭上に「？」マークが2つ浮かんでいる。
中央に太いオレンジの矢印があり、矢印の上に小さなターミナルアイコンで「@ファイル やさしく」と表示。中央上に小さな吹き出しで「ご検討のほど → 考えてみてね」と書かれ青いハイライト。「考えてみてね」のラベル。
右側にやさしい文書があり、大きめの文字、丸い枠線、余白に花や星の落書き、カラフルなハイライト。「やさしい！」のラベル。背景に緑の水彩スプラッシュ。その下に小さめの棒人間（子ども）が笑顔で、頭上に電球マーク。「わかった！」のラベル。
紙テクスチャの背景。マーカーペンで描いたようなラフな線。青/緑の水彩風アクセント。全ての要素をフレーム内に余裕をもって収めること。
```

---

## 08-translate.png — 英語に翻訳する

### YAML

```yaml
image_id: "ep09_08_translate"
concept_title: "英語に翻訳"
narrative:
  type: "before-after"
  story: "日本語メールが地球を越えて英語メールに変換される"
visual_elements:
  element_1:
    object: "日本語メール"
    detail: "White document with Japanese text lines visible ('日本語' written), Japan flag small icon"
    position: "左側"
  element_2:
    object: "地球儀"
    detail: "Hand-drawn globe with continents sketched, rotation arrow around it, blue/green watercolor"
    position: "中央"
  element_3:
    object: "英語メール"
    detail: "White document with English text lines ('Dear...' visible), small US/UK flag icon, sparkle marks"
    position: "右側"
  element_4:
    object: "手描き矢印（左→中央）"
    detail: "Orange arrow from Japanese doc to globe"
    position: "左中央"
  element_5:
    object: "手描き矢印（中央→右）"
    detail: "Orange arrow from globe to English doc"
    position: "中央右"
  element_6:
    object: "棒人間（ガッツポーズ）"
    detail: "Stick figure with confident pose, fist pump, no separate translation software needed"
    position: "右下"
  element_7:
    object: "×印の翻訳ソフトアイコン"
    detail: "Small crossed-out translation app icon (showing it's unnecessary)"
    position: "左下"
text_elements:
  labels:
    - text: "日本語"
      attached_to: "element_1"
    - text: "English"
      attached_to: "element_3"
    - text: "これだけ！"
      attached_to: "element_6"
    - text: "翻訳ソフト不要"
      attached_to: "element_7"
composition_and_emphasis:
  layout_structure: "Left-to-Right flow through central globe"
  focal_point: "地球儀 with watercolor"
  emphasis_technique: "Orange arrows, sparkle on English doc, crossed-out translation app"
  color_accents: "Blue/green watercolor on globe, green splash behind English document"
  frame_rule: "全ての要素をフレーム内に余裕をもって収めること"
style_application_notes:
  texture_focus: "Watercolor globe, marker arrows, crayon sparkles"
  mood_direction: "Accomplished / Confident"
```

### 変換プロンプト

```
左から右へ地球儀を経由するフロー構図の手書きスケッチ。
左側に日本語のメール文書があり、日本語のテキスト行が見え、小さな日本国旗アイコン。「日本語」のラベル。左下に翻訳ソフトのアイコンに赤い×印が重なっている。「翻訳ソフト不要」のラベル。
左からオレンジの手描き矢印が中央の地球儀へ向かう。中央に手描きの地球儀があり、大陸が簡略に描かれ、回転矢印が付いている。地球儀は青/緑の水彩で彩色されている。
地球儀から右へオレンジの矢印が伸び、右側に英語のメール文書があり「Dear...」の文字が見え、小さな英国旗アイコン、キラキラマーク3つ。背景に緑の水彩スプラッシュ。「English」のラベル。
右下にガッツポーズの棒人間が自信ありげに立っている。「これだけ！」のラベル。
紙テクスチャの背景。マーカーペンで描いたようなラフな線。青/緑の水彩風アクセント。全ての要素をフレーム内に余裕をもって収めること。
```

---

## 09-comparison.png — 要約との違い

### YAML

```yaml
image_id: "ep09_09_comparison"
concept_title: "要約 vs 修正の違い"
narrative:
  type: "comparison"
  story: "左: 要約は長い文を短くする。右: 修正は同じ長さで質を変える。目的が違う"
visual_elements:
  element_1:
    object: "元の長い文書"
    detail: "Tall document with many text lines, placed at top center, arrows branching left and right"
    position: "上部中央"
  element_2:
    object: "要約の結果（左）"
    detail: "Short small document (1/3 size of original), compact text, blue accent border"
    position: "左下"
  element_3:
    object: "修正の結果（右）"
    detail: "Same-height document as original but with different colored text/tone, orange accent border, heart mark"
    position: "右下"
  element_4:
    object: "分岐矢印"
    detail: "Two arrows branching from original: left arrow labeled '短くする', right arrow labeled '質を変える'"
    position: "中央"
  element_5:
    object: "ものさし（左）"
    detail: "Small ruler icon showing size reduction, measuring shorter document"
    position: "左の文書横"
  element_6:
    object: "ペンキ缶（右）"
    detail: "Small paint bucket icon suggesting tone/quality change, blue/green paint drip"
    position: "右の文書横"
  element_7:
    object: "棒人間（指差し）"
    detail: "Stick figure at bottom center pointing up at both results, neutral teaching expression"
    position: "下部中央"
text_elements:
  labels:
    - text: "要約"
      attached_to: "element_2"
    - text: "修正"
      attached_to: "element_3"
    - text: "短くする"
      attached_to: "element_4左矢印"
    - text: "質を変える"
      attached_to: "element_4右矢印"
composition_and_emphasis:
  layout_structure: "Top-center branching to left and right comparison"
  focal_point: "2つの結果文書の対比"
  emphasis_technique: "Size difference (small vs same-size), color accent difference (blue vs orange)"
  color_accents: "Blue watercolor accent on summary side, green watercolor accent on revision side"
  frame_rule: "全ての要素をフレーム内に余裕をもって収めること"
style_application_notes:
  texture_focus: "Marker borders, crayon arrows, watercolor accents on both sides"
  mood_direction: "Curious / Understanding"
```

### 変換プロンプト

```
上から左右への分岐対比構図の手書きスケッチ。
上部中央に元の長い文書があり、テキスト行がたくさん書かれている。
そこから2本の矢印が左下と右下に分岐。左の矢印に「短くする」のラベル、右の矢印に「質を変える」のラベル。
左下に要約の結果として元の3分の1サイズの小さい文書があり、簡潔なテキスト、青いアクセント枠線。横に小さなものさしアイコンがサイズ縮小を示している。「要約」のラベル。青い水彩アクセントが背景に。
右下に修正の結果として元と同じ高さの文書があり、テキストの色やトーンが変わっている。オレンジのアクセント枠線、小さなハートマーク。横にペンキ缶アイコンから青/緑の塗料がたれている。「修正」のラベル。緑の水彩アクセントが背景に。
下部中央に棒人間が上を指さして両方の結果を示している。
紙テクスチャの背景。マーカーペンで描いたようなラフな線。青/緑の水彩風アクセント。全ての要素をフレーム内に余裕をもって収めること。
```

---

## 10-retry.png — 何度でもやり直せる

### YAML

```yaml
image_id: "ep09_10_retry"
concept_title: "何度でもやり直し — 追加指示で微調整"
narrative:
  type: "multi-step-process"
  story: "修正結果を見る→もうちょっと→再修正→もう少し→完成！のループ"
visual_elements:
  element_1:
    object: "修正結果の文書"
    detail: "Document with text, small triangle/caution mark indicating 'not quite right'"
    position: "左側"
  element_2:
    object: "棒人間（首かしげ）"
    detail: "Stick figure tilting head, thinking pose, small speech bubble 'うーん'"
    position: "左下"
  element_3:
    object: "循環矢印"
    detail: "Large curved arrows forming a loop/cycle, orange and green colors, multiple rotation arrows"
    position: "中央"
  element_4:
    object: "追加指示の吹き出し3つ"
    detail: "Three stacked speech bubbles along the loop: 'もっとフォーマルに' / 'もう少し短く' / '最後だけ変えて'"
    position: "循環矢印に沿って"
  element_5:
    object: "完成した文書"
    detail: "Clean polished document with sparkle marks and green checkmark, glowing effect"
    position: "右側"
  element_6:
    object: "棒人間（ガッツポーズ）"
    detail: "Same stick figure now with fist pump and big smile, blue/green watercolor splash behind"
    position: "右下"
text_elements:
  labels:
    - text: "うーん"
      attached_to: "element_2"
    - text: "何度でもOK"
      attached_to: "element_3"
    - text: "納得！"
      attached_to: "element_6"
    - text: "遠慮いらない"
      attached_to: "element_3の下"
composition_and_emphasis:
  layout_structure: "Left-to-Right with central loop cycle"
  focal_point: "完成文書 with sparkles"
  emphasis_technique: "Loop arrows, stacked speech bubbles, sparkle on final result"
  color_accents: "Green watercolor splash behind satisfied stick figure, blue accent on loop arrows"
  frame_rule: "全ての要素をフレーム内に余裕をもって収めること"
style_application_notes:
  texture_focus: "Marker loop arrows, crayon sparkles, watercolor splash"
  mood_direction: "Left: Uncertain → Right: Satisfied"
```

### 変換プロンプト

```
左から右へのフローに循環ループを含む手書きスケッチ。
左側に修正結果の文書があり、小さな三角の注意マークが付いている。左下に首をかしげた棒人間が考えるポーズで、吹き出しに「うーん」。
中央に大きな循環矢印がループを描いており、オレンジと緑の色。ループに沿って3つの吹き出しが並んでいる：「もっとフォーマルに」「もう少し短く」「最後だけ変えて」。ループの上に「何度でもOK」のラベル、下に「遠慮いらない」のラベル。
右側に磨き上げられた完成文書があり、キラキラマーク3つと緑のチェックマーク、発光エフェクト。
右下に同じ棒人間が今度はガッツポーズで大きな笑顔、背景に青/緑の水彩スプラッシュ。「納得！」のラベル。
紙テクスチャの背景。マーカーペンで描いたようなラフな線。青/緑の水彩風アクセント。全ての要素をフレーム内に余裕をもって収めること。
```

---

## 11-variations.png — 修正指示のバリエーション

### YAML

```yaml
image_id: "ep09_11_variations"
concept_title: "修正指示のパターン一覧"
narrative:
  type: "multi-step-process"
  story: "1つのメール下書きから6つの違う指示パターンに分岐する放射型"
visual_elements:
  element_1:
    object: "中央のメール下書き"
    detail: "Document icon in center, labeled 'メール下書き.txt', blue/green watercolor glow around it"
    position: "中央"
  element_2:
    object: "丁寧にアイコン"
    detail: "Small document with ribbon/bow icon, formal elegant feel"
    position: "左上（放射）"
  element_3:
    object: "カジュアルにアイコン"
    detail: "Small document with smiley face, casual wavy border"
    position: "右上（放射）"
  element_4:
    object: "誤字チェックアイコン"
    detail: "Small document with magnifying glass and red pen"
    position: "左中（放射）"
  element_5:
    object: "やさしくアイコン"
    detail: "Small document with child/flower icon, rounded soft edges"
    position: "右中（放射）"
  element_6:
    object: "英語翻訳アイコン"
    detail: "Small document with globe icon, 'ABC' text"
    position: "左下（放射）"
  element_7:
    object: "箇条書きアイコン"
    detail: "Small document with bullet point list visible, neat formatting"
    position: "右下（放射）"
  element_8:
    object: "放射矢印6本"
    detail: "Six hand-drawn arrows radiating from center document to each icon, orange marker"
    position: "中央から各方向"
text_elements:
  labels:
    - text: "丁寧にして"
      attached_to: "element_2"
    - text: "カジュアルに"
      attached_to: "element_3"
    - text: "誤字チェック"
      attached_to: "element_4"
    - text: "やさしくして"
      attached_to: "element_5"
    - text: "英語に翻訳"
      attached_to: "element_6"
composition_and_emphasis:
  layout_structure: "Center-out radial layout"
  focal_point: "中央のメール下書き"
  emphasis_technique: "Watercolor glow on center, orange radiating arrows"
  color_accents: "Blue/green watercolor glow around center document"
  frame_rule: "全ての要素をフレーム内に余裕をもって収めること"
style_application_notes:
  texture_focus: "Marker arrows, crayon icons, watercolor center glow"
  mood_direction: "Organized / Comprehensive"
```

### 変換プロンプト

```
中央から放射状に広がる構図の手書きスケッチ。
中央に「メール下書き.txt」と書かれた文書アイコンがあり、青/緑の水彩の発光効果が背景に広がっている。
中央から6本のオレンジの手描き矢印が放射状に伸びている。
左上に丁寧な文書アイコン（リボン装飾付き）。「丁寧にして」のラベル。
右上にカジュアルな文書アイコン（笑顔マーク、波線の枠）。「カジュアルに」のラベル。
左中に誤字チェックアイコン（虫眼鏡と赤ペン付き文書）。「誤字チェック」のラベル。
右中にやさしい文書アイコン（花アイコン、丸い柔らかい枠）。「やさしくして」のラベル。
左下に英語翻訳アイコン（地球儀付き文書、「ABC」の文字）。「英語に翻訳」のラベル。
右下に箇条書きアイコン（箇条書きリストが見える整形された文書）。
紙テクスチャの背景。マーカーペンで描いたようなラフな線。青/緑の水彩風アクセント。全ての要素をフレーム内に余裕をもって収めること。
```

---

## 12-points.png — ポイント

### YAML

```yaml
image_id: "ep09_12_points"
concept_title: "4つのポイントまとめ"
narrative:
  type: "multi-step-process"
  story: "4つの重要ポイントを上から順に視覚的にまとめる"
visual_elements:
  element_1:
    object: "ポイント1アイコン"
    detail: "Magic wand icon with sparkle, representing 'instructions in Japanese = tone/proofread/rewrite/translate'"
    position: "左上"
  element_2:
    object: "ポイント2アイコン"
    detail: "Shield icon with document and save icon, representing 'save with different name for important files', orange emphasis star"
    position: "右上"
  element_3:
    object: "ポイント3アイコン"
    detail: "Loop/refresh arrow icon, representing 'retry as many times as you want'"
    position: "左下"
  element_4:
    object: "ポイント4アイコン"
    detail: "Shield with checkmark icon, representing 'Allow/Deny confirmation'"
    position: "右下"
  element_5:
    object: "中央タイトル"
    detail: "Hand-drawn banner/ribbon with title text, blue/green watercolor background"
    position: "中央上"
  element_6:
    object: "手描き番号 ①②③④"
    detail: "Circled numbers in orange crayon next to each point"
    position: "各ポイントの左"
  element_7:
    object: "棒人間（メモ取り）"
    detail: "Small stick figure at bottom with notepad, studious expression"
    position: "下部中央"
text_elements:
  labels:
    - text: "日本語で指示"
      attached_to: "element_1"
    - text: "別名で保存"
      attached_to: "element_2"
    - text: "何度もやり直し"
      attached_to: "element_3"
    - text: "Allow確認"
      attached_to: "element_4"
composition_and_emphasis:
  layout_structure: "2x2 grid with central title"
  focal_point: "4つのポイントが均等に目立つ"
  emphasis_technique: "Orange circled numbers, star on point 2 (most important), watercolor banner"
  color_accents: "Blue/green watercolor on central banner, green accent on each icon"
  frame_rule: "全ての要素をフレーム内に余裕をもって収めること"
style_application_notes:
  texture_focus: "Crayon numbers, marker icons, watercolor banner"
  mood_direction: "Organized / Studious"
```

### 変換プロンプト

```
2×2グリッド構図の手書きスケッチ。
中央上に手描きのリボンバナーがあり、青/緑の水彩背景。
左上にオレンジのクレヨンで「①」の番号。魔法の杖アイコンにキラキラ効果。「日本語で指示」のラベル。
右上にオレンジの「②」の番号。盾と文書の保存アイコン、オレンジの強調スター付き。「別名で保存」のラベル。
左下にオレンジの「③」の番号。ループ／リフレッシュの矢印アイコン。「何度もやり直し」のラベル。
右下にオレンジの「④」の番号。チェックマーク付きの盾アイコン。「Allow確認」のラベル。
各アイコンに緑のアクセントカラー。
下部中央にメモ帳を持った真面目な表情の小さな棒人間。
紙テクスチャの背景。マーカーペンで描いたようなラフな線。青/緑の水彩風アクセント。全ての要素をフレーム内に余裕をもって収めること。
```

---

## 13-troubleshoot.png — トラブルシュート

### YAML

```yaml
image_id: "ep09_13_troubleshoot"
concept_title: "よくある問題と対処法"
narrative:
  type: "comparison"
  story: "左に問題、右に対処法。4つの問題をペアで示す"
visual_elements:
  element_1:
    object: "問題①：ファイルが見つからない"
    detail: "Document icon with red question mark, error message bubble"
    position: "左上"
  element_2:
    object: "対処①：@候補から選ぶ"
    detail: "Terminal showing @ with dropdown suggestion list, green checkmark"
    position: "右上"
  element_3:
    object: "問題②：意図と違う結果"
    detail: "Document with wavy lines suggesting wrong content, sad face"
    position: "左中"
  element_4:
    object: "対処②：追加指示"
    detail: "Speech bubble showing 'もっと〜して', arrow pointing to improved document"
    position: "右中"
  element_5:
    object: "問題③：上書きされた"
    detail: "Document with red X, crossed out text"
    position: "左下"
  element_6:
    object: "対処③：次回は別名保存"
    detail: "Two documents side by side with green arrow and save icon"
    position: "右下"
  element_7:
    object: "中央の仕切り線"
    detail: "Vertical dashed line with lightning bolt icon, orange marker"
    position: "中央"
  element_8:
    object: "矢印（各ペア）"
    detail: "Three horizontal arrows from each problem to solution, green color"
    position: "各行の中央"
text_elements:
  labels:
    - text: "見つからない"
      attached_to: "element_1"
    - text: "@で候補表示"
      attached_to: "element_2"
    - text: "意図と違う"
      attached_to: "element_3"
    - text: "追加で指示"
      attached_to: "element_4"
    - text: "別名で保存"
      attached_to: "element_6"
composition_and_emphasis:
  layout_structure: "Left problems → Right solutions, 3 rows"
  focal_point: "問題→解決の矢印フロー"
  emphasis_technique: "Red marks on problems, green checks on solutions"
  color_accents: "Green solution arrows, blue/green watercolor accent on solution side"
  frame_rule: "全ての要素をフレーム内に余裕をもって収めること"
style_application_notes:
  texture_focus: "Red marker for problems, green crayon for solutions, marker dashed line"
  mood_direction: "Worried → Relieved (left to right)"
```

### 変換プロンプト

```
左右対比の3行構図の手書きスケッチ。中央に縦の点線が雷マーク付きで引かれている。
1行目：左に赤い「？」マーク付きの文書アイコンとエラー吹き出し。「見つからない」のラベル。緑の矢印が右へ。右にターミナル画面で「@」を打つとドロップダウン候補リストが表示されている。緑のチェックマーク。「@で候補表示」のラベル。
2行目：左に波線で内容が違うことを示す文書と悲しい顔。「意図と違う」のラベル。緑の矢印が右へ。右に吹き出しで「もっと〜して」の追加指示、矢印の先に改善された文書。「追加で指示」のラベル。
3行目：左に赤い×印で上書きされた文書、取り消し線。緑の矢印が右へ。右に2つの文書が並び、保存アイコンと緑の矢印。「別名で保存」のラベル。
右側全体に薄い青/緑の水彩アクセント。
紙テクスチャの背景。マーカーペンで描いたようなラフな線。青/緑の水彩風アクセント。全ての要素をフレーム内に余裕をもって収めること。
```

---

## 14-summary.png — まとめ

### YAML

```yaml
image_id: "ep09_14_summary"
concept_title: "第9回まとめ"
narrative:
  type: "journey"
  story: "今回学んだ4つのスキルが道に並び、ゴールの旗に続く"
visual_elements:
  element_1:
    object: "道のスタート地点"
    detail: "Starting mark with stick figure waving, small terminal icon"
    position: "左端"
  element_2:
    object: "トーン変更マイルストーン"
    detail: "Document pair (formal→casual) connected by small arrow, on the path"
    position: "左中"
  element_3:
    object: "校正マイルストーン"
    detail: "Document with magnifying glass and red pen, on the path"
    position: "中央左"
  element_4:
    object: "書き換えマイルストーン"
    detail: "Document with child icon and flower, on the path"
    position: "中央右"
  element_5:
    object: "翻訳マイルストーン"
    detail: "Document with globe icon, on the path"
    position: "右中"
  element_6:
    object: "道/パス"
    detail: "Winding hand-drawn path connecting all milestones, blue/green watercolor painted"
    position: "全体を横断"
  element_7:
    object: "ゴール：次回予告"
    detail: "Orange flag with sparkle marks at the end, small desktop/folder icon next to it"
    position: "右端"
  element_8:
    object: "キーメッセージ吹き出し"
    detail: "Large speech bubble below path: '別名保存で安心', star mark emphasis"
    position: "下部中央"
text_elements:
  labels:
    - text: "トーン変更"
      attached_to: "element_2"
    - text: "校正"
      attached_to: "element_3"
    - text: "書き換え"
      attached_to: "element_4"
    - text: "翻訳"
      attached_to: "element_5"
    - text: "次回も楽しみ"
      attached_to: "element_7"
composition_and_emphasis:
  layout_structure: "Left-to-Right winding path journey"
  focal_point: "ゴールの旗"
  emphasis_technique: "Orange flag, sparkles, watercolor path, star on key message"
  color_accents: "Blue/green watercolor painted path connecting milestones"
  frame_rule: "全ての要素をフレーム内に余裕をもって収めること"
style_application_notes:
  texture_focus: "Watercolor path, marker milestones, crayon flag and sparkles"
  mood_direction: "Accomplished / Forward-looking"
```

### 変換プロンプト

```
左から右へのうねる道の旅路構図の手書きスケッチ。
左端にスタート地点があり、手を振る棒人間と小さなターミナルアイコン。
青/緑の水彩で彩色されたうねる道が画面を横断している。
道に沿って4つのマイルストーンが並ぶ：
1つ目は堅い文書→カジュアルな文書の小さなペアが矢印で繋がっている。「トーン変更」のラベル。
2つ目は虫眼鏡と赤ペン付きの文書アイコン。「校正」のラベル。
3つ目は子どものアイコンと花の付いた文書。「書き換え」のラベル。
4つ目は地球儀付きの文書アイコン。「翻訳」のラベル。
右端にオレンジの大きな旗がキラキラマーク付きではためいており、横にデスクトップ/フォルダの小さなアイコン。「次回も楽しみ」のラベル。
下部中央に大きな吹き出しで「別名保存で安心」、スターマークの強調。
紙テクスチャの背景。マーカーペンで描いたようなラフな線。青/緑の水彩風アクセント。全ての要素をフレーム内に余裕をもって収めること。
```
