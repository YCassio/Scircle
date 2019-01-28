'''#三角形
from turtle import  *
setup(300,400,200,200)
pensize(2)
pencolor("blue")
pendown()
seth(0)
fd(50)
seth(120)
fd(50)
seth(-120)
fd(50)
#done()
'''
#叠加三角形
from turtle import  *
setup(300,400,200,200)
pensize(2)
pencolor("blue")
pendown()
seth(0)
fd(50)
seth(120)
fd(50)
seth(-120)
fd(50)
fd(50)
seth(0)
fd(100)
seth(120)
fd(50)
seth(-120)
fd(50)
seth(120)
fd(50)
#done()

'''
#无角正方形
from turtle import  *
setup(500,500,200,200)
pensize(2)
pencolor("red")
k = 0
up()
seth(k)
for i in range(0,4):
    fd(10)
    down()
    fd(50)
    up()
    fd(10)
    k += 90
    seth(k)


#六角形绘制
from turtle import  *
setup(500,500,200,200)
pensize(2)
pencolor("red")




#正方形螺旋线绘制
from turtle import  *
setup(500,500,200,200)
pensize(2)
pencolor("green")
seth(90)
for i in range(20):
    fd()


'''











