import turtle

def tree(branchLen, t):
    if branchLen > 5:
        t.forward(branchLen)    # 画树干
        t.right(20)             # 右倾 20 度
        tree(branchLen-15, t)   # 减小规模，树干减 15
        t.left(40)              # 左倾 40 度，即左 20
        tree(branchLen-15, t)   # 减小规模，树干减 15
        t.right(20)             # 回右倾 20 度，即回正
        t.backward(branchLen)   # 画笔回到原位置

def main():
    t = turtle.Turtle()     # 生成海龟
    myWin = turtle.Screen()
    t.left(90)              # 调整海龟位置
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75, t)             # 画树，树干长度 75
    myWin.exitonclick()

if __name__ == "__main__":
    main()