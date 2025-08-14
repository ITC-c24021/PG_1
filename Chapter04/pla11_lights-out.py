print("""
-----ライツアウト-----

1.5x5,3x3,7x7いずれかのパネルがあります
2.毎回座標を入力しその位置から十字型にパネルをひっくり返します
3.上記2.を繰り返し全面をひっくり返すことが出来ればクリアとなります
      """)
panelSizeLi = ["",3,5,7]
while True:
        sizeNum = int(input("""
パネルのサイズを選択してください
3x3 >> 1
5x5 >> 2
7x7 >> 3
番号を入力してください:"""))
        if sizeNum in [1,2,3]:
            break

panelLi = [["□" for _ in range(panelSizeLi[sizeNum])] for _ in range(panelSizeLi[sizeNum])]

directionLi = [(0,-1),
               (1,0),
               (0,1),
               (-1,0)]

def ShowPanel():
    num = 1
    print(f"""
  {" ".join([str(i) for i in range(1,panelSizeLi[sizeNum] + 1)])}""")
    for i in panelLi:
        print(f"{num} "+" ".join(i))
        num += 1


def PanelChange(y,x):
    print(y,x)
    if panelLi[y][x] == "□":
        panelLi[y][x] = "■"
    else:
        panelLi[y][x] = "□"
    for dx,dy in directionLi:
        if 0 <= x+dx < panelSizeLi[sizeNum] and 0 <= y+dy < panelSizeLi[sizeNum]:
            if panelLi[y+dy][x+dx] == "□":
                panelLi[y+dy][x+dx] = "■"
            else:
                panelLi[y+dy][x+dx] = "□"

def PanelReset():
    for y in range(panelSizeLi[sizeNum]):
        for x in range(panelSizeLi[sizeNum]):
            panelLi[y][x] = "□"
    print("---パネルがリセットされました---")



ShowPanel()


while True:
    clear = True
    y,x = 0,0
    while True:
        try:
            y = int(input("\n縦の行を選択して番号を入力してください(ゲーム終了>> 9,パネルリセット>> 0):"))
            if 0 <= y <= panelSizeLi[sizeNum] or y == 9:
                break
        except ValueError:
            print("\n正しく入力してください:")
    while True:
        if y == 0 or y == 9:
            break
        try:
            x = int(input("\n横の行を選択して番号を入力してください(ゲーム終了>> 9,パネルリセット>> 0):"))
            if 0 <= x <= panelSizeLi[sizeNum] or x == 9:
                break
        except ValueError:
            print("\n正しく入力してください:")

    if y == 9 or x == 9:
        print("---ゲームを終了します---")
        break
    elif y == 0 or x == 0:
        PanelReset()
    else:
        PanelChange(y-1,x-1)

    ShowPanel()

    for i in panelLi:
        if "□" in i:
            clear = False

    if clear:
        print("ゲームクリア！！")
        break




