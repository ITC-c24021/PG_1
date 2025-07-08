import random

num = random.randint(1,10)

answerCount = 0
while True:
    answer = int(input("1から10の数字のどれかを予想して数字で入力してください:"))
    answerCount += 1
    if answer == num:
        print("当たりです！")
        break
    elif answerCount >= 10:
        print("残念です！")
        break
    elif answer > num:
        print("数字が大きいです")
    else:
        print("数字が小さいです")


