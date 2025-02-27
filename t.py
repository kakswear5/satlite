import pgzrun
from random import randint
from time import time

WIDTH=600
HEIGHT=600

satellites=[]
lines=[]
start_time=0
total_time=0
end_time=0

number_of_satellites=10

next_satellite=0


def create_satelite():
    global start_time
    for i in range(number_of_satellites):
        st=Actor("satalite.png")
        st.pos=randint(40,(WIDTH-40)),randint(40,(HEIGHT -40))
        satellites.append(st)
    start_time=time()


def draw ():
    global total_time 
    screen.blit("bg",(0,0))
    num=1
    for satellite in satellites:
        screen.draw.text(str(num),(satellite.pos[0], satellite.pos[1]+20))
        satellite.draw()
        num=num+1
    for line in lines:
        screen.draw.line(line[0],line[1],(255,255,255))

    if next_satellite < number_of_satellites:
        total_time=time()-start_time
        screen.draw.text(str(round(total_time,2)),(25,20),fontsize=20)
    
    else:
        screen.draw.text(str(round(total_time,2)),(25,20),fontsize=20)

def on_mouse_down(pos):
    global next_satellite,lines
    if next_satellite < number_of_satellites:
        if satellites[next_satellite].collidepoint(pos):
            if next_satellite:
                lines.append((satellites[next_satellite-1].pos, satellites[next_satellite].pos))
            next_satellite = next_satellite+1
        else:
            lines = []
            next_satellite = 0


create_satelite()
pgzrun.go()




    

    

