import time
import math
import random
import mcpi.minecraft as minecraft
import minecraft.minecraft as mcraft
import mcpi.block as block

AIR=0
DIRT=3
SAND=12
SANDSTONE=24
GOLD = 41
TNT = 46

mc = minecraft.Minecraft.create()

def roundVec3(vec3):
    return minecraft.Vec3(int(vec3.x),int(vec3.y),int(vec3.z))

def CreatePyramid(posx,posy,posz,width,mybase,mywalls,mytopblock):
    mc.postToChat("creating")
    if width%2==0:
        width=width+1

    height = (width+1)/2
    halfsize = int(math.floor(width/2))
    print "player : {} {} {}".format(posx,posy,posz)
    print "size : {} H : {} Halfsize : {}".format(width,height,halfsize)

    print "create base"
    mc.setBlocks(posx-halfsize-2,posy-2,posz-halfsize-2,posx+halfsize+2,posy-2,posz+halfsize+2,DIRT)
    mc.setBlocks(posx-halfsize-2,posy-1,posz-halfsize-2,posx+halfsize+2,posy-1,posz+halfsize+2,mybase,1)
    #mc.setBlocks(posx-halfsize-2,posy-2,posy-halfsize-2,posx+halfsize+2,posy-2,posz+halfsize+2,DIRT)
    #mc.setBlocks(posx-halfsize-2,posy-1,posy-halfsize-2,posx+halfsize+2,posy-1,posz+halfsize+2,mybase)

    print "create pyramid"
    for y in range (posy,posy+height):
        mc.setBlocks(posx-halfsize,y,posz-halfsize,posx+halfsize,y,posz+halfsize,mywalls)
        #mc.setBlocks(posx-halfsize,y,posy-halfsize,posx+halfsize+2,posy,y,posz+halfsize,mywalls)
        halfsize=halfsize-1

    print "set top block"
    mc.setBlock(posx,posy+height-1,posz,mytopblock)
    print "player on top"
    mc.player.setPos(posx,posy+height,posz)

mc.setBlocks(-40,0,-128,128,-128,128,SANDSTONE)
mc.setBlocks(-128,1,-128,128,128,128,AIR)
time.sleep(8)

aa=-40
bb=1
cc=40
dd=21

ccc=cc%2
bbb=bb%2
ddd=dd%2

CreatePyramid(aa,bb,cc,dd,GOLD,GOLD,GOLD)
#CreatePyramid(-40,1,40,21,TNT,SANDSTONE,TNT)
#CreatePyramid(-40,1,40,21,SANDSTONE,SANDSTONE,SANDSTONE)
#CreatePyramid(-40,1,-40,21,SANDSTONE,SANDSTONE,SANDSTONE)
#CreatePyramid(40,1,40,21,SANDSTONE,SANDSTONE,SANDSTONE)
#CreatePyramid(40,1,-40,21,SANDSTONE,SANDSTONE,SANDSTONE)

#CreatePyramid(0,1,45,31,SANDSTONE,SANDSTONE,SANDSTONE)
#CreatePyramid(0,1,-45,31,SANDSTONE,SANDSTONE,SANDSTONE)
#CreatePyramid(45,1,0,31,SANDSTONE,SANDSTONE,SANDSTONE)
#CreatePyramid(-45,1,0,31,SANDSTONE,SANDSTONE,SANDSTONE)

time.sleep(8)

playerPos=mc.player.getPos()

print "player : {} {} {}".format(playerPos.x,playerPos.y,playerPos.z)

#mc.player.setPos(playerPos.x,playerPos.y,playerPos.z)
"""ee=(abs(playerPos.x)-(abs(playerPos.x % 10)*-1))
ff=(abs(playerPos.y)-(abs(playerPos.y % 2)*-1))
gg=(abs(playerPos.z)-(abs(playerPos.z % 10)*-1))

print ee, ff, gg
"""
randomBlockPos=roundVec3(playerPos)
#randomBlockPos.x=random.randint((float(playerPos.x) %2)*-1,float(playerPos.x) %2)  # Integer from 1 to 10, endpoints includedrand
#randomBlockPos.x=random.randrange(randomBlockPos.x-ee,randomBlockPos.x+ee)

#randomBlockPos.x=random.uniform((float(playerPos.x) %2),float(playerPos.x) %2)*-1  # Integer from 1 to 10, endpoints includedrand
#randomBlockPos.y=random.randint((float(playerPos.y) %2)*-1,float(playerPos.y) %2)  # Integer from 1 to 10, endpoints includedrand
#randomBlockPos.z=random.randint((float(playerPos.z) %2)*-1,float(playerPos.z) %2)  # Integer from 1 to 10, endpoints includedrand

randomBlockPos.x=random.randint(-3,3)
randomBlockPos.y=random.randint(1,2)
randomBlockPos.z=random.randint(-3,3)


print randomBlockPos

mc.setBlock(randomBlockPos.x, randomBlockPos.y,randomBlockPos.z, TNT,1)
mc.postToChat("a tnt block has been hidden - go find")
mc.postToChat((playerPos))


mc.player.setPos(randomBlockPos.x+1, randomBlockPos.y-1,randomBlockPos.z+1)
#mc.player.setPos(playerPos.x+15,playerPos.y+10,playerPos.z)
