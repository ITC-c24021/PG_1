import random

marks = ["ダイヤ",
         "クローバー",
         "ハート",
         "スペード"]
nums = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

cards = list(m +"の"+ n for m in marks for n in nums)

random.shuffle(cards)

pick_list = [cards[i]for i in range(5)]

print("あなたが引いたトランプは,")
for i in pick_list:
    print(i)
print("です。")
