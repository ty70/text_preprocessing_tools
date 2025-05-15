# -----------------------------------------------
# remove_annotation_words.py
#
# 《...》で囲まれた注釈付きの単語を含む語句を削除するスクリプト
#
# 用途:
#   青空文庫の文章で、ルビ注記付きの語（例: お世嗣《よつぎ》）を削除して
#   読みやすいプレーンテキストに変換したい場合に使用
#
# 入力:
#   --input: 入力ファイルのパス（UTF-8）
#   --output: 出力ファイルのパス
#
# 出力:
#   《...》付き語句を除去したテキストを指定された出力ファイルに保存
# -----------------------------------------------

import argparse
import re

def remove_annotated_words(text):
    """
    《...》付きの語を削除（例：お世嗣《よつぎ》 → 削除）
    """
    pattern = r'\S*《[^《》]*》'  # 《...》を含む単語にマッチ
    return re.sub(pattern, '', text)

def main():
    parser = argparse.ArgumentParser(description="《...》付き注釈語を削除するスクリプト")
    parser.add_argument('--input', required=True, help='入力テキストファイルのパス（UTF-8）')
    parser.add_argument('--output', required=True, help='出力テキストファイルのパス')
    args = parser.parse_args()

    # 入力ファイルを読み込み
    with open(args.input, 'r', encoding='utf-8') as infile:
        original_text = infile.read()

    # 注釈付き語を削除
    cleaned_text = remove_annotated_words(original_text)

    # 結果を出力ファイルに書き込み
    with open(args.output, 'w', encoding='utf-8') as outfile:
        outfile.write(cleaned_text)

    print(f"✅ 処理が完了しました: {args.output}")

if __name__ == '__main__':
    main()
