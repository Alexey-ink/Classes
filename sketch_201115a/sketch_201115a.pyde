width = 500
height = 500
inside = color (0, 255, 255)
nx = 8
ny = 8
len = 50
type_forms = 0
#0 - line, 1 - rect, 2 - ellipse
def setup(): 
   size(width, height)
   stroke(0, 240, 0)
   frameRate(1)
   
def draw():
    global type_forms
    background(255, 255, 0)
    fill(inside)
    for i in range(ny):
        for k in range(nx):
            x = ((k+1)*width/nx)-(width/nx/2)
            y = ((i+1)*height/ny)-(height/ny/2)
            if type_forms == 0:
               line(x, y-len/2, x, y+len/2)
            if type_forms == 1:
               rect(x-len/2, y-len/2, len, len)
            if type_forms == 2:
               ellipse(x, y, len, len)                    
    type_forms = (type_forms + 1) % 3                                               
    
      
