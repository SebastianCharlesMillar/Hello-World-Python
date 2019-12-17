#paddle
#paddle is a rectangle and 2 circles
#make paddle move with keys
#make paddle move with mouse
padpos = 0
def setup():
    size(500, 500)
    background(3)
"""
def paddle():
    circle(mouseX,390, 20)
    circle(mouseX + 20,390, 20)
    rect(mouseX,380,20,20)

def paddlekey(mouse_pos):
    circle(mouse_pos, 390, 20)
    circle(mouse_pos + 20, 390, 20)
    rect(mouse_pos, 380, 20, 20)
    """
def draw():
    x= 1
    #paddle()
    #global i
    #i = pmouseX
    #if keyPressed:
       # if keyCode == LEFT:
       #  i = i - 10
            
        # paddlekey(i)       


def keyPressed():
    paddlekey1()
    
def mousePressed():
        paddle1()
    
def paddle1():
    global padpos
    padpos = mouseX
    circle(padpos,390, 20)
    circle(padpos + 20,390, 20)
    rect(padpos,380,20,20)
    
def paddlekey1():
    circle(padpos, 390, 20)
    circle(padpos + 20, 390, 20)
    rect(padpos, 380, 20, 20)
