
from turtle import *

bgcolor('#ff90ab')
speed(-1)

color=['#a71594','#8e6d86','#9c8c51',
       '#fe6960','#9d1722','#c9031a']

for i in range(150):
    pencolor(color[i%6])
    circle(190-i/2,90)
    left(90)
    circle(190-i/3,90)
    left(60)

done()