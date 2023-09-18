def setup():
    size(600,600)
    background('#004477')
    frameRate(20)

def draw():
    print('x:%s, y:%s' % (mouseX, mouseY))
    fill('#FFFFFF')
    ellipse(mouseX,mouseY, 20,20)
