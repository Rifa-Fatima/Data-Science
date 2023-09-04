from turtle import *
speed('fastest')
colors = ['red','yellow','blue','green']
#square
#for i in range(100):
    #print(i%4,colors[i%4])
    #pencolor(colors[i%4])
    #fd(i*5)
    #lt(90)

for i in range(100):
    pencolor(colors[i%4])
    fd(i*2)
    lt(60)
    circle(i*2,90)                         #to draw arc or multiple circle
mainloop()
