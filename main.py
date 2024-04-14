import math
import copy
import time
import random 
from collections import defaultdict
 

from cmu_112_graphics import *

#acknowlegement
#key hold function: https://stackoverflow.com/questions/27215326/tkinter-keypress-and-keyrelease-events
#artistic resource: https://www.bilibili.com/video/BV1zr4y1775y/?spm_id_from=333.337.top_right_bar_window_default_collection.content.click&vd_source=d6c6981f815f31d5720b99d6fbfeeb80
                    #https://github.com/hk-modding/api
                    #from https://prts.wiki/w/%E9%A6%96%E9%A1%B5
                    #from hollow knight
                    #from tingchen

g=3
###################################some default helper#####################

def isOdd(n):
    if abs(n/2-n//2)>0:
        return True
    return False

def normalized(L):
    l=math.sqrt(L[0]**2+L[1]**2)
    C=[L[0]/l,L[1]/l]
    return C 

def contactWallLeft(L,block):
        for each in L:
            x=each[0]
            y=each[1]
            lx0=block.parameter[0][0]
            ly0=block.parameter[0][1]
            lx1=block.parameter[1][0]
            ly1=block.parameter[1][1]
            if lx0<=x<=lx1 and ly0<=y<=ly1:
                return True 
        return False
def contactWallRight(L,block):
        for each in L:
            x=each[0]
            y=each[1]
            lx0=block.parameter[0][0]
            ly0=block.parameter[0][1]
            lx1=block.parameter[1][0]
            ly1=block.parameter[1][1]
            if lx0<=x<=lx1 and ly0<=y<=ly1:
                return True 
        return False
def contactGround(L,block):
        for each in L:
            x=each[0]
            y=each[1]
            lx0=block.parameter[0][0]
            ly0=block.parameter[0][1]
            lx1=block.parameter[1][0]
            ly1=block.parameter[1][1]
            if lx0<=x+27<=lx1 and ly0<=y<=ly1:
                return True
            return False
def contactCeiling(L,block):
        for each in L:
            x=each[0]
            y=each[1]
            lx0=block.parameter[0][0]
            ly0=block.parameter[0][1]
            lx1=block.parameter[1][0]
            ly1=block.parameter[1][1]
            if lx0<=x<=lx1 and ly0<=y<=ly1:
                return True
            return False
##################################OOP stuff################################
class Game():
    phase="help"
    w=False
    backgroundMode=False
    complexBossAnimation=False

    def __init__(self):
        return 
    @classmethod
    def begin(cls):
        if Game.phase!=1:
            Game.phase=1
            Game.w=False
    @classmethod       
    def beginLast(cls):
        if Game.phase!='FN':
            Game.phase="FN"
            Game.w=False
    @classmethod
    def end(cls):
        if Game.phase!=2:
            Game.phase=2 
            Game.w=False
    @classmethod
    def win(cls):
        Game.w=True
        Button.num+=1

    @classmethod
    def practice(cls):
        if Game.phase!="practice":
            Game.phase="practice"
class Button():
    button=[]
    rTimer=0
    num=0
    def __init__(self,parameter,name):
        self.parameter=parameter
        self.name=name
        self.num=0
        Button.button.append(self)
    @classmethod
    def reminder(cls):
        Button.rTimer=50
    @property
    def locked(self):
        if (self.name=="Attuned: Frostnova" or self.name=="Ascended: Frostnova"
            or self.name=="Radient: Frostnova"):
            if Button.num<1:
                return True 
        return False
    
    @classmethod
    def timerFired(cls,app):
        if Button.rTimer>0:
            Button.rTimer-=1
    @classmethod
    def mousePressed(cls,app,event):
        if Button.button!=[]:
            for bot in Button.button:
                x0=bot.parameter[0][0]
                y0=bot.parameter[0][1]
                x1=bot.parameter[1][0]
                y1=bot.parameter[1][1]
                if x0<=event.x<=x1 and y0<=event.y<=y1:
                    bot.pressed(app)
        return None
    def pressed(self,app):
        if self.name=="Attuned: The Flying Columbian" and Game.phase==0: #default mode
            Game.begin()
            miku.position=[600,400]
            Landscape.landscapes=[]
            ground=Landscape([[-600,700],[1700,900]],"ground")
            wall0=Landscape([[-600,0],[10,900]],"wall")
            wall1=Landscape([[1440,0],[2000,900]],"wall")
            bump=Landscape([[400,600],[500,650]],"terrain")
    
            app.damage=1
            daidai=DaiBao()  
            miku.health=9
            miku.rage=0
            daidai.maxHealth=810
            Game.w=False
        elif self.name=="Ascended: The Flying Columbian" and Game.phase==0:
            Game.begin()
            Landscape.landscapes=[]
            ground=Landscape([[-600,700],[1700,900]],"ground")
            wall0=Landscape([[-600,0],[10,900]],"wall")
            wall1=Landscape([[1440,0],[2000,900]],"wall")
            bump=Landscape([[400,600],[500,650]],"terrain")
            miku.rage=0
            miku.position=[600,400]
            app.damage=2
            daidai=DaiBao()
            miku.health=9
            daidai.health=1000
            daidai.maxHealth=1000
            Game.w=False
        elif self.name=="Radient: The Flying Columbian" and Game.phase==0: #one hit kill mod
            Game.begin()
            Landscape.landscapes=[]
            miku.rage=0
            ground=Landscape([[-600,700],[1700,900]],"ground")
            wall0=Landscape([[-600,0],[10,900]],"wall")
            wall1=Landscape([[1440,0],[2000,900]],"wall")
            bump=Landscape([[400,600],[500,650]],"terrain")
            
            miku.position=[600,400]
            miku.health=9
            app.damage=114514
            daidai=DaiBao()
            daidai.health=1200
            daidai.maxHealth=1200
            Game.w=False
        elif self.name=="Practice" and Game.phase==0:
            Game.practice()
            miku.rage=0
            Landscape.landscapes=[]
            Landscape.generated={0,1,2}

            miku.health=9
            ground=Landscape([[-600,700],[1700,900]],"ground")
            wall0=Landscape([[-600,0],[10,900]],"wall")
            Game.w=False
        elif self.name=="Help" and Game.phase==0:
            Game.phase="help"
            Game.w=False
            miku.rage=0
        elif self.name=="Attuned: Frostnova" and Game.phase==0:
            if self.locked==True:
                Button.reminder()
                return
            else:
                Game.beginLast()
                miku.position=[600,400]
                Landscape.landscapes=[]
                ground=Landscape([[-600,700],[1700,900]],"ground")
                wall0=Landscape([[-600,0],[10,900]],"wall")
                wall1=Landscape([[1440,0],[2000,900]],"wall")
                app.damage=1
                fn=FN([1200,400])  
                miku.health=9
                fn.maxHealth=1000
                fn.health=1000
                Game.w=False
                miku.rage=0

        elif self.name=="Ascended: Frostnova" and Game.phase==0:
            if self.locked==True:
                Button.reminder()
                return
            else:
                Game.beginLast()
                miku.position=[600,400]
                Landscape.landscapes=[]
                ground=Landscape([[-600,700],[1700,900]],"ground")
                wall0=Landscape([[-600,0],[10,900]],"wall")
                wall1=Landscape([[1440,0],[2000,900]],"wall")
                app.damage=2
                fn=FN([1200,400])  
                miku.health=9
                fn.maxHealth=1300
                fn.health=1300
                miku.rage=0
                Game.w=False
            pass
        elif self.name=="Radient: Frostnova" and Game.phase==0:
            if self.locked==True:
                Button.reminder()
                return
            else:
                Game.beginLast()
                miku.position=[600,400]
                Landscape.landscapes=[]
                ground=Landscape([[-600,700],[1700,900]],"ground")
                wall0=Landscape([[-600,0],[10,900]],"wall")
                wall1=Landscape([[1440,0],[2000,900]],"wall")
                app.damage=114514
                fn=FN([1200,400])  
                miku.health=9
                fn.maxHealth=1500
                fn.health=1500
                Game.w=False
                miku.rage=0
            pass
        elif self.name=="Background" and Game.phase==0:
            if Game.backgroundMode==True:
                Game.backgroundMode=False
            elif Game.backgroundMode==False:
                Game.backgroundMode=True
        elif self.name=="Boss Animation" and Game.phase==0:
            if Game.complexBossAnimation==True:
                Game.complexBossAnimation=False
            elif Game.complexBossAnimation==False:
                Game.complexBossAnimation=True



b0=Button([[550-150,400],[550+150,500]],"Attuned: The Flying Columbian")
b1=Button([[550-150,550],[550+150,650]],"Ascended: The Flying Columbian")
b2=Button([[550-150,700],[550+150,800]],"Radient: The Flying Columbian")
b3=Button([[200-150,550],[200+150,750]],"Practice")
b4=Button([[200-150,150],[200+150,350]],"Help")

b5=Button([[900-150,400],[900+150,500]],"Attuned: Frostnova")
b6=Button([[900-150,550],[900+150,650]],"Ascended: Frostnova")
b7=Button([[900-150,700],[900+150,800]],"Radient: Frostnova")

b8=Button([[1220-150,200],[1220+150,300]],"Background")
b9=Button([[1220-150,400],[1220+150,500]],"Boss Animation")

class Icicle():
    icicleList=[]
    def __init__(self,position,status):
        self.position=position 
        self.status= status
        self.timer=50
        Icicle.icicleList.append(self)
    @property
    def parameter(self):
        return [[self.position[0]-27,self.position[1]-700],
        [self.position[0]+27,self.position[1]+20]]
    @property
    def hitBox(self):
        return [[self.position[0]-17,self.position[1]-500],
        [self.position[0]+17,self.position[1]-500],
        [self.position[0]-17,self.position[1]-450],
        [self.position[0]+17,self.position[1]-450],
        [self.position[0]-17,self.position[1]-400],
        [self.position[0]+17,self.position[1]-400],
        [self.position[0]-17,self.position[1]-350],
        [self.position[0]+17,self.position[1]-350],
        [self.position[0]-17,self.position[1]-300],
        [self.position[0]+17,self.position[1]-300],
        [self.position[0]-17,self.position[1]-250],
        [self.position[0]+17,self.position[1]-250],
        [self.position[0]-17,self.position[1]-200],
        [self.position[0]+17,self.position[1]-200],
        [self.position[0]-17,self.position[1]-150],
        [self.position[0]+17,self.position[1]-150],
        [self.position[0]-17,self.position[1]-100],
        [self.position[0]+17,self.position[1]-100],
        [self.position[0]-17,self.position[1]-50],
        [self.position[0]+17,self.position[1]-50],
        [self.position[0]-17,self.position[1]],
        [self.position[0]+17,self.position[1]],
        [self.position[0],self.position[1]]]
    @classmethod
    def hit(cls):
        x0=miku.position[0]-27 
        y0=miku.position[1]-44
        x1=miku.position[0]+27 
        y1=miku.position[1]+44
        if Icicle.icicleList!=[]:
            for each in Icicle.icicleList:
                if each.status=="real":
                    for point in each.hitBox:
                        if x0<=point[0]<=x1 and y0<=point[1]<=y1 and miku.invinsible==False:
                            return True
    @classmethod
    def timerFired(cls,app):
        if Icicle.hit():
            miku.health-=app.damage
            miku.invinsibleTimer=40
        if Icicle.icicleList!=[]:
            for each in Icicle.icicleList:
                each.timer-=1 
                if each.timer==0:
                    Icicle.icicleList.remove(each)


class Landscape():
    landscapes=[] #creating a list of landscapes that is used to create landscape
    generated={0,1,2}
    timer=0
    def __init__(self,parameter,lType):
        self.parameter=parameter
        self.destructable=False
        self.lType=lType
        Landscape.landscapes.append(self)
    @classmethod
    def timerFired(cls,app):
        #Landscape.timer+=1

        if Game.phase=="practice": #and Landscape.timer>=5:
            Landscape.generation(app)
            Landscape.timer=0
            
    @staticmethod
    def generateBump(o):
        x0=o+800
        y0=650
        x1=x0+random.randint(100,130)
        y1=700
        ground=Landscape([[x0,y0],[x1,y1]],"terrain")
        return None
    @staticmethod
    def generateLongPlateform(o,lower,upper):
        x0=o+800+random.randint(0,50)
        y0=random.randint(int(upper-50),int(upper+50))
        x1=x0+random.randint(100,120)
        y1=y0+random.randint(40,50)
        ground=Landscape([[x0,y0],[x1,y1]],"terrain")
        return None    
    @staticmethod
    def generateShortPlatform(o,lower,upper):
        x0=o+800+random.randint(0,50)
        y0=random.randint(int(upper-50),int(upper+50))
        x1=x0+random.randint(200,220)
        y1=y0+random.randint(40,50)
        ground=Landscape([[x0,y0],[x1,y1]],"terrain")
        return None
    @classmethod
    def generation(cls,app):
        if (int(miku.position[0]//300) not in Landscape.generated):
            Landscape.generated.add(int(miku.position[0]//300))
            o=miku.position[0]
            ground=Landscape([[0,700],[o+1600,900]],"ground")
            for i in range(7,2,-2):
                if i == 7:
                    num=random.randint(0,3)
                    if num==3:
                        Landscape.generateBump(o)
                else:
                    lower=(i+1)*100
                    upper=(i)*100 
                    c=random.randint(0,1)
                    num=random.randint(0,10)
                    if isOdd(num):
                        if c==0:
                            Landscape.generateLongPlateform(o,lower,upper)
                        elif c==1:
                            Landscape.generateShortPlatform(o,lower,upper)
                    if not isOdd(num):
                        return

           
            

#wall1=Landscape([[1700,0],[1900,900]])

class Enemy():
    enemyList=list()
    def __init__(self,parameter,hitBoxType,health,position):
        self.parameter=parameter 
        self.invinsible=False
        self.hitBoxType=hitBoxType
        self.health=health
        Enemy.enemyList.append(self)
        self.position=position
        self.timer=0
    @classmethod
    def timerFired(cls,app):
        if Enemy.enemyList!=[]:
            for each in Enemy.enemyList:
                each.parameter[0][0]-=10
                each.parameter[1][0]-=10
                if each.parameter[1][0]<=0:
                     each.parameter[0][0]=app.width
                     each.parameter[1][0]=app.width+60        


class MiniDai(Enemy):
    miniDai= list()
    practiceTimer=0
    def __init__(self,position):
        self.position=position
        self.jumpTimer=0
        self.health=90
        self.inAir=True
        self.jumpCount=1
        self.resistence=0
        self.attackTimer=0
        MiniDai.miniDai.append(self)
        Enemy.enemyList.append(self)
    @property 
    def parameter(self):
        return [[self.position[0]-27,self.position[1]-44],
        [self.position[0]+27,self.position[1]+44]]
    @property
    def hitBox(self):
        return [[self.position[0]-27,self.position[1]-44],
        [self.position[0]+27,self.position[1]-44],
        [self.position[0]-27,self.position[1]+44],
        [self.position[0]+27,self.position[1]+44],
        [self.position[0]-27,self.position[1]],
        [self.position[0]+27,self.position[1]],
        [self.position[0],self.position[1]]]
    @property
    def lAhitBox(self):
        return [[self.position[0]-60,self.position[1]-44],
        [self.position[0]+27,self.position[1]-44],
        [self.position[0]-60,self.position[1]+44],
        [self.position[0]+27,self.position[1]+44],
        [self.position[0]-60,self.position[1]],
        [self.position[0]+27,self.position[1]],
        [self.position[0],self.position[1]]]
    @property   
    def rAhitBox(self):
        return [[self.position[0]-27,self.position[1]-44],
        [self.position[0]+60,self.position[1]-44],
        [self.position[0]-27,self.position[1]+44],
        [self.position[0]+60,self.position[1]+44],
        [self.position[0]-27,self.position[1]],
        [self.position[0]+60,self.position[1]],
        [self.position[0],self.position[1]]]
    @classmethod
    def hit(cls):
        x0=miku.position[0]-27 
        y0=miku.position[1]-44
        x1=miku.position[0]+27 
        y1=miku.position[1]+44
        if MiniDai.miniDai!=[]:
            for each in MiniDai.miniDai:
                for point in each.hitBox:
                    if x0<=point[0]<=x1 and y0<=point[1]<=y1 and miku.invinsible==False:
                        return True
    def Lhit(self):
        x0=miku.position[0]-27 
        y0=miku.position[1]-44
        x1=miku.position[0]+27 
        y1=miku.position[1]+44
        for point in self.lAhitBox:
            if x0<=point[0]<=x1 and y0<=point[1]<=y1 and miku.invinsible==False:
                return True     
    def Rhit(self):
        x0=miku.position[0]-27 
        y0=miku.position[1]-44
        x1=miku.position[0]+27 
        y1=miku.position[1]+44
        for point in self.lAhitBox:
            if x0<=point[0]<=x1 and y0<=point[1]<=y1 and miku.invinsible==False:
                return True  
    def jump(self):
        self.jumpTimer=1000
        self.inAir=True 
        self.jumpCount=0
        return None
    def collisionLeft(self):
        cy=self.position[1]
        cx=self.position[0]
        point0=[cx-27,cy-44]
        point1=[cx-27,cy]
        point2=[cx-27,cy+44]
        L=[point0,point1]
        for block in Landscape.landscapes:
            if contactWallLeft(L,block):
                return True
        return False
    def collisionRight(self):
        cy=self.position[1]
        cx=self.position[0]
        point0=[cx+27,cy-44]
        point1=[cx+27,cy]
        point2=[cx+27,cy+44]
        L=[point0,point1]
        for block in Landscape.landscapes:
            if contactWallLeft(L,block):
                return True
        return False
    def collisionCeiling(self):
        cy=self.position[1]
        cx=self.position[0]
        point0=[cx+15,cy-46]
        point1=[cx,cy-46]
        point2=[cx-15,cy-46]
        L=[point0,point1,point2]
        for block in Landscape.landscapes:
            if contactCeiling(L,block):
                return block
        return False
    @property
    def direction(self):
        if self.position[0]<=miku.position[0]:
            return "right"
        elif self.position[0]>miku.position[0]:
            return "left"
        
    def collisionLand(self):
        cy=self.position[1]
        cx=self.position[0]
        point0=[cx-27,cy+44]
        point1=[cx,cy+44]
        point2=[cx+27,cy+44]
        L=[point0,point1,point2]
        for block in Landscape.landscapes:
            if contactGround(L,block):
                return block
        return None
    @classmethod
    def spawnPracticeDai(cls):
        o=miku.position[0]
        num=random.randint(0,1)
        if num==1:
            mini=MiniDai([o+900,300])
        elif num==0:
            mini=MiniDai([o-900,300])
    @classmethod

    def timerFired(cls,app):
        if Game.phase=="practice":
            MiniDai.practiceTimer+=1
            if MiniDai.practiceTimer==40000:
                MiniDai.spawnPracticeDai()
                MiniDai.practiceTimer=0
        
        if MiniDai.hit()==True:
            miku.health-=app.damage
            miku.invinsibleTimer=40
        if len(MiniDai.miniDai)!=0:
            for self in MiniDai.miniDai:
                if self.attackTimer>0:
                    self.attackTimer-=1
                    if self.direction=="right":
                        if self.Rhit():
                            miku.health-=app.damage
                            miku.invinsibleTimer=40

                    elif self.direction=="left":
                        if self.Lhit():
                            miku.health-=app.damage
                            miku.invinsibleTimer=40
                elif self.position[0] >= miku.position[0] +70 and self.collisionLeft()==False:
                    self.position[0]-=4 
                elif self.position[0]< miku.position[0] - 70 and self.collisionRight()==False:
                    self.position[0]+=4 
                elif miku.position[0]-70<=self.position[0] <= miku.position[0]+70 and abs(self.position[1]-miku.position[1])<=100:
                    if self.attackTimer==0:
                        self.attackTimer=12
                    
                if self.collisionLeft() or self.collisionRight():
                    if self.jumpCount>0:
                        self.jump()
                if self.jumpTimer>0:
                    if self.collisionCeiling()==False: 
                        self.position[1]-=20
                    elif self.collisionCeiling()!=False: 
                        block=self.collisionCeiling()
                        self.position[1]=block.parameter[1][1]+44
                    self.jumpTimer-=100
                elif self.jumpTimer<=0:
                    if self.inAir==True:
                        self.position[1]+=15
                    if self.collisionLand()!=None:
                        self.position[1]=self.collisionLand().parameter[0][1]-44
                        self.inAir=False
                        self.jumpTimer=0
                        self.jumpCount=1
                    if self.collisionLand()==None:
                        self.inAir=True
                if self.health<=0:
                    MiniDai.miniDai.remove(self)
                    Enemy.enemyList.remove(self)

class ParabolicProjectile():
    pProjectileList=[]
    def __init__(self,angle,xv0,yv0,initialPosition):
        self.angle=angle
        self.xv0=xv0
        self.yv0=yv0
        self.initialPosition=initialPosition
        self.r=15
        self.t=0
        ParabolicProjectile.pProjectileList.append(self)
    def hit(self):
        centerX=self.position[0]
        centerY=self.position[1]
        r=self.r
        for each in miku.hitBox:
            if (math.sqrt(abs(each[0]-centerX)**2+abs(each[1]-centerY)**2)<=r and 
                miku.invinsible==False):
                miku.invinsibleTimer=30
                return True
    @property
    def position(self):
        xv0=self.xv0
        yv0=self.yv0
        x0=self.initialPosition[0]
        y0=self.initialPosition[1]
        x=x0+xv0*self.t
        y=y0+yv0*self.t+(1/2)*g*(self.t**2)
        return [x,y]
    
    @classmethod
    def timerFired(cls,app):
        if ParabolicProjectile.pProjectileList!=[]:
            for each in ParabolicProjectile.pProjectileList:
                each.t+=1
                if each.hit():
                    miku.health-=app.damage


class Socery(Enemy):
    socery=list()
    practiceTimer=0
    def __init__(self,position):
        self.position=position
        self.jumpTimer=0
        self.health=90
        self.inAir=True
        self.jumpCount=1
        self.resistence=0
        self.attackTimer=12
        self.moveTimer=0
        self.inAir=True
        self.attackCount=2
        self.jumpTimer=0
        self.jumpCount=1
        Socery.socery.append(self)
        Enemy.enemyList.append(self)
    def jump(self):
        self.jumpTimer=1000
        self.inAir=True 
        self.jumpCount=0
        return None
    @property 
    def parameter(self):
        return [[self.position[0]-32,self.position[1]-44],
        [self.position[0]+32,self.position[1]+44]]
    @property
    def hitBox(self):
        return [[self.position[0]-27,self.position[1]-44],
        [self.position[0]+27,self.position[1]-44],
        [self.position[0]-27,self.position[1]+44],
        [self.position[0]+27,self.position[1]+44],
        [self.position[0]-27,self.position[1]],
        [self.position[0]+27,self.position[1]],
        [self.position[0],self.position[1]]]
    @property
    def direction(self):
        if self.position[0]<=miku.position[0]:
            return "right"
        elif self.position[0]>miku.position[0]:
            return "left"
    def collisionCeiling(self):
        cy=self.position[1]
        cx=self.position[0]
        point0=[cx+15,cy-46]
        point1=[cx,cy-46]
        point2=[cx-15,cy-46]
        L=[point0,point1,point2]
        for block in Landscape.landscapes:
            if contactCeiling(L,block):
                return block
        return False
    def caste(self):
        if self.direction=="left":
            x0=self.position[0]-30
            y0=self.position[1]-50
        elif self.direction=="right":
            x0=self.position[0]+30
            y0=self.position[1]-50
        xf0=miku.position[0]
        yf0=miku.position[1]
        d=abs(xf0-x0)
        k=abs(yf0-y0)*16
        angle0=math.pi/4
        angle1=math.pi/3
        #v00=(1/math.cos(angle0))*math.sqrt(((1/2)*g*abs(x0-xf0)**2)/(abs(x0-xf0)
        #*math.tan(angle0)))
        v00=math.sqrt(2*d+math.sqrt(2)+math.sqrt(2)*math.sqrt(2*math.sqrt(2)*d+4*k+1))
        if self.direction=="right" and y0-yf0<=50:
            xv0=-math.cos(angle0)*-v00*1.25
            yv0=math.sin(angle0)*-v00
        #projectile0=ParabolicProjectile(angle0,v00,[x0,y0])
            projectile1=ParabolicProjectile(angle0,xv0,yv0,[x0,y0])
        elif self.direction=="right" and y0-yf0>=50:
            v00=math.sqrt((4*d+1+math.sqrt(8*d+32*k+1))/2)
            
            xv0=-math.cos(angle1)*-v00*1.25
            yv0=math.sin(angle1)*-v00*1.5
            projectile1=ParabolicProjectile(angle0,xv0,yv0,[x0,y0])
        elif self.direction=="left"and y0-yf0<=50:
            xv0=math.cos(angle0)*-v00*1.25
            yv0=math.sin(angle0)*-v00
        #projectile0=ParabolicProjectile(angle0,v00,[x0,y0])
            projectile1=ParabolicProjectile(angle0,xv0,yv0,[x0,y0])
        elif self.direction=="left"and y0-yf0>=50:
            v00=math.sqrt((4*d+1+math.sqrt(8*d+32*k+1))/2)
            xv0=math.cos(angle1)*-v00*1.25
            yv0=math.sin(angle1)*-v00*1.5
            projectile1=ParabolicProjectile(angle0,xv0,yv0,[x0,y0])

    
    @classmethod
    def hit(cls):
        x0=miku.position[0]-27 
        y0=miku.position[1]-44
        x1=miku.position[0]+27 
        y1=miku.position[1]+44
        if Socery.socery!=[]:
            for each in Socery.socery:
                for point in each.hitBox:
                    if x0<=point[0]<=x1 and y0<=point[1]<=y1 and miku.invinsible==False:
                        return True
    
    def collisionLeft(self):
        cy=self.position[1]
        cx=self.position[0]
        point0=[cx-27,cy-44]
        point1=[cx-27,cy]
        point2=[cx-27,cy+44]
        L=[point0,point1]
        for block in Landscape.landscapes:
            if contactWallLeft(L,block):
                return True
        return False
    def collisionRight(self):
        cy=self.position[1]
        cx=self.position[0]
        point0=[cx+27,cy-44]
        point1=[cx+27,cy]
        point2=[cx+27,cy+44]
        L=[point0,point1]
        for block in Landscape.landscapes:
            if contactWallLeft(L,block):
                return True
        return False
    def collisionLand(self):
        cy=self.position[1]
        cx=self.position[0]
        point0=[cx-27,cy+44]
        point1=[cx,cy+44]
        point2=[cx+27,cy+44]
        L=[point0,point1,point2]
        for block in Landscape.landscapes:
            if contactGround(L,block):
                return block
        return None
    @classmethod
    def timerFired(cls,app):
        if Socery.hit():
            miku.health-=app.damage
            miku.invinsibleTimer=40
        if Socery.socery!=[]:
            for self in Socery.socery:
                if self.inAir==True and self.jumpTimer==0:
                    self.position[1]+=15
                if self.collisionLand()!=None:
                    self.position[1]=self.collisionLand().parameter[0][1]-44
                    self.inAir=False
                    self.jumpCount=1
                if self.collisionLand()==None:
                    self.inAir=True
                if self.attackTimer>=0:
                    if (self.attackCount>0 and self.inAir==False and 
                        abs(self.position[0]-miku.position[0])<=700) :
                        self.caste()
                        self.attackCount-=1
                    elif abs(self.position[0]-miku.position[0])>=700:
                        self.attackTimer=1
                    self.attackTimer-=1
                if self.attackTimer==0 and self.moveTimer==0:
                    self.moveTimer=24
                if self.jumpTimer>0:
                    if self.collisionCeiling()==False: 
                        self.position[1]-=20
                    elif self.collisionCeiling()!=False: 
                        block=self.collisionCeiling()
                        self.position[1]=block.parameter[1][1]+44
                    self.jumpTimer-=100
                if self.moveTimer>0:
                    self.moveTimer-=1
                    if self.position[0] >= miku.position[0] +500 and self.collisionLeft()==False:
                        self.position[0]-=4
                    elif self.position[0]< miku.position[0] -500 and self.collisionRight()==False:
                        self.position[0]+=4
                    if self.moveTimer==0:
                        self.attackTimer=12
                        self.attackCount=1
                if self.collisionLeft() or self.collisionRight():
                    if self.jumpCount>0:
                        self.jump()
                if self.attackTimer==0 and self.moveTimer<=0:
                    self.attackTimer=12
                if self.health<=0:
                    Enemy.enemyList.remove(self)
                    Socery.socery.remove(self)
 

class Drone(Enemy):
    droneList=[]
    spawnTimer=0
    def __init__(self,position):
        self.position=position
        self.health=90
        self.mode="attack"
        self.attackTimer=12
        self.moveTimer=0
        self.attackCount=2
        self.resistence=0.5
        Enemy.enemyList.append(self)
        Drone.droneList.append(self)
    @property 
    def parameter(self):
        return [[self.position[0]-50,self.position[1]-25],
        [self.position[0]+50,self.position[1]+25]]
    @property
    def hitBox(self):
        return [[self.position[0]-50,self.position[1]-25],
        [self.position[0]+50,self.position[1]-25],
        [self.position[0]-50,self.position[1]+25],
        [self.position[0]+50,self.position[1]+25],
        [self.position[0]-50,self.position[1]],
        [self.position[0]+50,self.position[1]],
        [self.position[0],self.position[1]]]
    @classmethod
    def hit(cls):
        x0=miku.position[0]-27 
        y0=miku.position[1]-44
        x1=miku.position[0]+27 
        y1=miku.position[1]+44
        if MiniDai.miniDai!=[]:
            for each in Drone.droneList:
                for point in each.hitBox:
                    if x0<=point[0]<=x1 and y0<=point[1]<=y1 and miku.invinsible==False:
                        return True
    @property
    def direction(self):
        if self.position[0]<=miku.position[0]:
            return "right"
        elif self.position[0]>miku.position[0]:
            return "left"

    def shootProjectile(self):
        if self.direction=="left":
            initPosition=[self.position[0]-50,self.position[1]+25]
            initPosition1=[self.position[0]-45,self.position[1]+20]
        elif self.direction=="right":
            initPosition=[self.position[0]+50,self.position[1]+25]
            initPosition1=[self.position[0]+45,self.position[1]+20]

        L=[miku.position[0]-initPosition[0],miku.position[1]-initPosition[1]]
        D=normalized(L)
        proj=ovalProjectile("oval",initPosition,D,10,30,"drone")
        proj=ovalProjectile("oval",initPosition1,D,10,30,"drone")
        
    def collisionLeft(self):
        cy=self.position[1]
        cx=self.position[0]
        point0=[cx-50,cy-25]
        point1=[cx-50,cy]
        point2=[cx-50,cy+25]
        L=[point0,point1,point2]
        for block in Landscape.landscapes:
            if contactWallLeft(L,block):
                return block
        return False
    def collisionRight(self):
        cy=self.position[1]
        cx=self.position[0]
        point0=[cx+50,cy-25]
        point1=[cx+50,cy]
        point2=[cx+50,cy+25]
        L=[point0,point1]
        for block in Landscape.landscapes:
            if contactWallRight(L,block):
                return block
        return False
    
    @classmethod
    def spawnPracticeDrone(cls):
        o=miku.position[0]
        drone=Drone([o+400,200])
    @classmethod
    def timerFired(cls,app):
        Drone.spawnTimer+=1
        if Drone.spawnTimer==10:
            pass
            #Drone.spawnPracticeDrone()
        if Drone.hit()==True:
            miku.health-=app.damage
            miku.invinsibleTimer=40
        if Drone.droneList!=[]:
            for drone in Drone.droneList:
                if drone.health<=0:
                    Enemy.enemyList.remove(drone)
                    Drone.droneList.remove(drone)
                if drone.attackTimer>0:
                    drone.attackTimer-=1
                    if drone.attackCount>0:
                        drone.shootProjectile()
                        drone.attackCount-=1
                if drone.attackTimer==0 and drone.moveTimer==0:
                    drone.moveTimer=60
                if drone.moveTimer>0:
                    drone.moveTimer-=1
                    if miku.position[0]+800>=drone.position[0] >= miku.position[0] and drone.collisionLeft()==False:
                        drone.position[0]+=3
                    elif miku.position[0]-800<=drone.position[0]<=miku.position[0]  and drone.collisionRight()==False:
                        drone.position[0]-=3
                    if drone.collisionLeft()!=False:
                        drone.position[0]=drone.collisionLeft().parameter[1][0]+50
                    if drone.collisionRight()!=False:
                        drone.position[0]=drone.collisionRight().parameter[0][0]-50

                if drone.attackTimer==0 and drone.moveTimer==0:
                    drone.attackTimer=12
                    drone.attackCount=2

        

class DaiBao(Enemy):
    dai=list()
    positionVector=[[1,-1],[1,1],[-1,-1],[-1,1]]
    def __init__(self):
        self.health=810
        self.phase=0
        self.hitBoxType="oval"
        self.position=[200,200]
        self.direction="right"
        self.timer=0
        self.atkTimer=0
        self.spTimer=0
        self.resistence=0.8
        self.maxHealth=810
        self.mode="attunded"
        DaiBao.dai.append(self)
        Enemy.enemyList.append(self)
    @property
    def p(self):
        if self.mode=="attuned":
            if self.health/self.maxHealth>=0.5:
                return 0
            if self.health/self.maxHealth<=0.5:
                return 1
        else:
            if self.health/self.maxHealth>=0.7:
                return 0
            if self.health/self.maxHealth<=0.7:
                return 1
    def sommonMiniDai(self): 
        miniDai=MiniDai([self.position[0],self.position[1]+100])
        return None
    def sommonSocery(self): 
        socery=Socery([self.position[0],self.position[1]+100])
        return None
    def sommonDrone(self): 
        drone=Drone([self.position[0],self.position[1]+200])
        return None
    @property
    def parameter(self):
        cx=self.position[0]
        cy=self.position[1]
        return [[cx-120,cy-50],[cx-70,cy-70],[cx+70,cy-70],[cx+120,cy-50],
            [cx+120,cy+200],[cx-120,cy+200]]
    def createProjectile(self):
        initPosition=[self.position[0],self.position[1]]
        L=[miku.position[0]-initPosition[0],miku.position[1]-initPosition[1]]
        D=normalized(L)
        proj=ovalProjectile("oval",initPosition,D,30,10,"fly")
        return None
    @classmethod
    def timerFired(cls,app):
        if DaiBao.dai!=[]:
            for daibao in DaiBao.dai:
                daibao.timer+=1
                daibao.atkTimer+=1
                daibao.spTimer+=1
                if daibao.p==0:
                    if daibao.spTimer>=200:
                        num=random.randint(0,2)
                        if num==0:
                            daibao.sommonMiniDai()
                        elif num==1:
                            daibao.sommonSocery()
                        elif num==2:
                            daibao.sommonDrone()
                        daibao.spTimer=0
                elif daibao.p==1:
                    if daibao.spTimer>=100:
                        num=random.randint(0,2)
                        if num==0:
                            daibao.sommonMiniDai()
                        elif num==1:
                            daibao.sommonSocery()
                        elif num==2:
                            daibao.sommonDrone()
                        daibao.spTimer=0
                if daibao.atkTimer==50:
                    daibao.createProjectile()
                    daibao.atkTimer=0
                if daibao.direction=="right":
                    if daibao.timer<=14:
                        daibao.position[0]+=5*DaiBao.positionVector[0][0]
                        daibao.position[1]+=5*DaiBao.positionVector[0][1]
                    elif daibao.timer<=28:
                        daibao.position[0]+=5*DaiBao.positionVector[1][0]
                        daibao.position[1]+=5*DaiBao.positionVector[1][1]
                    elif daibao.timer>28:
                        daibao.timer=0
                elif daibao.direction=="left":
                    if daibao.timer<=14:
                        daibao.position[0]+=5*DaiBao.positionVector[2][0]
                        daibao.position[1]+=5*DaiBao.positionVector[2][1]
                    elif daibao.timer<=28:
                        daibao.position[0]+=5*DaiBao.positionVector[3][0]
                        daibao.position[1]+=5*DaiBao.positionVector[3][1]
                    elif daibao.timer>28:
                        daibao.timer=0
                if daibao.parameter[0][0]>=1200:
                    daibao.direction="left"
                elif daibao.parameter[0][0]<=200:
                    daibao.direction="right"
                if daibao.health<=0:
                    DaiBao.dai.remove(daibao)
                    Enemy.enemyList.append(daibao)
                    

class Projectile():
    projectiles=[]
    def __init__(self,projectileType, parameter,vector):
        self.projectileType=projectileType
        self.parameter=parameter
        self.vector=vector
        Projectile.projectiles.append(self)
 
    def hit(self):
        return 42
    @classmethod
    def timerFired(self,app):
        if Projectile.projectiles!=[]:
            for each in Projectile.projectiles:
                each.parameter[0]+=each.speed*each.vector[0]
                each.parameter[1]+=each.speed*each.vector[1]
                if each.hit():
                    if miku.health>=1:
                        miku.health-=app.damage
                        miku.invinsibleTimer=30
                        if each in Projectile.projectiles:
                            Projectile.projectiles.remove(each)
                if each.hitLandscape():
                    if each in Projectile.projectiles:
                        Projectile.projectiles.remove(each)
       
class ovalProjectile(Projectile):
 
    def __init__(self,projectileType,parameter,vector,r,speed,name):
        #super().__init__(projectileType,parameter,vector,r)
        self.projectileType=projectileType
        self.parameter=parameter
        self.vector=vector
        self.r=r
        self.speed=speed
        self.name=name
        Projectile.projectiles.append(self)
        
    def hit(self):
        centerX=self.parameter[0]
        centerY=self.parameter[1]
        r=self.r
        for each in miku.hitBox:
            if (math.sqrt(abs(each[0]-centerX)**2+abs(each[1]-centerY)**2)<=r and 
                miku.invinsible==False):
                miku.invinsibleTimer=30
                return True

    def hitLandscape(self):
        centerX=self.parameter[0]
        centerY=self.parameter[1]
        r=self.r
        for each in Landscape.landscapes:
            if (each.parameter[0][0]<=centerX<=each.parameter[1][0] and 
                each.parameter[0][1]<=centerY<=each.parameter[1][1]):
                return True
class FN(Enemy):
    nova=[]
    def __init__(self,position):
        self.position=position
        self.inAir=True
        self.health=1000
        self.maxHealth=1000
        self.aiTimer=30
        self.resistence=1
        self.dashTimer=0
        self.dashCount=1 
        self.projectileTimer=0
        self.icicleTimer=0
        self.aoeTimer=0
        self.aoeCount=1
        self.aoePCount=1
        self.mode="attuned" 
        self.dash_direction="right"
        self.projectile_direction="right"
        self.icicleSCount=1
        self.icicleRCount=1
        self.projectileCount=1
        self.aiChoiceCount=1
        self.x=1
        FN.nova.append(self)
        Enemy.enemyList.append(self)  
    @property
    def parameter(self):
        x0=self.position[0]
        y0=self.position[1]
        return[[x0-60,y0-50],[x0-60,y0-50]]
    @property
    def phase(self):
        if self.mode=="attuned":
            if self.health/self.maxHealth>=0.5:
                return 0
            if self.health/self.maxHealth<=0.5:
                return 1
        else:
            if self.health/self.maxHealth>=0.7:
                return 0
            if self.health/self.maxHealth<=0.7:
                return 1
    @property 
    def parameter(self):
        return [[self.position[0]-50,self.position[1]-60],[self.position[0]+50,self.position[1]+60]]
    def collisionLand(self):
        cy=self.position[1]
        cx=self.position[0]
        point0=[cx-27,cy+60]
        point1=[cx,cy+60]
        point2=[cx+27,cy+60]
        L=[point0,point1,point2]
        for block in Landscape.landscapes:
            if contactGround(L,block):
                return block
        return None
    def atk_dash(self):
        self.dashTimer=13
    def atk_icicle(self):
        self.icicleTimer=40
    def atk_aoe(self):
        self.aoeTimer=55
    def atk_projectile(self):
        self.projectileTimer=40
    def gen_frostNova(self):
        pass
    def groundWork(self):
        if self.inAir==True:
            self.position[1]+=15
        if self.collisionLand()!=None:
            self.position[1]=self.collisionLand().parameter[0][1]-60
            self.inAir=False
        if self.collisionLand()==None:
            self.inAir=True
    def icicleAttackS(self,x):
       
        icicle=Icicle([x,800],"shadow")
        icicle=Icicle([x-150,800],"shadow")
        icicle=Icicle([x+150,800],"shadow")
        icicle=Icicle([x-300,800],"shadow")
        icicle=Icicle([x+300,800],"shadow")
    def icicleAttackR(self,x):
        
        icicle=Icicle([x,800],"real")
        icicle=Icicle([x-150,800],"real")
        icicle=Icicle([x+150,800],"real")
        icicle=Icicle([x-300,800],"real")
        icicle=Icicle([x+300,800],"real")
    @property
    def direction(self):
        if self.position[0]<=miku.position[0]:
            return "right"
        elif self.position[0]>miku.position[0]:
            return "left"
    @classmethod
    def timerFired(cls,app):
        if FN.nova!=[]:
            for self in FN.nova:
                self.groundWork()
                if self.aiTimer>0:
                    self.aiTimer-=1
                if self.aiTimer==0 and self.aiChoiceCount==1:
                    self.aiChoiceCount-=1
                    num=random.randint(0,3)
                    if num==0:
                        if self.direction=="left" and self.position[0]>800:
                            self.atk_dash()
                            self.dash_direction="left"
                        elif self.direction=="right" and 1440-self.position[0]>800:
                            self.atk_dash()
                            self.dash_direction="right"
                        else:
                            self.atk_projectile() 
                    elif num==1:
                        self.atk_icicle()
                    elif num==2:
                        if self.direction=="left":
                            self.projectile_direction="left"
                            self.atk_projectile()
                            
                        elif self.direction=="right":
                            self.projectile_direction="right"
                            self.atk_projectile()

                    elif num==3:
                        self.atk_aoe() 
                if self.dashTimer>0:
                    self.dashTimer-=1
                    if self.dash_direction =="left":
                        self.position[0]-=700/12
                    elif self.dash_direction=="right":
                        self.position[0]+=700/12
                    if self.dashTimer==0:
                        self.aiTimer=30
                        self.aiChoiceCount=1
                elif self.icicleTimer>0:
                    self.icicleTimer-=1
                    if self.icicleSCount>0:
                        self.x=miku.position[0]
                        self.icicleAttackS(self.x)
                        self.icicleSCount=0
                    if self.icicleTimer<=20 and self.icicleRCount>0:
                        self.icicleAttackR(self.x)
                        self.icicleRCount=0
                    if self.icicleTimer==0:
                        self.icicleRCount=1
                        self.icicleSCount=1
                        self.aiTimer=30

                        self.aiChoiceCount=1
                elif self.projectileTimer>0:
                    self.projectileTimer-=1
                    if self.projectileCount>0:
                        self.projectileCount=0
                        if self.projectile_direction=="left":
                            for i in range(12):
                                x=1*math.sin(math.pi+(math.pi*i/12))
                                y=1*math.cos(math.pi+(math.pi*i/12))
                                ini=[self.position[0]-50,self.position[1]]
                                projectile=ovalProjectile("oval",ini,[x,y],15,20,"fn")    
                        elif self.projectile_direction=="right":
                            for i in range(12):
                                x=-1*math.sin(math.pi+(math.pi*i/12))
                                y=-1*math.cos(math.pi+(math.pi*i/12))
                                ini=[self.position[0]+50,self.position[1]]
                                projectile=ovalProjectile("oval",ini,[x,y],15,20,"fn")
                    if self.projectileTimer==0:
                        self.aiTimer=30
                        self.projectileCount=1
                        self.aiChoiceCount=1
                elif self.aoeTimer>0:
                    self.aoeTimer-=1
                    if self.aoePCount>0:
                        self.aoePCount=0
                        f=Wave("oval",[self.position[0],self.position[1]],[0,0],400,0,"fnn",55)
                    #if self.aoeCount>0 and self.aoeTimer==20:
                        #self.apeCount=0
                        #f=Wave("oval",[self.position[0],self.position[1]],[0,0],400,0,20,True)
                    if self.aoeTimer==0:
                        self.aiTimer=30
                        self.aoePCount=1
                        self.apeCount=1
                        self.aiChoiceCount=1
                if self.health<=0:
                    Enemy.enemyList.remove(self)
                    FN.nova.remove(self)


class Wave(ovalProjectile):
    waveList=[]
    def __init__(self,projectileType,parameter,vector,r,speed,name,timer):
        super().__init__(projectileType,parameter,vector,r,speed,name)
        self.timer=timer
        Wave.waveList.append(self)
    @property
    def dmg(self):
        if self.timer>=20:
            return False
        else:
            return True

    def hit(self):
        centerX=self.parameter[0]
        centerY=self.parameter[1]
        r=self.r
        for each in miku.hitBox:
            if (math.sqrt(abs(each[0]-centerX)**2+abs(each[1]-centerY)**2)<=r and 
                miku.invinsible==False and self.dmg==True):
                miku.invinsibleTimer=30
                return True
    def hitLandscape(self):
        return False
    @classmethod
    def timerFired(cls,app):
        if Wave.waveList!=[]:
            for each in Wave.waveList:
                each.timer-=1
                if each.timer==0:
                    if each in Projectile.projectiles:
                        Projectile.projectiles.remove(each)
                    if each in Wave.waveList:
                        Wave.waveList.remove(each)
            

          
            
class Miku(): #this is the main class 
    def __init__(self,position):
        self.position=position
        self.jumpTimer=0
        self.doubleJumpCount=2
        self.direction=defaultdict(lambda:False)
        self.direction["right"]=True 
        self.inAir=True #加入惯性
        self.dashStatus=False
        self.dashTimer=0
        self.health=70
        self.attackTimer=0
        self.dropTimer=0
        self.initialPosition=[800,666]
        self.invinsibleTimer=0
        self.skillTimer=0
        self.rage=0
        self.maxRage=100

    @property
    def invinsible(self):
        if self.skillTimer>0:
            return True
        if self.invinsibleTimer>0:
            return True 
        elif self.invinsibleTimer<=0:
            return False
    @property
    def skill(self):
        if self.skillTimer>0:
            return True
        return False 
    @property
    def drawVector(self):
        x=self.position[0]
        y=self.position[1]
        return [x-self.initialPosition[0],y-self.initialPosition[1]]

    def hitWallLeft(self):
        cy=self.position[1]
        cx=self.position[0]
        point0=[cx-27,cy-44]
        point1=[cx-27,cy]
        point2=[cx-27,cy+44]
        L=[point0,point1]
        for block in Landscape.landscapes:
            if contactWallLeft(L,block):
                return True
        return False
    def hitWallRight(self):
        cy=self.position[1]
        cx=self.position[0]
        point0=[cx+27,cy-44]
        point1=[cx+27,cy]
        point2=[cx+27,cy+44]
        L=[point0,point1]
        for block in Landscape.landscapes:
            if contactWallLeft(L,block):
                return True
        return False
    def hitCeiling(self):
        cy=self.position[1]
        cx=self.position[0]
        point0=[cx+15,cy-46]
        point1=[cx,cy-46]
        point2=[cx-15,cy-46]
        L=[point0,point1,point2]
        for block in Landscape.landscapes:
            if contactCeiling(L,block):
                return block
        return False
    def land(self):
        cy=self.position[1]
        cx=self.position[0]
        point0=[cx-27,cy+44]
        point1=[cx,cy+44]
        point2=[cx+27,cy+44]
        L=[point0,point1,point2]
        for block in Landscape.landscapes:
            if contactGround(L,block):
                return block
        return None
    @property
    def hitBox(self):
        cx=self.position[0]
        cy=self.position[1]
        point0=(cx-27,cy-44)
        point1=(cx-10,cy-44)
        point2=(cx,cy-44)
        point3=(cx+10,cy-44)
        point4=(cx+27,cy-25)
        point5=(cx+27,cy-5)
        point6=(cx+27,cy+5)
        point7=(cx+27,cy+25)
        point8=(cx+27,cy+44)
        point9=(cx-27,cy+44)
        point10=(cx-10,cy+44)
        point11=(cx,cy+44)
        point12=(cx-10,cy+44)
        point13=(cx-27,cy+44)
        point14=(cx-27,cy-25)
        point15=(cx-27,cy-5)
        point16=(cx-27,cy+5)
        point17=(cx-27,cy+25)
        return[point0,point1,point2,point3,point4,point5,
               point6,point7,point8,point9,point10,point11
               ,point12,point13,point14,point15,point16,point17]
    
    def caste(self):
        if self.rage>30:
            self.rage-=30
            self.health-=2
            self.skillTimer=1000
            self.attackTimer=0
            

    def jump(self):
        self.jumpTimer=2000
        self.doubleJumpCount-=1
        self.inAir=True
    def dash(self):
        if self.skillTimer==0:
            self.dashTimer=1000
            self.dashStatus=True
    def slash(self):
        if self.skillTimer==0:
            if self.attackTimer==0:
                self.attackTimer=12
    def timerFired(self,app):
        if self.jumpTimer>=1500:
            if self.dashStatus==False and self.hitCeiling()==False and self.skill==False:
                cy=self.position[1]
                x=self.jumpTimer//10
                cy-=(math.e**(0.07*x))/20000
                self.position[1]=cy
            elif self.hitCeiling()!=False:
                block=self.hitCeiling()
                self.position[1]=block.parameter[1][1]+44
        elif 1100<=self.jumpTimer<1500:
            if self.dashStatus==False and self.hitCeiling()==False and self.skill==False:
                cy=self.position[1]
                x=self.jumpTimer//10
                cy-=(math.e**(0.07*x))/2000
                self.position[1]=cy
            elif self.hitCeiling()!=False:
                block=self.hitCeiling()
                self.position[1]=block.parameter[1][1]+44
        elif 1000<=self.jumpTimer<=1100:
            if self.dashStatus==False and self.hitCeiling()==False and self.skill==False:
                self.position[1]+=1
            elif self.hitCeiling()!=False:
                block=self.hitCeiling()
                self.position[1]=block.parameter[1][1]+44
        elif self.jumpTimer<1000:
            if self.dashStatus==False and self.skill==False:
                if miku.land()!=None:
                    self.position[1]=miku.land().parameter[0][1]-44
                    self.inAir=False
                    self.doubleJumpCount=2
                    self.dropTimer=0
                elif self.inAir==True:
                    self.dropTimer+=1
                    if self.dropTimer<=7:
                        self.position[1]+=self.dropTimer*3
                    elif self.dropTimer>7:
                        self.position[1]+=7*3
                elif miku.land()==None and self.inAir==False:
                    self.inAir=True
                
                '''if self.position[1]>=666.66-30:
                        self.position[1]=666.66-30
                        self.doubleJumpCount=2
                        self.inAir=False'''
        if self.jumpTimer>0: 
            self.jumpTimer-=100
        if self.skillTimer>0:
            self.skillTimer-=100  
        elif self.dashTimer>0: 
            self.dashTimer-=150
            if self.direction["left"]==True and miku.hitWallLeft()==False:
                self.position[0]-=30
            elif self.direction["right"]==True and miku.hitWallRight()==False:
                self.position[0]+=30
            if self.dashTimer<=0:
                self.dashTimer=0
                self.dashStatus=False
        elif self.attackTimer>0:
            self.attackTimer-=1
        if self.invinsibleTimer>0:
            self.invinsibleTimer-=1
        if self.health<=0:
            DaiBao.dai=[]
            MiniDai.miniDai=[]
            Projectile.projectiles=[]
            ovalProjectile.projectiles=[]
            ParabolicProjectile.pProjectileList=[]
            Socery.socery=[]
            Drone.droneList=[]
            FN.nova=[]
            self.rage=0
            Game.end()
        if self.health>0 and len(DaiBao.dai)==0 and Game.phase==1:
            DaiBao.dai=[]
            MiniDai.miniDai=[]
            Projectile.projectiles=[]
            ovalProjectile.projectiles=[]
            ParabolicProjectile.pProjectileList=[]
            Socery.socery=[]
            Drone.droneList=[]
            FN.nova=[]
            self.rage=0
            Game.win()
        if self.health>0 and len(FN.nova)==0 and Game.phase=="FN":
            DaiBao.dai=[]
            MiniDai.miniDai=[]
            Projectile.projectiles=[]
            ovalProjectile.projectiles=[]
            ParabolicProjectile.pProjectileList=[]
            Socery.socery=[]
            Drone.droneList=[]
            FN.nova=[]
            self.rage=0
            Game.win()
            #if attack.hit()==True and self.
       
class Attack(Miku):
    def __init__(self):
        self.attacked=[]
        return
    @property
    def skill(self):
        if miku.skill==True:
            return True 
        return False 
    @property
    def position(self):
        return miku.position
    def hit(self,target): #the logic is that
        for i in range(0,len(self.parameter),2):
            x=self.parameter[i]
            y=self.parameter[i+1]
            positiveCountX=0
            negativeCountX=0
            positiveCountY=0
            negativeCountY=0
            for each in target.parameter: 
                targetX=each[0]
                targetY=each[1]
                if x<=targetX:
                    negativeCountX+=1 
                elif x>targetX:
                    positiveCountX+=1 
                if y<=targetY:
                    negativeCountY+=1 
                elif y>targetY:
                    positiveCountY+=1
            if(positiveCountX>0 and negativeCountX>0 and positiveCountY>0
            and negativeCountY>0 and miku.skillTimer>0):
                return True

            elif(positiveCountX>0 and negativeCountX>0 and positiveCountY>0
            and negativeCountY>0 and miku.attackTimer>0):
                return True
        return False

    @property
    def parameter(self):
        cx=self.position[0]
        cy=self.position[1]
        if self.skill==True:
            point0=[cx+100,cy-20]
            point1=[cx+100,cy-60]
            point2=[cx+100,cy-100]
            point3=[cx+100,cy-140]
            point4=[cx+100,cy-180]
            point5=[cx+75,cy-200]
            point6=[cx+50,cy-210]
            point7=[cx+30,cy-220]
            point8=[cx-30,cy-220]
            point9=[cx-50,cy-210]
            point10=[cx-75,cy-200]
            point11=[cx-100,cy-180]
            point12=[cx-100,cy-140]
            point13=[cx-100,cy-100]
            point14=[cx-100,cy-60]
            point15=[cx-100,cy-20]
            point16=[cx,cy]
            point17=[cx,cy+30]
            point18=[cx,cy+50]
            point19=[cx,cy-100]
            point20=[cx,cy-50]
            point21=[cx,cy-100]
            point22=[cx,cy-70]
            point23=[cx,cy-120]
            point24=[cx+100,cy]
            point25=[cx+100,cy+20]
            point26=[cx+100,cy+60]
            point27=[cx+100,cy+120]
            point28=[cx+75,cy+120]
            point29=[cx+50,cy+60]
            point30=[cx+50,cy+60]
            point31=[cx+75,cy+120]
            point32=[cx-75,cy+120]
            point33=[cx-100,cy-60]
            point34=[cx-100,cy-20]
            point35=[cx-30,cy-20]

            return [point0[0],point0[1],
                        point1[0],point1[1],
                        point2[0],point2[1],
                        point3[0],point3[1],
                        point4[0],point4[1],
                        point5[0],point5[1],
                        point6[0],point6[1],
                        point7[0],point7[1],
                        point8[0],point8[1],
                        point9[0],point9[1],
                        point10[0],point10[1],
                        point11[0],point11[1],
                        point12[0],point12[1],
                        point13[0],point13[1],
                        point14[0],point14[1],
                        point15[0],point15[1],
                        point16[0],point16[1],
                        point17[0],point17[1],
                        point18[0],point18[1],
                        point19[0],point19[1],
                        point20[0],point20[1],
                point21[0],point21[1],
                point22[0],point22[1],
                point23[0],point23[1],
                point24[0],point24[1],
                point25[0],point25[1],
                point26[0],point26[1],
                point27[0],point27[1],
                point28[0],point28[1],
                point29[0],point29[1],
                point30[0],point30[1],
                point31[0],point31[1],
                point32[0],point32[1],
                point33[0],point33[1],
                point34[0],point34[1],
                point35[0],point35[1],
                        ]
            
        elif miku.direction["up"]==True:
            point0=[cx+50,cy-20]
            point1=[cx+50,cy-60]
            point2=[cx+50,cy-100]
            point3=[cx+50,cy-140]
            point4=[cx+50,cy-180]
            point5=[cx+45,cy-200]
            point6=[cx+30,cy-210]
            point7=[cx+15,cy-220]
            point8=[cx-14,cy-220]
            point9=[cx-30,cy-210]
            point10=[cx-45,cy-200]
            point11=[cx-50,cy-180]
            point12=[cx-50,cy-140]
            point13=[cx-50,cy-100]
            point14=[cx-50,cy-60]
            point15=[cx-50,cy-20]
            point16=[cx,cy]
            point17=[cx,cy+30]
            point18=[cx,cy+50]
            point19=[cx,cy-100]
            point20=[cx,cy-50]
            point21=[cx,cy-100]
            point22=[cx,cy-70]
            point23=[cx,cy-120]
        elif miku.direction["down"]==True:
            point0=[cx+50,cy+20]
            point1=[cx+50,cy+60]
            point2=[cx+50,cy+100]
            point3=[cx+50,cy+140]
            point4=[cx+50,cy+180]
            point5=[cx+45,cy+200]
            point6=[cx+30,cy+210]
            point7=[cx+15,cy+220]
            point8=[cx-14,cy+220]
            point9=[cx-30,cy+210]
            point10=[cx-45,cy+200]
            point11=[cx-50,cy+180]
            point12=[cx-50,cy+140]
            point13=[cx-50,cy+100]
            point14=[cx-50,cy+60]
            point15=[cx-50,cy+20]
            point16=[cx,cy]
            point17=[cx,cy+50]
            point18=[cx,cy+100]
            point19=[cx,cy-50]
            point20=[cx,cy-30]
            point21=[cx,cy+100]
            point22=[cx,cy+70]
            point23=[cx,cy+120]
        elif miku.direction["right"]==True:
            point0=[cx+20,cy+50]
            point1=[cx+60,cy+50]
            point2=[cx+100,cy+50]
            point3=[cx+140,cy+50]
            point4=[cx+180,cy+50]
            point5=[cx+200,cy+45]
            point6=[cx+210,cy+30]
            point7=[cx+220,cy+15]
            point8=[cx+220,cy-14]
            point9=[cx+210,cy-30]
            point10=[cx+200,cy-45]
            point11=[cx+180,cy-50]
            point12=[cx+140,cy-50]
            point13=[cx+100,cy-50]
            point14=[cx+60,cy-50]
            point15=[cx+20,cy-50]
            point16=[cx,cy]
            point17=[cx+50,cy]
            point18=[cx+100,cy]
            point19=[cx-50,cy]
            point20=[cx-30,cy]
            point21=[cx+100,cy]
            point22=[cx+70,cy]
            point23=[cx+120,cy]  
        elif miku.direction["left"]==True:
            point0=[cx-20,cy+50]
            point1=[cx-60,cy+50]
            point2=[cx-100,cy+50]
            point3=[cx-140,cy+50]
            point4=[cx-180,cy+50]
            point5=[cx-200,cy+45]
            point6=[cx-210,cy+30]
            point7=[cx-220,cy+15]
            point8=[cx-220,cy-14]
            point9=[cx-210,cy-30]
            point10=[cx-200,cy-45]
            point11=[cx-180,cy-50]
            point12=[cx-140,cy-50]
            point13=[cx-100,cy-50]
            point14=[cx-60,cy-50]
            point15=[cx-20,cy-50]
            point16=[cx,cy]
            point17=[cx+30,cy]
            point18=[cx+50,cy]
            point19=[cx-100,cy]
            point20=[cx-50,cy]
            point21=[cx-100,cy]
            point22=[cx-70,cy]
            point23=[cx-120,cy]
            

        return [point0[0],point0[1],
                        point1[0],point1[1],
                        point2[0],point2[1],
                        point3[0],point3[1],
                        point4[0],point4[1],
                        point5[0],point5[1],
                        point6[0],point6[1],
                        point7[0],point7[1],
                        point8[0],point8[1],
                        point9[0],point9[1],
                        point10[0],point10[1],
                        point11[0],point11[1],
                        point12[0],point12[1],
                        point13[0],point13[1],
                        point14[0],point14[1],
                        point15[0],point15[1],
                        point16[0],point16[1],
                        point17[0],point17[1],
                        point18[0],point18[1],
                        point19[0],point19[1],
                        point20[0],point20[1],
                point21[0],point21[1],
                point22[0],point22[1],
                point23[0],point23[1],
                        ]
    def timerFired(self,app):
        if ((Enemy.enemyList!=[] and miku.attackTimer>0) or
        (Enemy.enemyList!=[] and miku.skillTimer>0)):
            for each in Enemy.enemyList:
                if attack.hit(each) and each not in self.attacked:
                    if attack.skill==False:
                        each.health-=50
                        if miku.rage<100:
                            miku.rage+=10

                    elif attack.skill==True:
                        each.health-=200
                    self.attacked.append(each)
                    if miku.direction["down"]==[True]:
                        miku.doubleJumpCount=2
                    elif miku.direction["up"]==True:
                        each.position[1]-=30*(1-each.resistence)
                    elif miku.direction["left"]==True:
                        each.position[0]-=30*(1-each.resistence)
                    elif miku.direction["right"]==True:
                        each.position[0]+=30*(1-each.resistence)     
        if miku.attackTimer==0 and miku.skillTimer==0:
            self.attacked=[]

                
attack=Attack()
class KeyPress():
    keyPressed=defaultdict(lambda:False)
    #this is the class in which you keep track of all the key 
    def __init__(self):
        pass
############################################




def appStarted(app):
    app.timerDelay=25
    app.timer=0
    app.pTimer=0
    app.damage=1
    app.practiceTimer=0
    app.highQaulityMod=False 
    app.dashImage_left=loadAnimatedGif('42_dash_left.gif')
    app.dashCount_left=0
    app.dashImage_right=loadAnimatedGif('42_dash_right.gif')
    app.dashCount_right=0
    app.walkImage_left=loadAnimatedGif('42_walk_left.gif')
    app.walkCount_left=0
    app.walkImage_right=loadAnimatedGif('42_walk_right.gif')
    app.walkCount_right=0
    app.standImage_left=loadAnimatedGif('42_stand_left.gif')
    app.standCount_left=0
    app.standImage_right=loadAnimatedGif('42_stand_right.gif')
    app.standCount_right=0
    app.jumpImage_left=loadAnimatedGif('42_jump_left.gif')
    app.jumpCount_left=0
    app.jumpImage_right=loadAnimatedGif('42_jump_right.gif')
    app.jumpCount_right=0
    app.jumpAnimationImage=loadAnimatedGif('42_jump_animation.gif')
    app.jumpAnimationCount=0
    app.slashImage_left=loadAnimatedGif('42_slash_left.gif')
    app.slashCount_left=0
    app.slashImage_right=loadAnimatedGif('42_slash_right.gif')
    app.slashCount_right=0
    app.slashImage_up=loadAnimatedGif('42_slash_up.gif')
    app.slashCount_up=0
    app.slashImage_down=loadAnimatedGif('42_slash_down.gif')
    app.slashCount_down=0
    app.attackImage_left=loadAnimatedGif('42_attack_left.gif')
    app.attackCount_left=0
    app.attackImage_right=loadAnimatedGif('42_attack_right.gif')
    app.attackCount_right=0
    app.attackImage_down=loadAnimatedGif('42_attack_down.gif')
    app.attackCount_down=0
    app.attackImage_up=loadAnimatedGif('42_attack_up.gif')
    app.attackCount_up=0
    app.kunkunL=loadAnimatedGif('kunkunL.gif')
    app.kunkunLCount=0
    app.kunkunR=loadAnimatedGif('kunkunR.gif')
    app.kunkunRCount=0
    app.pawnL=loadAnimatedGif('pawnL.gif')
    app.pawnLCount=0
    app.pawnR=loadAnimatedGif('pawnR.gif')
    app.pawnRCount=0
    app.pawnAL=loadAnimatedGif('pawnAL.gif')
    app.pawnALCount=0
    app.pawnAR=loadAnimatedGif('pawnAR.gif')
    app.pawnARCount=0
    app.droneL=loadAnimatedGif('droneL.gif')
    app.droneLCount=0
    app.droneR=loadAnimatedGif('droneR.gif')
    app.droneRCount=0
    app.droneAL=loadAnimatedGif('droneAL.gif')
    app.droneALCount=0
    app.droneAR=loadAnimatedGif('droneAR.gif')
    app.droneARCount=0
    app.soceryL=loadAnimatedGif("soceryL.gif")
    app.soceryLCount=0
    app.soceryR=loadAnimatedGif('soceryR.gif')
    app.soceryRCount=0
    app.soceryAL=loadAnimatedGif('soceryAL.gif')
    app.soceryALCount=0
    app.soceryAR=loadAnimatedGif('soceryAR.gif')
    app.soceryARCount=0
    app.soceryIL=loadAnimatedGif('soceryIL.gif')
    app.soceryILCount=0
    app.soceryIR=loadAnimatedGif('soceryIR.gif')
    app.soceryIRCount=0
    app.aoeL=loadAnimatedGif("aoeL.gif")
    app.aoeLCount=0
    app.aoeR=loadAnimatedGif('aoeR.gif')
    app.aoeRCount=0
    app.atkL=loadAnimatedGif("atkL.gif")
    app.atkLCount=0
    app.atkR=loadAnimatedGif('atkR.gif')
    app.atkRCount=0
    app.icicleL=loadAnimatedGif("icicleL.gif")
    app.icicleLCount=0
    app.icicleR=loadAnimatedGif('icicleR.gif')
    app.icicleRCount=0
    app.idleL=loadAnimatedGif("idleL.gif")
    app.idleLCount=0
    app.idleR=loadAnimatedGif('idleR.gif')
    app.idleRCount=0
    app.roar=loadAnimatedGif('roar.gif')
    app.roarCount=0
    app.iceP=app.loadImage("iceP.png")
    app.iceS=app.loadImage("iceS.png")
    app.iceS_shadow=app.loadImage("iceS_shadow.png")
    app.ring=app.loadImage("ring.png")
    app.ring_exp=app.loadImage("ring_exp.png")
    app.flyP=app.loadImage("flyP.png")
    app.fP=app.loadImage("fP.png")
    app.pawn=app.loadImage("pawn.png")
    app.pawn=app.scaleImage(app.pawn,2/5)
    app.image0 = app.loadImage('42.jpeg')
    app.image0 = app.scaleImage(app.image0, 3/5)
    app.background=app.loadImage('back.jpeg')
    app.background = app.scaleImage(app.background, 7.5/6)
    app.losing=app.loadImage('cai.png')
    app.losing =app.scaleImage(app.losing, 7.5/6)
    app.ma=app.loadImage('ma.png')
    app.ma=app.scaleImage(app.ma,1)
    app.health=app.loadImage("health.png")
    app.bullet=app.loadImage("bullet.png")
    app.readme=app.loadImage("readme.png")
    app.readme=app.scaleImage(app.readme,1/2)
    app.icecream=app.loadImage("icecream.png")
    

def getCachedPhotoImage(app,image):
    if ('cachedPhotoImage' not in image.__dict__):
        image.cachedPhotoImage = ImageTk.PhotoImage(image)
    return image.cachedPhotoImage 

def loadAnimatedGif(path):
    dashImage = [PhotoImage(file=path, format='gif -index 0')]
    i = 1
    while True:
        try:
            dashImage.append(PhotoImage(file=path,
                                                format=f'gif -index {i}'))
            i += 1
        except Exception as e:
            return dashImage


def alternativeKeyPressed(app): 
    if KeyPress.keyPressed['s']==True:
        print("s")
        miku.direction["down"]=True 
        miku.direction["up"]=False 
        if KeyPress.keyPressed['a']==True:
            cx=miku.position[0]
            
            miku.direction["left"]=True
            miku.direction["right"]=False
            if miku.hitWallLeft()==False:
                cx-=7
            miku.position[0]=cx
        elif KeyPress.keyPressed['d']==True:
            miku.direction["right"]=True 
            miku.direction["left"]=False
            cx=miku.position[0]
            if miku.hitWallRight()==False:
                cx+=7
            miku.position[0]=cx

    #short-circut eval so that you can always do down-slash!
    elif KeyPress.keyPressed['w']==True: 
        miku.direction["up"]=True 
        miku.direction["down"]=False 
        if KeyPress.keyPressed['a']==True:
            cx=miku.position[0]
            miku.direction["left"]=True
            miku.direction["right"]=False
            if miku.hitWallLeft()==False:
                cx-=7
            miku.position[0]=cx
        elif KeyPress.keyPressed['d']==True: 
            cx=miku.position[0]
            miku.direction["right"]=True 
            miku.direction["left"]=False
            if miku.hitWallRight()==False:
                cx+=7
            miku.position[0]=cx
    elif KeyPress.keyPressed["a"]==True:
        cx=miku.position[0]
        miku.direction["left"]=True
        miku.direction["right"]=False
        if miku.hitWallLeft()==False:
                cx-=7
        miku.position[0]=cx
        
    elif KeyPress.keyPressed['d']==True:
        
        cx=miku.position[0]
        miku.direction["right"]=True 
        miku.direction["left"]=False
        if miku.hitWallRight()==False:
                cx+=7
        miku.position[0]=cx
    if KeyPress.keyPressed["s"]==False and KeyPress.keyPressed["w"]==False:
        miku.direction['up']=False
        miku.direction['down']=False
    
miku=Miku([400,666]) 
def keyPressed(app,event):
    KeyPress.keyPressed[event.key]=True
    if event.key=="Space":
        if miku.doubleJumpCount>0:
            miku.jump()
    if event.key=="k":
       
        if miku.rage>=30:
            miku.caste()
    if event.key=="e":
        miku.dash()
    if event.key=="j":
        miku.slash()
    
def mousePressed(app,event):
    if Game.phase==0:
        Button.mousePressed(app,event)  
    elif Game.phase==2:
        Game.phase=0
        DaiBao.dai=[]
        MiniDai.enemyList=[]
        miku.health=9
    elif Game.phase==1 and Game.w==True:
        Game.phase=0
        DaiBao.dai=[]
        miku.health=9
        MiniDai.enemyList=[]
        Game.w=False
    elif Game.phase=="FN" and Game.w==True:
        Game.phase=0
        DaiBao.dai=[]
        miku.health=9
        MiniDai.enemyList=[]
        Game.w=False
    elif Game.phase=="practice" or Game.phase=="help":
        Game.phase=0
        DaiBao.dai=[]
        miku.health=9
        MiniDai.enemyList=[]
        Game.w=False




def keyReleased(app,event):
    KeyPress.keyPressed[event.key]=False    
def timerFired(app):
    if Game.phase==0:
        Button.timerFired(app)
    if Game.phase=="practice":
        app.practiceTimer+=1
        if app.practiceTimer==100:
            app.practiceTimer=0
            num=random.randint(0,2)
            if num==0:
                mini=MiniDai([miku.position[0]+900,700])
            elif num==1:
                mini=Socery([miku.position[0]+900,700])
            elif num==2:
                mini=Drone([miku.position[0]+900,200])
            
    if Game.phase==4 or Game.phase==1 or Game.phase=="practice" or Game.phase=="FN":
        alternativeKeyPressed(app)
        app.dashCount_left = (1 + app.dashCount_left) % len(app.dashImage_left)
        app.dashCount_right = (1 + app.dashCount_right) % len(app.dashImage_right)
        #app.attackCount_right = (1 + app.attackCount_right) % len(app.attackImage_right)
        #app.attackCount_left = (1 + app.attackCount_left) % len(app.attackImage_left)
        app.slashCount_right = (1 + app.slashCount_right) % len(app.slashImage_right)
        app.slashCount_left = (1 + app.slashCount_left) % len(app.slashImage_left)
        app.slashCount_up = (1 + app.slashCount_up) % len(app.slashImage_up)
        app.slashCount_down = (1 + app.slashCount_down) % len(app.slashImage_down)
        app.roarCount= (1 + app.roarCount) % len(app.roar)
        app.pawnLCount=(1 + app.pawnLCount) % len(app.pawnL)
        app.pawnRCount=(1 + app.pawnRCount) % len(app.pawnR)
        app.pawnALCount=(1 + app.pawnALCount) % len(app.pawnAL)
        app.pawnARCount=(1 + app.pawnARCount) % len(app.pawnAR)
        app.droneLCount=(1 + app.droneLCount) % len(app.droneL)
        app.droneRCount=(1 + app.droneRCount) % len(app.droneR)
        app.droneALCount=(1 + app.droneALCount) % len(app.droneAL)
        app.droneARCount=(1 + app.droneARCount) % len(app.droneAR)
        app.soceryLCount=(1 + app.soceryLCount) % len(app.soceryL)
        app.soceryRCount=(1 + app.soceryRCount) % len(app.soceryR)
        app.soceryALCount=(1 + app.soceryALCount) % len(app.soceryAL)
        app.soceryARCount=(1 + app.soceryARCount) % len(app.soceryAR)
        app.soceryILCount=(1 + app.soceryILCount) % len(app.soceryIL)
        app.soceryIRCount=(1 + app.soceryIRCount) % len(app.soceryIR)
        app.idleLCount=(1 + app.idleLCount) % len(app.idleL)
        app.idleRCount=(1 + app.idleRCount) % len(app.idleR)
        app.icicleLCount=(1 + app.icicleLCount) % len(app.icicleL)
        app.icicleRCount=(1 + app.icicleRCount) % len(app.icicleR)
        app.atkLCount=(1 + app.atkLCount) % len(app.atkL)
        app.atkRCount=(1 + app.atkRCount) % len(app.atkR)
        app.aoeLCount=(1 + app.aoeLCount) % len(app.aoeL)
        app.aoeRCount=(1 + app.aoeRCount) % len(app.aoeR)
        
        

        app.timer+=1
        if app.timer>2:
            app.walkCount_right = (1 + app.walkCount_right) % len(app.walkImage_right)
            app.walkCount_left = (1 + app.walkCount_left) % len(app.walkImage_left)
            app.standCount_right = (1 + app.standCount_right) % len(app.standImage_right)
            app.standCount_left = (1 + app.standCount_left) % len(app.standImage_left)
            app.jumpCount_right = (1 + app.jumpCount_right) % len(app.jumpImage_right)
            app.jumpCount_left = (1 + app.jumpCount_left) % len(app.jumpImage_left)
            #app.slashCount_right = (1 + app.slashCount_right) % len(app.slashImage_right)
            #app.slashCount_left = (1 + app.slashCount_left) % len(app.slashImage_left)
            app.attackCount_right = (1 + app.attackCount_right) % len(app.attackImage_right)
            app.attackCount_left = (1 + app.attackCount_left) % len(app.attackImage_left)
            app.attackCount_up = (1 + app.attackCount_up) % len(app.attackImage_up)
            app.attackCount_down = (1 + app.attackCount_down) % len(app.attackImage_down)
            app.jumpAnimationCount = (1 + app.jumpAnimationCount) % len(app.jumpAnimationImage)
            app.kunkunLCount=(1 + app.kunkunLCount) % len(app.kunkunL)
            app.kunkunRCount=(1 + app.kunkunRCount) % len(app.kunkunR)
            
            


            app.timer=0
        miku.timerFired(app)
        DaiBao.timerFired(app)
        #Enemy.timerFired(app)
        attack.timerFired(app)
        Projectile.timerFired(app)
        MiniDai.timerFired(app)
        Landscape.timerFired(app)
        Drone.timerFired(app)
        Socery.timerFired(app)
        ParabolicProjectile.timerFired(app)
        Icicle.timerFired(app)
        Wave.timerFired(app)
        FN.timerFired(app)
         
    
def drawWave(app,canvas):
    x=miku.drawVector[0]
    y=miku.drawVector[1]
    if Wave.waveList!=[]:
        for each in Wave.waveList:
            r=each.r
            cx=each.parameter[0]-x
            cy=each.parameter[1]-y
            if each.dmg==False:
                if Game.complexBossAnimation==False:
                    canvas.create_oval(cx-r,cy-r,cx+r,cy+r,fill="",outline="cyan")
                elif Game.complexBossAnimation==True:
                    image=getCachedPhotoImage(app,app.ring)
                    canvas.create_image(cx,cy,image=image)
                
            elif each.dmg==True:
                if Game.complexBossAnimation==False:
                    canvas.create_oval(cx-r,cy-r,cx+r,cy+r,fill="cyan")
                elif Game.complexBossAnimation==True:
                    image=getCachedPhotoImage(app,app.ring_exp)
                    canvas.create_image(cx,cy,image=image)

def drawMiku(app,canvas):
    cx,cy=miku.initialPosition
    
    if miku.dashStatus==True:
        if miku.direction["left"]==True:
            photoImage = app.dashImage_left[app.dashCount_left]
            canvas.create_image(cx,cy,image=photoImage)
        elif miku.direction["right"]==True:
            photoImage = app.dashImage_right[app.dashCount_right]
            canvas.create_image(cx,cy,image=photoImage)
    elif miku.attackTimer>0:
        if miku.direction["down"]==True:
            photoImage = app.attackImage_down[app.attackCount_down]
            canvas.create_image(cx,cy,image=photoImage)
        elif miku.direction["up"]==True:
            photoImage = app.attackImage_up[app.attackCount_up]
            canvas.create_image(cx,cy,image=photoImage)
        elif miku.direction["left"]==True:
            photoImage = app.attackImage_left[app.attackCount_left]
            canvas.create_image(cx,cy,image=photoImage)
        elif miku.direction["right"]==True:
            photoImage = app.attackImage_right[app.attackCount_right]
            canvas.create_image(cx,cy,image=photoImage)
    elif miku.inAir==True:
        if miku.direction["left"]==True:
            photoImage = app.jumpImage_left[app.jumpCount_left]
            canvas.create_image(cx,cy,image=photoImage)
        elif miku.direction["right"]==True:
            photoImage = app.jumpImage_right[app.jumpCount_right]
            canvas.create_image(cx,cy,image=photoImage)
        if miku.jumpTimer>1500 and miku.doubleJumpCount==0:
             photoImage = app.jumpAnimationImage[app.jumpAnimationCount]
             cy0=cy+60
             canvas.create_image(cx,cy0,image=photoImage)
            

    elif (miku.direction["left"]==True and KeyPress.keyPressed['d']==False 
            and KeyPress.keyPressed['a']==False):
            photoImage = app.standImage_left[app.standCount_left]
            canvas.create_image(cx,cy,image=photoImage)
        
    elif (miku.direction["right"]==True and KeyPress.keyPressed['d']==False 
            and KeyPress.keyPressed['a']==False):
            photoImage = app.standImage_right[app.standCount_right]
            canvas.create_image(cx,cy,image=photoImage)
            pass

    elif miku.direction["left"]==True:
        photoImage = app.walkImage_left[app.walkCount_left]
        canvas.create_image(cx,cy,image=photoImage)
    elif miku.direction["right"]==True:
        photoImage = app.walkImage_right[app.walkCount_right]
        canvas.create_image(cx,cy,image=photoImage)

    else:
        canvas.create_rectangle(cx-20,cy-30,cx+20,cy+30,fill="cyan")
        canvas.create_text(cx,cy,tex=f"{miku.direction}",font="Arial 12")

    #canvas.create_rectangle(cx-27,cy-44,cx+27,cy+44,fill="red")
def drawGround(app,canvas):
    
    canvas.create_rectangle(0,5*app.height/6,app.width,app.height,fill="gray")

def drawEnemy(app,canvas):
    x=miku.drawVector[0]
    y=miku.drawVector[1]
    for each in Enemy.enemyList:
        parameter=each.parameter
        if each.hitBoxType=="oval":
            c0=parameter[0][0]-x
            c1=parameter[0][1]-y
            c2=parameter[1][0]-x
            c3=parameter[1][1]-y
            canvas.create_oval(c0,c1,c2,c3,fill="brown",outline="black")
            canvas.create_text(c0+(c2-c0)/2,c1+(c3-c1)/2,text=f"{each.health}"
            ,font="Arial 14")
         

def drawProjectile(app,canvas):
    vx=miku.drawVector[0]
    vy=miku.drawVector[1]
    if Projectile.projectiles!=[]:
        for each in Projectile.projectiles:
            if not isinstance(each,Wave):
                r=each.r
                x=each.parameter[0]-vx
                y=each.parameter[1]-vy
                if each.name==None:
                    canvas.create_oval(x-r,y-r,x+r,y+r,fill="orange")
                if each.name=="fn":
                    image=getCachedPhotoImage(app,app.iceP)
                    canvas.create_image(x,y,image=image)
                elif each.name=="fly":
                    image=getCachedPhotoImage(app,app.flyP)
                    canvas.create_image(x,y,image=image)
                elif each.name=="drone":
                     image=getCachedPhotoImage(app,app.bullet)
                     canvas.create_image(x,y,image=image)


                    #canvas.create_oval(x-r,y-r,x+r,y+r,fill="orange")

def drawLandscape(app,canvas):
    x=miku.drawVector[0]
    y=miku.drawVector[1]
    for block in Landscape.landscapes:
        x0=block.parameter[0][0]-x
        y0=block.parameter[0][1]-y
        x1=block.parameter[1][0]-x
        y1=block.parameter[1][1]-y
        canvas.create_rectangle(x0,y0,x1,y1,fill="gray")
def drawMiniDai(app,canvas):
    x=miku.drawVector[0]
    y=miku.drawVector[1]
    if MiniDai.miniDai!=[]:
        for each in MiniDai.miniDai:
            cx=each.position[0]-x
            cy=each.position[1]-y
            if each.direction=="right" and each.attackTimer>0:
                image=app.pawnAR[app.pawnARCount]
            elif each.direction=="left" and each.attackTimer>0:
                image=app.pawnAL[app.pawnALCount]
            elif each.direction=="right":
                image=app.pawnR[app.pawnRCount]
            elif each.position=="left":
                image=app.pawnL[app.pawnLCount]
            else:image=app.pawnL[app.pawnLCount]
            
            canvas.create_image(cx,cy,image=image)
            canvas.create_rectangle(cx-30,cy-60,cx-30+60*(each.health/90),
            cy-55,fill="red")
def drawKunKun(app,canvas):
    x=miku.drawVector[0]
    y=miku.drawVector[1]
    if DaiBao.dai!=[]:
        for emo in DaiBao.dai:
            cx=emo.position[0]-x
            cy=emo.position[1]-y
           
            if emo.direction=="left":
                image = app.kunkunL[app.kunkunLCount]
            elif emo.direction=="right":
                image = app.kunkunR[app.kunkunRCount]
            #image= app.scaleImage(image,1/2)
            canvas.create_image(cx-30,cy+60,image=image)
            canvas.create_rectangle(cx-100,cy-100,cx-100+200*(emo.health/emo.maxHealth),cy-80
            ,fill="red")
            

def drawButton(app,canvas):
    if Button.button!=[] and Game.phase==0:
        for bot in Button.button:
            x0=bot.parameter[0][0]
            y0=bot.parameter[0][1]
            x1=bot.parameter[1][0]
            y1=bot.parameter[1][1]
            if bot.locked ==False:
                canvas.create_rectangle(x0,y0,x1,y1,fill="gray")
            elif bot.locked ==True:
                canvas.create_rectangle(x0,y0,x1,y1,fill="red")
            canvas.create_text(x0+(x1-x0)/2,y0+(y1-y0)/2,text=f"{bot.name}",font="Arial 20")
            if bot.name=="Background" and Game.backgroundMode==True:
                canvas.create_rectangle(x0,y0,x1,y1,fill="cyan")
                canvas.create_text(x0+(x1-x0)/2,y0+(y1-y0)/2,text="Background: On",font="Arial 20")
            if bot.name=="Boss Animation" and Game.complexBossAnimation==True:
                canvas.create_rectangle(x0,y0,x1,y1,fill="cyan")
                canvas.create_text(x0+(x1-x0)/2,y0+(y1-y0)/2,text="Boss Animation: Complex",font="Arial 20")



def drawAttack(app,canvas):
    x=miku.drawVector[0]
    y=miku.drawVector[1]
    if miku.skill==True:     
        cy=miku.position[1]-y
        cx=miku.position[0]-x
        photoImage= app.roar[app.roarCount]
        canvas.create_image(cx,cy-50,image=photoImage)
    elif 7<miku.attackTimer<12:
        if True:
            (cx0,cy0,cx1,cy1,cx2,cy2,cx3,cy3,cx4,cy4,cx5,
             cy5,cx6,cy6,cx7,cy7,cx8,cy8,cx9,cy9,
             cx10,cy10,cx11,cy11,cx12,cy12,cx13,cy13,cx14,cy14,
             cx15,cy15,cx16,cy16,cx17,cy17,cx18,cy18,cx19,cy19,
             cx20,cy20,cx21,cy21,cx22,cy22,cx23,cy23)=attack.parameter
            '''canvas.create_polygon(cx0,cy0,
                            cx1,cy1,
                            cx2,cy2,
                            cx3,cy3,
                            cx4,cy4,
                            cx5,cy5,
                            cx6,cy6,
                           cx7,cy7,
                            cx8,cy8,
                            cx9,cy9,
                           fill="red")'''
            
            if miku.direction["up"]==True and miku.skill==False:
                cy=cy0-65-y
                cx=cx0-30-x
                photoImage = app.slashImage_up[app.slashCount_up]
                canvas.create_image(cx,cy,image=photoImage)
            elif miku.direction["down"]==True and miku.skill==False:
                cy=cy0+65-y
                cx=cx0-30-x
                photoImage = app.slashImage_down[app.slashCount_down]
                canvas.create_image(cx,cy,image=photoImage)
            elif miku.direction["right"]==True and miku.skill==False:
                cx=cx0+65-x
                cy=cy0-30-y
                photoImage = app.slashImage_right[app.slashCount_right]
                canvas.create_image(cx,cy,image=photoImage)
            elif miku.direction["left"]==True and miku.skill==False:
                cx=cx0-65-x
                cy=cy0-30-y
                photoImage = app.slashImage_left[app.slashCount_left]
                canvas.create_image(cx,cy,image=photoImage)  
def drawBackground(app,canvas):
    x=miku.drawVector[0]
    y=miku.drawVector[1]
    image=getCachedPhotoImage(app, app.background)
    canvas.create_image(app.width/2, app.height/2, image= image)
def drawLosing(app,canvas):
    canvas.create_image(app.width/2, app.height/2, image=ImageTk.PhotoImage(app.losing))
    canvas.create_text(app.width/2,app.height/2+400,text="You're dead! Click anywhere to restart",fill="red",
    font="Arial 28")
def drawWining(app,canvas):
    canvas.create_image(app.width/2, app.height/2, image=ImageTk.PhotoImage(app.ma))
    canvas.create_text(app.width/2,app.height/2+300,text="Click anywhere to restart",fill="red",
    font="Arial 28")
def drawParaProjectile(app,canvas):
    cx=miku.drawVector[0]
    cy=miku.drawVector[1]
    image=getCachedPhotoImage(app,app.fP)
    if ParabolicProjectile.pProjectileList!=[]:
        for each in ParabolicProjectile.pProjectileList:
            x=each.position[0]-cx
            y=each.position[1]-cy
            canvas.create_oval(x-15,y-15,x+15,y+15,fill="red")
            canvas.create_image(x,y,image=image)

def drawHealth(app,canvas):
    for i in range(miku.health):
        canvas.create_image(20+i*60,50,image=ImageTk.PhotoImage(app.health))

def drawRage(app,canvas):
    canvas.create_rectangle(20,130,20+150*(miku.rage/miku.maxRage),150,fill="orange")
    canvas.create_line(20+150*(1/3),130,20+150*(1/3),150, fill="orange")
    canvas.create_line(20+150*(2/3),130,20+150*(2/3),150, fill="orange")
    canvas.create_line(20+150*(3/3),130,20+150*(3/3),150, fill="orange")
def drawDrone(app,canvas):
    x=miku.drawVector[0]
    y=miku.drawVector[1]
    if Drone.droneList!=[]:
        for each in Drone.droneList:
            cx=each.position[0]-x
            cy=each.position[1]-y
            if each.direction=="right" and each.attackTimer>0:
                image=app.droneAR[app.droneARCount]
            elif each.direction=="left" and each.attackTimer>0:
                image=app.droneAL[app.droneALCount]
            elif each.direction=="right":
                image=app.droneR[app.droneRCount]
            elif each.position=="left":
                image=app.droneL[app.droneLCount]
            else:image=app.droneL[app.droneLCount]
            canvas.create_image(cx,cy,image=image)
            canvas.create_rectangle(cx-50,cy-60,cx-50+60*(each.health/90),
            cy-55,fill="red")
def drawSocery(app,canvas):
    x=miku.drawVector[0]
    y=miku.drawVector[1]
    if Socery.socery!=[]:
        for each in Socery.socery:
            cx=each.position[0]-x
            cy=each.position[1]-y
            if each.attackTimer>0:
                if each.direction=="right":
                    image=app.soceryAR[app.soceryARCount]
                elif each.direction=="left":
                    image=app.soceryAL[app.soceryALCount]
            else:
                if abs(each.position[0]-miku.position[0])<=500:
                    if each.direction=="right":
                        image=app.soceryIR[app.soceryIRCount]
                    elif each.direction=="left":
                        image=app.soceryIL[app.soceryILCount]
                else:
                    if each.direction=="right":
                        image=app.soceryR[app.soceryRCount]
                    elif each.direction=="left":
                        image=app.soceryL[app.soceryLCount]
            canvas.create_image(cx,cy,image=image)
            canvas.create_rectangle(cx-30,cy-60,cx-30+60*(each.health/90),
            cy-55,fill="red")

def drawIcicle(app,canvas):
    x=miku.drawVector[0]
    y=miku.drawVector[1]
    if Icicle.icicleList!=[]:
        for each in Icicle.icicleList:
            cx0=each.parameter[0][0]-x
            cy0=each.parameter[0][1]-y
            cx1=each.parameter[1][0]-x
            cy1=each.parameter[1][1]-y
            if each.status=="shadow":
                
                image=getCachedPhotoImage(app,app.iceS_shadow)
                if Game.complexBossAnimation==False:
                    canvas.create_rectangle(cx0,cy0,cx1,cy1,fill="",outline="blue")
                x0=each.position[0]-x
                y0=each.position[1]-y
                if Game.complexBossAnimation==True:
                    canvas.create_image(x0,cy0+350,image=image)   
            elif each.status=="real":
                image=getCachedPhotoImage(app,app.iceS)
                if Game.complexBossAnimation==False:
                    canvas.create_rectangle(cx0,cy0,cx1,cy1,fill="blue",outline="blue")
                x0=each.position[0]-x
                y0=each.position[1]-y
                if Game.complexBossAnimation==True:
                    canvas.create_image(x0,cy0+350,image=image)
def drawFinal(app,canvas):
    image=getCachedPhotoImage(app,app.icecream)
    canvas.create_image(app.width/2,app.height/2,image=image)
    canvas.create_text(app.width/2,700,text="Congrats, here is your ice cream! Click everywhere to restart"
    ,fill="cyan",font="Arial 19")
def drawFN(app,canvas):
    x=miku.drawVector[0]
    y=miku.drawVector[1]
    if FN.nova!=[]:
        for fn in FN.nova:
            cx=fn.position[0]-x
            cy=fn.position[1]-y
            if fn.aiTimer>0:
                if fn.direction=="left":
                    image =app.idleL[app.idleLCount]
                elif fn.direction=="right":
                    image =app.idleR[app.idleRCount]
            elif fn.dashTimer>0:
                if fn.dash_direction=="left":
                    image =app.atkL[app.atkLCount]
                elif fn.dash_direction=="right":
                    image =app.atkR[app.atkRCount]
            elif fn.icicleTimer>0:
                if fn.direction=="left":
                    image =app.icicleL[app.icicleLCount]
                elif fn.direction=="right":
                    image =app.icicleR[app.icicleRCount]
            elif fn.projectileTimer>0:
                if fn.projectile_direction=="left":
                    image =app.atkL[app.atkLCount]
                elif fn.projectile_direction=="right":
                    image =app.atkR[app.atkRCount]
            elif fn.aoeTimer>0:
                if fn.direction=="left":
                    image =app.aoeL[app.aoeLCount]
                elif fn.direction=="right":
                    image =app.aoeR[app.aoeRCount]
            canvas.create_image(cx,cy,image=image)
            canvas.create_rectangle(cx-60,cy-70,cx-60+120*(fn.health/fn.maxHealth),
            cy-60,fill="red")
def redrawAll(app,canvas):
    
    if Game.phase==0:
        canvas.create_image(app.width/2, app.height/2, image=ImageTk.PhotoImage(app.background))
        canvas.create_image(720, 100, image=ImageTk.PhotoImage(app.image0))
        drawButton(app,canvas)
        if Button.rTimer>0:
            canvas.create_text(app.width/2,200,text="You need to beat The Flying Columbian first to unlock this boss fight!"
            ,fill="red",font="Arial 18")

    elif Game.phase==1 or Game.phase==4 or Game.phase=="practice" or Game.phase=="FN":
        canvas.create_rectangle(0,0,app.width,app.height,fill="black")  
        if Game.backgroundMode==True:
            drawBackground(app,canvas)
        drawLandscape(app,canvas)
 
        drawMiku(app,canvas)
        drawIcicle(app,canvas)
    #drawEnemy(app,canvas)
        drawAttack(app,canvas)
        drawProjectile(app,canvas)
        drawKunKun(app,canvas)
        drawMiniDai(app,canvas)
        drawDrone(app,canvas)
        drawParaProjectile(app,canvas)
        drawHealth(app,canvas)
        drawSocery(app,canvas)
        drawWave(app,canvas)
        drawFN(app,canvas)
        drawRage(app,canvas)
    if Game.phase=="practice":
        canvas.create_text(app.width/2,200,text="Practice Mode, click everywhere to quit",fill="red",font="Arial 18")
    elif Game.phase==2:
        drawLosing(app,canvas)
    elif Game.phase=="help":
        canvas.create_image(app.width/2, app.height/2, image=ImageTk.PhotoImage(app.background))
        canvas.create_image(720, 100, image=ImageTk.PhotoImage(app.image0))
        canvas.create_image(app.width/2, app.height/2+150,image=ImageTk.PhotoImage(app.readme))
        canvas.create_text(app.width/2,850,text="click anywhere to start playing the game",fill="red",font="Arial 18")

    if Game.w==True and Game.phase==1:
        drawWining(app,canvas)
    if Game.w==True and Game.phase=="FN":
        drawFinal(app,canvas)
    
runApp(width=1600,height=1200)
