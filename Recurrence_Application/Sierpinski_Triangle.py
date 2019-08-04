import turtle

def sierpinski(points, degree, myTurtle):
    
    colormap = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
    drawTriangle(points, colormap[degree], myTurtle)    # 等边三角形

    if degree > 0:      
        '''
        最小规模，0 直接退出
        减小规模：getMid() 边长减半
        调用自身，左上右次序
        '''
        sierpinski([points[0], getMid(points[0], points[1]), getMid(points[0], points[2])], degree-1, myTurtle)
        sierpinski([getMid(points[0], points[1]), points[1], getMid(points[1], points[2])], degree-1, myTurtle)
        sierpinski([getMid(points[0], points[2]), getMid(points[2], points[1]), points[2]], degree-1, myTurtle)

def drawTriangle(points, color, myTurtle):
    '''
    画指定顶点的等边三角形，指定填充颜色
    1. 抬笔到左顶点
    2. 落笔开始填充
    3. 到上顶点
    4. 到右顶点
    5. 回到左顶点闭合
    '''
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0], points[1][1])
    myTurtle.goto(points[2][0], points[2][1])
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.end_fill()

def getMid(p1, p2):     # 取两点的中点
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def main():
    myTurtle = turtle.Turtle()
    myWin = turtle.Screen()
    myPoints = [[-200,-100], [0,200], [200,-100]]   # 外轮廓的三个顶点
    sierpinski(myPoints, 3, myTurtle)
    myWin.exitonclick()

main()