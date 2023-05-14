z = 200
x = 100
c = 500
v = 300
b = 200
n = 100
m = 300
a = 200
def setup():
    size(600,600)
    background(0)
    frameRate(5)
def draw():
    background(0)
    global z,x,c,v,b,n,m,a
    push()
    fill(223,12,23)
    ellipse(z,x,100,100)
    pop()
    push()
    fill(0, 206, 209)
    ellipse(c,v,150,150)
    pop()
    push()
    ellipse(n,b,50,50)
    pop() 
    push()
    ellipse(a,m,50,50)
    pop()
    point(random(5,600),random(5,600))
    point(random(5,600),random(5,600))
    point(random(5,600),random(5,600))
    point(random(5,600),random(5,600))
    point(random(5,600),random(5,600))
    point(random(5,600),random(5,600))
    point(random(5,600),random(5,600))
    point(random(5,600),random(5,600))
    point(random(5,600),random(5,600))
    point(random(5,600),random(5,600))
    point(random(5,600),random(5,600))
    point(random(5,600),random(5,600))
    point(random(5,600),random(5,600))
    point(random(5,600),random(5,600))
    point(random(5,600),random(5,600))
    point(random(5,600),random(5,600))
    point(random(5,600),random(5,600))
    point(random(5,600),random(5,600))
    stroke(random(0,255),random(0,255),random(0,255))
    strokeWeight(random(1,10))
    z += 0
    x += 0
    c += 0
    v += 0
    b += 1
    n += 1
    m += 2
    a += 1
