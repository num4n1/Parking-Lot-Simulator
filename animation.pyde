#def parkinglot():
x=0
y=0
colorselector_row=0
colorselector_col=0
vacant_lot=0
occupied=[]
a=False
b=0
no_of_customers=0
earning=0
w1=15
w2=65
w3=2000
w4=2000
gate_condition=False
exit_condition=False

def setup():
    
    smooth()
    frameRate(60)
    size(1920,1080)
    background(26,183,79)
    p1.parking()


def draw():
    
    delay(100)
    s1.street_design()
    obj.body() 
    m1.moving()
    o1.stall()
class Gate:
    
    #stat = True
    #sp = 0
    def __init__(self, s, status):
        self.stat = status
        self.sp = s

    #space = str(sp)
    
    def body(self):
        
        global gate_condition
        textSize(15)
        fill(255)
        strokeWeight(2)
        fill(51,158,222)
        rect(805, 300, 100, 20)
        fill(255)
        rect(805, 320, 100, 20)
        rect(805, 825, 100, 20)
        rect(805, 845, 100, 20)
        fill(0)
        text("Entry", 825, 315)
        text("Exit", 825, 840)
        text("Spaces:"+ str(60-len(occupied)/2), 825, 335)
        
        if(gate_condition):
            strokeWeight(8)
            line(910, 320, 995, 350)
        
        else:
            strokeWeight(8)
            line(910, 330, 995, 330) 
         
            
        if(exit_condition):
            strokeWeight(8)
            line(910, 835, 995, 855)
            
        else:
            strokeWeight(8)
            line(910, 835, 995, 835)
            
        
        strokeWeight(1)
        
obj = Gate(20,True)
    
