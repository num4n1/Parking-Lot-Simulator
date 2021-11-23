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
    
