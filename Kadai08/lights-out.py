print("""
-----ライツアウト-----

1.5x5,3x3,7x7いずれかのパネルがあります
2.毎回座標を入力しその位置から十字型に５マスをひっくり返します
3.パネルにはxとoがあります
3.上記2.を繰り返し全面をoにすることが出来ればクリアとなります
      """)
panelSizeLi = ["",3,5,7] #パネルサイズ

flipCount = 0 #試行回数

#サイズ選択
while True:
        sizeNum = int(input("""
パネルのサイズを選択してください
3x3 >> 1
5x5 >> 2
7x7 >> 3
番号を入力してください:"""))
        if sizeNum in [1,2,3]:
            break

#サイズに応じてパネルを作成
panelLi = [["x" for _ in range(panelSizeLi[sizeNum])] for _ in range(panelSizeLi[sizeNum])]

#上下左右方向の座標
directionLi = [(0,-1),
               (1,0),
               (0,1),
               (-1,0)]

#パネル表示用
def ShowPanel():
    num = 1
    print(f"""
  {" ".join([str(i) for i in range(1,panelSizeLi[sizeNum] + 1)])}""")
    for i in panelLi:
        print(f"{num} "+" ".join(i))
        num += 1
    print(f"""
動かした回数:{flipCount}回
          """)


#ひっくり返す処理
def PanelChange(y,x):
    global flipCount

    if panelLi[y][x] == "x":
        panelLi[y][x] = "o"
    else:
        panelLi[y][x] = "x"
    for dx,dy in directionLi:
        if 0 <= x+dx < panelSizeLi[sizeNum] and 0 <= y+dy < panelSizeLi[sizeNum]:
            if panelLi[y+dy][x+dx] == "x":
                panelLi[y+dy][x+dx] = "o"
            else:
                panelLi[y+dy][x+dx] = "x"
    flipCount += 1

#パネルリセット処理
def PanelReset():
    for y in range(panelSizeLi[sizeNum]):
        for x in range(panelSizeLi[sizeNum]):
            panelLi[y][x] = "x"
    print("---パネルがリセットされました---")



ShowPanel()


#メイン処理
while True:
    clear = True #クリアフラグ
    y,x = 0,0 #座標用

    #マス選択(列ごと)
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

    #ゲーム終了かどうか
    if y == 9 or x == 9:
        print("---ゲームを終了します---")
        break
    #パネルリセットかどうか
    elif y == 0 or x == 0:
        PanelReset()
    #ひっくり返す
    else:
        PanelChange(y-1,x-1)

    ShowPanel()

    #×が含まれている場合にクリア判定をfalse
    for i in panelLi:
        if "x" in i:
            clear = False

    #フラグがtrueならクリアで終了
    if clear:
        print("ゲームクリア！！")
        print(f"記録:{flipCount}回！！")
        break



#こだわり
#上下左右の座標をリストにすることでひっくり返す処理がしやすくなるようにした
