from turtle import *
speed('slowest')
pencolor('red')
\
# range(stop)
# range(start,stop)
# range(start,stop,step)

for i in range(1,11):
 fd(90)
 lt(360/10)
 dot(10,'green')
 write (i,font=('Calibri',20,'bold'))


#reverse
goto(100,100)
for i in range(10,0,-1):
 fd(60)
 lt(360/10)
 dot(20,'red')
 write(i,font = ('Calibri',20,'bold'))
mainloop()
