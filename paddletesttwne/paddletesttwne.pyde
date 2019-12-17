def setup():
    size(500, 500)
    background(30)

padpos=250    

def paddle():
    circle(padpos , 390 , 20)
    circle(padpos + 20 , 390, 20)
    rect(padpos, 380 , 20 , 20)
    
def draw():
    pushMatrix()
    translate(mouseX,0)       
    paddle()
    popMatrix()

  #create a keystroke mode when keyboard is used
     #within the keystroke mode we have left and right movement with keys
  
  #create a mouse mode when the mouse is used
     #within mouse mode we have left and right movement with the mouse
     
     
#when KeyPressed start key control
    #left key press moves left
    #right key press moves right
    
#when mousePressed start mouse control
    #mousex follows mouse
