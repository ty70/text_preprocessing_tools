# -----------------------------------------------
# remove_kanji_before_ruby.py
#
# 《...》のルビの直前に連続する漢字を削除し、ルビの中身だけを残すスクリプト
#
# 入力:
#   --input: 入力テキストファイルのパス（UTF-8）
#   --output: 出力テキストファイルのパス
#
# 出力:
#   《...》の直前にある連続漢字と《》を削除し、ルビ内文字列だけを出力
# -----------------------------------------------

import argparse
import re

def replace_kanji_ruby(text):
    # ([\u4E00-\u9FFF]+)：連続した漢字
    # 《(.*?)》：ルビ
    # → ルビだけを残す（《》も削除）
    return re.sub(r'[\u4E00-\u9FFF]+《(.*?)》', r'\1', text)

def main():
    parser = argparse.ArgumentParser(description="漢字+ルビの漢字部分と《》を削除し、ルビだけを残す")
    parser.add_argument('--input', required=True, help='入力ファイル（UTF-8）')
    parser.add_argument('--output', required=True, help='出力ファイル')
    args = parser.parse_args()

    # 入力ファイル読み込み
    with open(args.input, 'r', encoding='utf-8') as infile:
        text = infile.read()

    # 漢字+ルビ→ルビのみ へ変換
    result = replace_kanji_ruby(text)

    # 出力ファイル書き込み
    with open(args.output, 'w', encoding='utf-8') as outfile:
        outfile.write(result)

    print(f"✅ 処理が完了しました: {args.output}")

if __name__ == '__main__':
    main()
