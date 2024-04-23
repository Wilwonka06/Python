
from turtle import *

bgcolor('white')
speed(-1)

color=['#a71594','#ffaaa6','#ff8c94',
       '#fe6960','#9d1722','#c9031a']

for i in range(150):
    pencolor(color[i%6])
    circle(190-i/2,90)
    left(90)
    circle(190-i/3,90)
    left(60)

done()