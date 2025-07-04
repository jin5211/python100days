#!/usr/bin/env python3

import os
import logo

print(logo.logo)  # ロゴを表示

# ターミナルの画面をクリアする関数を定義
# os.name が 'nt' の場合は Windows ⇒ 'cls' コマンド
# それ以外（macOS / Linux）の場合は 'clear' コマンドを使用
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# 全ての入札者情報（名前と金額）を格納する辞書
bidders = {}

# 入札ループ（複数のユーザーから情報を集める）
while True:
    # 入札者の名前を取得（バリデーション付き）
    while True:
        name = input("What's your name?: ").strip()
        if name == "":
            print("Name cannot be empty. Please enter your name.")
            continue
        break

    # 入札金額を整数として取得（バリデーション付き）
    while True:
        try:
            bid = int(input("What's your bid?: $"))
            if bid < 0:
                print("You typed negative input. Please try again.")
                continue
            break  # 正しく入力されたらループを抜ける
        except ValueError:
            # 数字以外が入力された場合のエラーメッセージ
            print("You typed wrong input. Please try again.")
            continue

    # 辞書にユーザー名と入札額を追加
    bidders[name] = bid

    # 他の入札者がいるかを確認
    any_other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ")
    if any_other_bidders != "yes":
        break  # もういない場合、ループ終了
    else:
        clear_screen()  # 画面をクリアして入力を開始
        continue

# 最後にもう一度画面をクリアして、勝者を発表する準備
clear_screen()

# 最大入札金額とそのユーザー名を求める処理
max_bid = 0
winner = ''
for key in bidders:
    if bidders[key] > max_bid:
        max_bid = bidders[key]
        winner = key

# 勝者を表示
print(f"The winner is {winner} with a bid of ${max_bid}.")
print("\n"*3)  # 少しスペースをあけて終了
