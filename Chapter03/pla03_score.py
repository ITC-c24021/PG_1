engScore = int(input("英語の点数を数字で入力してください:"))
mathScore = int(input("数学の点数を数字で入力してください:"))

totalRank = ""

if engScore >= 90 and mathScore >= 90:
    totalRank = "S"
elif engScore >= 70 or mathScore >= 70:
    totalRank = "A"
elif engScore >= 50 or mathScore >= 50:
    totalRank = "B"
elif engScore < 50 and mathScore < 50:
    totalRank = "C"
else:
    totalRank = "不明"

print(f"あなたの成績は{totalRank}です")
