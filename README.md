# Text Preprocessing Tools for Subtitles and Speech Synthesis

このリポジトリは、テキストに含まれるルビ表現（《ふりがな》）を処理するための Python スクリプト2本を収録しています。  
字幕用途および音声読み上げ用途それぞれに適した前処理を行います。

📦 セットアップ
事前に Python 3.7 以上が必要です。依存関係は特にありません（re モジュールのみ使用）。
```
python remove_annotation_word.py --input sample.txt --output sample_subtitle.txt
python remove_kanji_before_ruby.py --input sample.txt --output sample_voicevox.txt
```

## 📄 プロジェクト構成例
```
.
├── LICENSE
├── README.md (いまここ)
├── remove_ananotation_words.py
├── remove_kanji_before_ruby.py
├── requirements.txt
├── sample_subtitle.txt
├── sample_voicevox.txt
└── sample.txt
```

## 📄 スクリプト一覧

### 1. `remove_annotation_word.py` - 字幕用（ルビ付き単語を削除）

- **用途**: 字幕テキストとして表示する際、視認性を重視し、ルビ全体を削除します。
- **変換例**:
```
お世嗣《よつぎ》と皇后《こうごう》は城へ向かった。
→ お世嗣と皇后は城へ向かった。
```

#### ▶️ 使い方

```bash
python remove_annotation_word.py --input input.txt --output output.txt
```
#### 引数	説明
----
- --input	入力テキストファイル（UTF-8）
- --output	出力テキストファイル

### 2. remove_kanji_before_ruby.py - 音声読み上げ用

- **用途**: テキスト音声合成で正しい発音を得るために、ルビの中身だけを残します。漢字は読み上げ時の誤読を防ぐため削除します。

- **変換例**:
```
お世嗣《よつぎ》と皇后《こうごう》は城へ向かった。
→ およつぎとこうごうは城へ向かった。
```

#### ▶️ 使い方
```bash
python remove_kanji_before_ruby.py --input input.txt --output output.txt
```
#### 引数	説明
----
- --input	入力テキストファイル（UTF-8）
- --output	出力テキストファイル

📜 ライセンス
このプロジェクトは MITライセンス の下で公開されています。

🙋‍♂️ 作者
ご質問・ご要望は Issues または GitHub Discussions からどうぞ。