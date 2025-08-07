seizaLi = ["山羊座","水瓶座","魚座",
           "牡羊座","牡牛座","双子座",
           "蟹座","獅子座","乙女座",
           "天秤座","蠍座","射手座"]

dayLi = [22,20,19,21,20,21,22,23,23,23,24,23]

month = int(input("生まれた月を数字で入力してください:")) -12
day = int(input("生まれた日を数字で入力してください:"))


if dayLi[month] <= day:
    print(f"あなたの星座は{seizaLi[month]}です")
else:
    print(f"あなたの星座は{seizaLi[month-1]}です")
