#Jenny Chen 

from random import *
from pygame import *
from tkinter import *
from math import *
from queue import *

root=Tk()  
root.withdraw()
init()
font.init()
#######################################################################
#colours

RED=(255,0,0) 
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)
MINT=(44,214,104)
GRAPE=(55,18,102)
ROSERED=(193,27,27)
LILAC=(220,43,226)
PLUM=(56,26,56)
OLIVE=(85,107,47)
NAVY=(6,13,105)
ORCHID=(218,112,214)

#####################################################################
#music

mixer.music.load("music.mp3")#import music
mixer.music.play(-1) #play the music forever

######################################################################
#set up

size=(1024,768) #screen resolution
screen=display.set_mode(size)#creating a 800x600 window
display.set_caption("Bonbon Cakery Paint") #title
myClock=time.Clock() #for frame rate

########################################################################
#naming 

running=True #boolean variable
font=font.SysFont("Tw Cen MT Condensed Extra Bold",20) #the font I use
undoList=[] #list for undo pictures
redoList=[] #list for redo pictures
mmouse="up" #variable that keeps track of if the mouse is down or not, this is used for the stamps and when the cursor is visable 
decoPos=0 #variable for posistion of the decorations
cakePos=0 #variable for position of the cakes
platePos=0 #variable for position of the plates
backGPos=0 #variable for position of the backgrounds
markerR=10 #variable for the radius for the marker
sprayR=20 #variable for the radius of the spray paint
lineT=1 #variable for the thickness of the line
reT=1 #variable for the thickness of the rectangle and the ellipse
polyT=1 #a variable for the thickness of the polygon 
tool="no tool" #variable for the current tool
polyPoints=[] #list for points for drawing the polygon
col=BLACK #variable for colour, and is set to the default colour
omx,omy=300,300 #a variable that keeps track of where the mouse was in the last loop

########################################################################
#loading pictures

title=image.load("Images/title.png") #the title
background=image.load("Images/background.png") #the background

#list for groups of pictures
#the tool icon pictures
toolsList=["pencil.png","eraser.png","marker.png","spraypaint.png","bucket.png","line.jpg","rectangle.jpg","ellipse.png","polygon.jpg","clear.png","undo.png","redo.png","open.png","save.png"]
toolsPics=[] #a list for loaded pictures
for tool in toolsList: #load the pictures in a loop
    pic=image.load("Images/tools/"+tool) #load the picture
    toolsPics.append(pic) #append the picture

#repeat for all other groups of pictures
    
#decoration stamps
decoList=["almond.png","bigBerry.png","chocoDeluxe.png","chocoSticks.png","hardCandy.png","icecream.png","kiwi.png","mint.png","sprinkles.png","starCookie.png"]
decoPics=[]
for deco in decoList:
    pic=image.load("Images/stamps/ingredients/"+deco)
    decoPics.append(pic)
    
#cake stamps
    
    #the actual stamps
cakeList=["tiramisu.png","cakeRoll.png","creamPuff.png","pudding.png","3layered.png","cheesecake.png"]
cakePics=[]
for cake in cakeList:
    pic=image.load("Images/stamps/cakes/"+cake)
    cakePics.append(pic)
    #the icons for the cakes
cakeIconList=["tiramisuSmall.png","cakeRollSmall.png","creamPuffSmall.png","puddingSmall.png","3layeredSmall.png","cheesecakeSmall.png"]
cakeIcons=[]
for cake in cakeIconList:
    pic=image.load("Images/stamps/cakes/"+cake)
    cakeIcons.append(pic)

#plate stamps
    
    #actual plate stamps
plateList=["plainPlate.png","cosmicPlateIcon.png","elegantPlate.png","galacticPlate.png","lacquerPlate.png"] 
platePics=[]
for plate in plateList:
    pic=image.load("Images/stamps/plates/"+plate)
    platePics.append(pic)
    #plate icons 
plateIconList=["plainPlateIcon.png","cosmicPlateIcon.png","elegantPlateIcon.png","galacticPlateIcon.png","lacquerPlateIcon.png"]
plateIcons=[]
for plate in plateIconList:
    pic=image.load("Images/stamps/plates/"+plate)
    plateIcons.append(pic)

#background stamps
    
    #the actual backgrounds
backGList=["background1.png","doorstep.png","table.png"]
backGPics=[]
for back in backGList:
    pic=image.load("Images/backgroundStamps/"+back)
    backGPics.append(pic)
    #background icons
backIconsList=["background1Icon.png","doorstepIcon.png","tableIcon.png"]
backGIcons=[]
for back in backIconsList:
    pic=image.load("Images/backgroundStamps/"+back)
    backGIcons.append(pic)
    
palette=image.load("Images/tools/palette.png") #the palette
guider=image.load("Images/guider.png") #the person that is talking

########################################################################
#making the rectangles

rectList=[] #a list for all the tool rectangles
pencilRect=Rect(35,265,60,60) #the pencil rectangle
rectList.append(pencilRect) #add the rectangles into a list so they are easier to use
eraserRect=Rect(105,265,60,60)#the eraser rectangle
rectList.append(eraserRect)
markerRect=Rect(35,330,60,60) #the marker rectangle
rectList.append(markerRect)
sprayRect=Rect(105,330,60,60) #the spraypaint rectangle
rectList.append(sprayRect)
bucketRect=Rect(35,395,60,60) #the fill rectanlge
rectList.append(bucketRect)
lineRect=Rect(105,395,60,60) #the line tool rectangle
rectList.append(lineRect)
rectangleRect=Rect(35,460,60,60) #the rectangle tool rectangle
rectList.append(rectangleRect)
ellipseRect=Rect(105,460,60,60) #the ellipse tool rectangle
rectList.append(ellipseRect)
drawpolyRect=Rect(35,525,60,60) #the draw polygon tool rectangle
rectList.append(drawpolyRect)
clearRect=Rect(105,525,60,60) #the clear screen rectangle
rectList.append(clearRect)
undoRect=Rect(35,590,60,60) #the undo rectangle
rectList.append(undoRect)
redoRect=Rect(105,590,60,60) #the redo rectangle
rectList.append(redoRect)
openRect=Rect(35,655,60,60) #the open tool rectangle
rectList.append(openRect)
saveRect=Rect(105,655,60,60) #the save tool rectangle
rectList.append(saveRect)

paletteRect=Rect(849,150,150,111) #the palette rectangle

decoRect=Rect(864,270,120,120) #the decoration stamp rectangle
cakeRect=Rect(849,400,150,150) #the cake stamp rectangle
plateRect=Rect(839,560,170,80) #the plate stamp rectangle
backGRect=Rect(849,650,150,100) #the background stamp rectangle

posRect=Rect(30,717,140,25) #the rectangle that displays the position 
sizeRect=Rect(25,738,150,25) #the rectangle that displays the size or thickness of the tool
colRect=Rect(437,735,140,25) #the rectanlge that displays the rectangle
currentColRect=Rect(497,737,79,22) #the rectangle displaying the current colour

randColRect=Rect(869,130,110,20) #the rectangle to get a random colour

canvasRect=Rect(200,150,624,568) #the canvas rectangle
textRect=Rect(60,150,105,100) #the rectangle that displays info

#######################################################################
#blitting pics

screen.blit(background,(0,0)) #blitting the background

x=35 #a variable for the x coord
y=265 #a variable for the y  coord
c=1 #a marker to see if we need move down to the next line or not

for pics in toolsPics: #blit the pictures of the tools in a loop
    screen.blit(pics,(x,y)) #blit the pics at the (x,y) values
    
    if x==35: #if x=35, then it is on the right and we need to set the variable to 105 so it is to the left
        x=105
    else: #if x=105 then we move it back to the left
        x=35
        
    if c==2: #c tells if this is the first or second box in the row, because we need to use the same y coord twice 
        c=1      #if c=2 then it is the second one and we move back to the first
        y+=65         #and add 65 to move down to the next row
    else:  #if this is the first box, we just add one to c
        c+=1

screen.blit(palette,(849,150)) #blit the palette onto the screen
screen.blit(title,(165,2)) #blit the title onto the screen
screen.blit(guider,(20,200)) #blit the person that talks onto the screen

#######################################################################
#fill function

def fill(surface,x,y,col): #defining the fill function
     pixels=[(x,y)] #a list of the pixels that need to be check
     firstCol=surface.get_at((x, y)) #this is the colour that is clicked on
     if firstCol!=col: #if the colour clicked isn't the same as the selected colour, then it starts filling
          while len(pixels)>0: #keeps setting pixels as long as there are coordinates in the list
              #if the pixel is within the boundaries of the canvas and that pixel is the same as the colour of the pixel the user clicked on then it is filled
               if pixels[0][0]>=200 and pixels[0][0]<824 and pixels[0][1]>=150 and pixels[0][1]<718 and surface.get_at(pixels[0])==firstCol:
                    surface.set_at((pixels[0]),col) #set the pixel at the front of the list as the wanted colour
                    pixels.append((pixels[0][0], pixels[0][1]-1)) #and the pixels that are one unit up, down, left and right of that pixel are added into the list to be checked
                    pixels.append((pixels[0][0], pixels[0][1]+1))
                    pixels.append((pixels[0][0]-1, pixels[0][1]))
                    pixels.append((pixels[0][0]+1, pixels[0][1]))
               del pixels[0] #we delete the list of pixel when we're done

########################################################################
#drawing tool rectangles

for pics in rectList: #with the list of tool rectangles, I draw the outlines in a list
    draw.rect(screen,LILAC,pics,2) 


draw.rect(screen,WHITE,decoRect) #drawing the white box for the decoration stamps
screen.blit(decoPics[0],(864,270)) #blitting the first stamp there 
draw.rect(screen,LILAC,decoRect,2) #drawing the outline for the decoration stamps

draw.rect(screen,WHITE,cakeRect) #drawing the white box for cake stamps 
screen.blit(cakeIcons[0],(849,400)) #blitting the first cake stamp there 
draw.rect(screen,LILAC,cakeRect,2) #drawing the outline for the cake stamps

draw.rect(screen,WHITE,plateRect) #drawing the white box for the plate stamps 
screen.blit(plateIcons[0],(839,560)) #blitting the first plate stamp there
draw.rect(screen,LILAC,plateRect,2) #drawing the outline for the plate stamps

                                    #the backgrounds don't need a white box
screen.blit(backGIcons[0],(849,650)) #we blit the first background
draw.rect(screen,LILAC,backGRect,2) #drawing the outline

draw.rect(screen,WHITE,textRect) #the white box for the text rectangle
draw.rect(screen,LILAC,textRect,2) #the outline for the text rectangle

draw.rect(screen,WHITE,posRect) #the white box for the rectangle that displays position
draw.rect(screen,LILAC,posRect,2) #the outline for the rectangle

draw.rect(screen,WHITE,sizeRect) #the white box for the rectangle that displays sizer
draw.rect(screen,LILAC,sizeRect,2) #the outline for the rectangle

draw.rect(screen,WHITE,colRect) #the white box for the rectangle that displays the colour
draw.rect(screen,LILAC,colRect,2) #the outline for the rectangle
draw.rect(screen,BLACK,currentColRect) #we draw the current colour as black because that is the default colour

draw.rect(screen,WHITE,randColRect) #the white box for the random colour rectangle
draw.rect(screen,LILAC,randColRect,2) #the outline for the rectangle

draw.rect(screen,WHITE,canvasRect) #drawing the canvas

######################################################################
#text

greeting=font.render("Hello :)",True,BLACK) #the first message in the text box and blitting it 
screen.blit(greeting,(83,180))

positionText=font.render("Position:",True,BLACK) #the text that tells us the numbers displayed are the coordinates of the mouse and blitting it 
screen.blit(positionText,(35,720))

sizeText=font.render("Size/Thickness:",True,BLACK) #the text that tells us the number displayed is the size or thickness and blitting it 
screen.blit(sizeText,(28,742)) 

colourText=font.render("Colour:",True,BLACK) #the text that displays the colour and blitting it 
screen.blit(colourText,(442,740))

randColText=font.render("Random Colour",True,BLACK) #the text for the random colour box and blitting it 
screen.blit(randColText,(872,132))

#####################################################################
#copying the screen

backUndo=screen.subsurface(canvasRect).copy() #for undo function
undoList.append(backUndo) #add it into the list so the first item is a blank screen
screenBuff=screen.subsurface(canvasRect).copy() #for the stamps 

while running:
    
    clicked=False #after a loop we set these thing false because we want them true when they happen
    unclicked=False
    scroll=False
    scrollUp=False
    scrollDown=False
    rightClicked=False

    mx,my=mouse.get_pos() #getting the position of the mouse
    mb=mouse.get_pressed() #getting information of if the mouse is being clicked or not

    for evt in event.get(): 
        if evt.type==QUIT: #if the user closes the window
            running=False
            
        if evt.type==MOUSEBUTTONDOWN: #if something on the mouse is being pressed
            if evt.button==1: #if left clicked
                clicked=True #the variable clicked is true, this is used for many tools
                back=screen.subsurface(canvasRect).copy() #copies the canvas when clicked for the line, rectangle, and ellipse tool
                start=mx,my
                lx,ly=mx,my #gets where the mouse started for the line tool
                
            if evt.button==3: #if right clicked
                rightClicked=True #for polygon tool
                
            if evt.button==4: #if scroll up
                scrollUp=True #scrolling up is true
                scroll=True #scrolling in general is true
            
            if evt.button==5: #if scrolling down
                scrollDown=True #scrolling down is true
                scroll=True #scrolling in general is true
                
        if evt.type==MOUSEBUTTONUP: #if the mouse has lifted after being clicked
            unclicked=True #the variable unclicked is true

    ###########################################################            
    #drawing boxes
            
    for rect in rectList: #redraw the rectangles every loop so if no rectangles are drawn red, they will turn back to lilac
        draw.rect(screen,LILAC,rect,2)
        
    draw.rect(screen,LILAC,randColRect,2) #including the rectangles in the list we draw the random colour rect, 
    draw.rect(screen,LILAC,decoRect,2) #decoration rect,
    draw.rect(screen,LILAC,cakeRect,2) #cake rect,
    draw.rect(screen,LILAC,plateRect,2) #plate rect,
    draw.rect(screen,LILAC,backGRect,2) #and background rect
    
    ################################################################
    #undo/redo

    if canvasRect.collidepoint(mx,my) and mb[0]==1: #for the undo redo tool, if the user were to draw on the canvas again, everything in the redo list is deleted
        del redoList[:]
        
    if canvasRect.collidepoint(mx,my)and unclicked and not scroll: #if the mouse has finished drawing on the canvas we append that picture to the undolist
        backUndo=screen.subsurface(canvasRect).copy() #copy the screen to add to the undo list
        undoList.append(backUndo)                                   #and since none of the tools use scroll to draw, I make sure it doesn't append the picture after scrolling to the list

    ###############################################################
    #selecting tools
        
    if pencilRect.collidepoint(mx,my): #for all tools, if the mouse is hovering over the box, we draw the highlighting (red rectangle of that tool)
        draw.rect(screen,RED,pencilRect,2)
        if clicked: #if you mouse button down on the box, it will change the tool
            tool="pencil" #when you use mb[0]==1 to change the tool, if the mouse accidently went out of the canvas while drawing, the tool would change
        
    if eraserRect.collidepoint(mx,my):
        draw.rect(screen,RED,eraserRect,2)
        if clicked:
            tool="eraser"
            markerR=10 #if a tool has a thickness variable and it is re-selected, the thickness is changed back to the default thickness

    if markerRect.collidepoint(mx,my):
        draw.rect(screen,RED,markerRect,2)
        if clicked:
            tool="marker"
            markerR=10

    if sprayRect.collidepoint(mx,my):
        draw.rect(screen,RED,sprayRect,2)
        if clicked:
            tool="spray"
            sprayR=20
            
    if bucketRect.collidepoint(mx,my):
        draw.rect(screen,RED,bucketRect,2)
        if clicked:
            tool="bucket"        
            
    if lineRect.collidepoint(mx,my):
        draw.rect(screen,RED,lineRect,2)
        if clicked:
            tool="line"
            lineT=1
            
    if rectangleRect.collidepoint(mx,my):
        draw.rect(screen,RED,rectangleRect,2)
        if clicked:
            tool="rectangle"
            reT=1
            
    if ellipseRect.collidepoint(mx,my):
        draw.rect(screen,RED,ellipseRect,2)
        if clicked:
            tool="ellipse"
            reT=1
            
    if drawpolyRect.collidepoint(mx,my):
        draw.rect(screen,RED,drawpolyRect,2)
        if clicked:
            tool="polygon"
            polyT=1

    if clearRect.collidepoint(mx,my):
        draw.rect(screen,RED,clearRect,2)
        if clicked:
            tool="clear"
            draw.rect(screen,WHITE,canvasRect) #since this tool is clear, the canvas rectangle is simply drawn on to avoid more lines of code
            backUndo=screen.subsurface(canvasRect).copy() #this is added to the undoList in case the user wishes to undo
            undoList.append(backUndo)
            

    if undoRect.collidepoint(mx,my):
        draw.rect(screen,RED,undoRect,2)
        if clicked:
            tool="undo" #undo and redo are done as soon as the user clicks on the rectangles, because the mouse does not need to be on the canvas
            if len(undoList)>1: #if there is more than 1 item in the list, that means there are pictures that we can blit, because we start with a blank canvas in the list, the blank is never blit onto the screen
                undo=undoList.pop() #pop the undoList (take the last item of the list out)
                redoList.append(undo) #and add it to the redoList
                screen.blit(undoList[-1],(200,150)) #since the last item has been taken out already, the last item from the undoList is blit onto the screen
       
    if redoRect.collidepoint(mx,my):
        draw.rect(screen,RED,redoRect,2)
        if clicked:
            tool="redo"
            if len(redoList)>0: #as long as there is at least one item in the list, there is something to blit onto the screen
                screen.blit(redoList[-1],(200,150)) #blit the last item in the redo list
                redo=redoList.pop() #pop the list and we add the item to the undo list
                undoList.append(redo)
                
    if openRect.collidepoint(mx,my): 
        draw.rect(screen,RED,openRect,2)
        if clicked: #open and save are done right here
            tool="open"
            try: #try and pass in case something goes wrong
                fname=filedialog.askopenfilename(filetypes=[("Images","*.png;*.jpg;*.jpeg;*.bmp")]) #ask to open a file
                openPic=image.load(fname) #load that picture
                screen.blit(openPic,(200,150)) #and blit the picture onto the canvas
            except:
                pass
            
    if saveRect.collidepoint(mx,my):
        draw.rect(screen,RED,saveRect,2)
        if clicked:
            tool="save"
            try:
                fname=filedialog.asksaveasfilename(defaultextension=".png") #we ask for a file name
                image.save(screen.subsurface(canvasRect),fname) #and save the canvas image
            except:
                pass
            
    if randColRect.collidepoint(mx,my):
        draw.rect(screen,RED,randColRect,2)
        if clicked: #don't give random colour a tool name because it is more convienient to select a random colour and continue to draw, and the box is red just when the user clicks or hovers on the rect 
            col=(randint(0,255),randint(0,255),randint(0,255)) #set the colour variable as a random colour
            draw.rect(screen,col,currentColRect) #and draw the current colour rectangle as that colour
            
    if decoRect.collidepoint(mx,my):
        draw.rect(screen,RED,decoRect,2)
        if clicked:
            tool="decoration"

            
    if cakeRect.collidepoint(mx,my):
        draw.rect(screen,RED,cakeRect,2)
        if clicked:
            tool="cake"
            
    if plateRect.collidepoint(mx,my):
        draw.rect(screen,RED,plateRect,2)
        if clicked:
            tool="plate"


    if backGRect.collidepoint(mx,my):
        draw.rect(screen,RED,backGRect,2)
        if clicked:
            tool="background"
            screen.blit(backGPics[backGPos],(200,150)) #blit the background as soon as the user presses the box
            backUndo=screen.subsurface(canvasRect).copy() #and we add this to the undo list
            undoList.append(backUndo)


    ####################################################################
    #highlighting boxes
    
    if tool=="pencil": #for each tool, text is displayed to give info
        draw.rect(screen,WHITE,textRect) #draw the text box and its outline again
        draw.rect(screen,LILAC,textRect,2)
        line1=font.render("Pencil",True,BLACK) #render titles and informantion by using variables for line numbers
        line2=font.render("-renders on ",True,PLUM) 
        line3=font.render("scantrons",True,PLUM)
        screen.blit(line1,(75,165)) #and blit the text accordingly
        screen.blit(line2,(65,185))
        screen.blit(line3,(65,195))
        draw.rect(screen,RED,pencilRect,2) #as long as the tool is pencil the tool box will be selected as red
        
    if tool=="eraser":
        draw.rect(screen,WHITE,textRect)
        draw.rect(screen,LILAC,textRect,2)
        line1=font.render("Eraser",True,BLACK)
        line2=font.render("-fixes",True,PLUM)
        line3=font.render("mistakes",True,PLUM)
        line4=font.render("-scroll to",True,PLUM)
        line5=font.render("+/- size",True,PLUM)
        screen.blit(line1,(75,165))
        screen.blit(line2,(65,185))
        screen.blit(line3,(65,195))
        screen.blit(line4,(65,208))
        screen.blit(line5,(65,218))
        draw.rect(screen,RED,eraserRect,2)
        
    if tool=="marker":
        draw.rect(screen,WHITE,textRect)
        draw.rect(screen,LILAC,textRect,2)
        line1=font.render("Marker",True,BLACK)
        line2=font.render("-seeps on",True,PLUM)
        line3=font.render("paper",True,PLUM)
        line4=font.render("-scroll to",True,PLUM)
        line5=font.render("+/- size",True,PLUM)
        screen.blit(line1,(75,165))
        screen.blit(line2,(65,185))
        screen.blit(line3,(65,195))
        screen.blit(line4,(65,208))
        screen.blit(line5,(65,218))
        draw.rect(screen,RED,markerRect,2)
        
    if tool=="spray":
        draw.rect(screen,WHITE,textRect)
        draw.rect(screen,LILAC,textRect,2)
        line1=font.render("Spray",True,BLACK)
        line2=font.render("-vanadlizes",True,PLUM)
        line3=font.render("the canvas",True,PLUM)
        line4=font.render("-scroll to",True,PLUM)
        line5=font.render("+/- size",True,PLUM)
        screen.blit(line1,(75,165))
        screen.blit(line2,(65,185))
        screen.blit(line3,(65,195))
        screen.blit(line4,(65,208))
        screen.blit(line5,(65,218))
        draw.rect(screen,RED,sprayRect,2)
        
    if tool=="bucket":
        draw.rect(screen,WHITE,textRect)
        draw.rect(screen,LILAC,textRect,2)
        line1=font.render("Fill",True,BLACK)
        line2=font.render("-colours big",True,PLUM)
        line3=font.render("or small",True,PLUM)
        line4=font.render("areas (all)",True,PLUM)
        screen.blit(line1,(75,165))
        screen.blit(line2,(65,185))
        screen.blit(line3,(65,195))
        screen.blit(line4,(65,205))
        draw.rect(screen,RED,bucketRect,2)
        
    if tool=="line":
        draw.rect(screen,WHITE,textRect)
        draw.rect(screen,LILAC,textRect,2)
        line1=font.render("Line",True,BLACK)
        line2=font.render("-draws lines",True,PLUM)
        line3=font.render("lines",True,PLUM)
        line4=font.render("-scroll to",True,PLUM)
        line5=font.render("+/- thickness",True,PLUM)
        screen.blit(line1,(75,165))
        screen.blit(line2,(65,185))
        screen.blit(line3,(65,195))
        screen.blit(line4,(65,208))
        screen.blit(line5,(65,218))
        draw.rect(screen,RED,lineRect,2)
        
    if tool=="rectangle":
        draw.rect(screen,WHITE,textRect)
        draw.rect(screen,LILAC,textRect,2)
        line1=font.render("Rectangle",True,BLACK)
        line2=font.render("-draws 90°",True,PLUM)
        line3=font.render("angles (four)",True,PLUM)
        line4=font.render("-scroll to",True,PLUM)
        line5=font.render("+/- thickness",True,PLUM)
        screen.blit(line1,(65,165))
        screen.blit(line2,(65,185))
        screen.blit(line3,(65,195))
        screen.blit(line4,(65,208))
        screen.blit(line5,(65,218))
        draw.rect(screen,RED,rectangleRect,2)
        
    if tool=="ellipse":
        draw.rect(screen,WHITE,textRect)
        draw.rect(screen,LILAC,textRect,2)
        line1=font.render("Ellipse",True,BLACK)
        line2=font.render("-for round",True,PLUM)
        line3=font.render("areas",True,PLUM)
        line4=font.render("-scroll to",True,PLUM)
        line5=font.render("+/- thickness",True,PLUM)
        screen.blit(line1,(75,165))
        screen.blit(line2,(65,185))
        screen.blit(line3,(65,195))
        screen.blit(line4,(65,208))
        screen.blit(line5,(65,218))
        draw.rect(screen,RED,ellipseRect,2)

    if tool=="polygon":
        draw.rect(screen,WHITE,textRect)
        draw.rect(screen,LILAC,textRect,2)
        line1=font.render("Polygon",True,BLACK)
        line2=font.render("-polyester",True,PLUM)
        line3=font.render("-left click to",True,PLUM)
        line4=font.render("make points,",True,PLUM)
        line5=font.render("right click to",True,PLUM)
        line6=font.render("close polygon",True,PLUM)
        screen.blit(line1,(75,165))
        screen.blit(line2,(65,185))
        screen.blit(line3,(65,198))
        screen.blit(line4,(65,208))
        screen.blit(line5,(65,218))
        screen.blit(line6,(65,228))
        draw.rect(screen,RED,drawpolyRect,2)

    if tool=="clear":
        draw.rect(screen,WHITE,textRect)
        draw.rect(screen,LILAC,textRect,2)
        line1=font.render("Clear",True,BLACK)
        line2=font.render("-a fresh",True,PLUM)
        line3=font.render("start",True,PLUM)
        line4=font.render("(only for",True,PLUM)
        line5=font.render("the canvas)",True,PLUM)
        screen.blit(line1,(75,165))
        screen.blit(line2,(65,185))
        screen.blit(line3,(65,195))
        screen.blit(line4,(65,208))
        screen.blit(line5,(65,218))
        draw.rect(screen,RED,clearRect,2)
        
    if tool=="undo":
        draw.rect(screen,WHITE,textRect)
        draw.rect(screen,LILAC,textRect,2)
        line1=font.render("Undo",True,BLACK)
        line2=font.render("-fixes bigger",True,PLUM)
        line3=font.render("mistakes",True,PLUM)
        screen.blit(line1,(75,165))
        screen.blit(line2,(65,185))
        screen.blit(line3,(65,198))
        draw.rect(screen,RED,undoRect,2)
        
    if tool=="redo":
        draw.rect(screen,WHITE,textRect)
        draw.rect(screen,LILAC,textRect,2)
        line1=font.render("Redo",True,BLACK)
        line2=font.render("-for mistakes",True,PLUM)
        line3=font.render("on mistakes",True,PLUM)
        screen.blit(line1,(75,165))
        screen.blit(line2,(65,185))
        screen.blit(line3,(65,195))
        draw.rect(screen,RED,redoRect,2)

    if tool=="open":
        draw.rect(screen,WHITE,textRect)
        draw.rect(screen,LILAC,textRect,2)
        line1=font.render("Open",True,BLACK)
        line2=font.render("-continues",True,PLUM)
        line3=font.render("past projects",True,PLUM)
        screen.blit(line1,(75,165))
        screen.blit(line2,(65,185))
        screen.blit(line3,(65,195))
        draw.rect(screen,RED,openRect,2)

    if tool=="save":
        draw.rect(screen,WHITE,textRect)
        draw.rect(screen,LILAC,textRect,2)
        line1=font.render("Save",True,BLACK)
        line2=font.render("-keeps your",True,PLUM)
        line3=font.render("art safe",True,PLUM)
        screen.blit(line1,(75,165))
        screen.blit(line2,(65,185))
        screen.blit(line3,(65,195))
        draw.rect(screen,RED,saveRect,2)
        
    if tool=="decoration":
        draw.rect(screen,WHITE,textRect)
        draw.rect(screen,LILAC,textRect,2)
        line1=font.render("Decorations",True,BLACK)
        line2=font.render("-prettifies",True,PLUM)
        line3=font.render("the cakes",True,PLUM)
        line4=font.render("-scroll for",True,PLUM)
        line5=font.render("more options",True,PLUM)
        screen.blit(line1,(75,165))
        screen.blit(line2,(65,185))
        screen.blit(line3,(65,195))
        screen.blit(line4,(65,208))
        screen.blit(line5,(65,218))
        draw.rect(screen,RED,decoRect,2)
        
    if tool=="cake":
        draw.rect(screen,WHITE,textRect)
        draw.rect(screen,LILAC,textRect,2)
        line1=font.render("Cakes",True,BLACK)
        line2=font.render("-helps your",True,PLUM)
        line3=font.render("cake craving",True,PLUM)
        line4=font.render("-scroll for",True,PLUM)
        line5=font.render("more options",True,PLUM)
        screen.blit(line1,(75,165))
        screen.blit(line2,(65,185))
        screen.blit(line3,(65,195))
        screen.blit(line4,(65,208))
        screen.blit(line5,(65,218))
        draw.rect(screen,RED,cakeRect,2)
        
    if tool=="plate":
        draw.rect(screen,WHITE,textRect)
        draw.rect(screen,LILAC,textRect,2)
        line1=font.render("Plates",True,BLACK)
        line2=font.render("-keeps cakes",True,PLUM)
        line3=font.render("sanitary",True,PLUM)
        line4=font.render("-scroll for",True,PLUM)
        line5=font.render("more options",True,PLUM)
        screen.blit(line1,(75,165))
        screen.blit(line2,(65,185))
        screen.blit(line3,(65,195))
        screen.blit(line4,(65,208))
        screen.blit(line5,(65,218))
        draw.rect(screen,RED,plateRect,2)

    if tool=="background":
        draw.rect(screen,WHITE,textRect)
        draw.rect(screen,LILAC,textRect,2)
        line1=font.render("Background",True,BLACK)
        line2=font.render("-sets a nice",True,PLUM)
        line3=font.render("setting",True,PLUM)
        line4=font.render("-scroll for",True,PLUM)
        line5=font.render("more options",True,PLUM)
        screen.blit(line1,(75,165))
        screen.blit(line2,(65,185))
        screen.blit(line3,(65,195))
        screen.blit(line4,(65,208))
        screen.blit(line5,(65,218))
        draw.rect(screen,RED,backGRect,2)
        
    ##################################################################
    #mouse visability
        
    if mmouse=="up" and canvasRect.collidepoint(mx,my) and mb[0]==1: #while the mouse is being held down on the canvas and the mouse was up before
         screenBuff=screen.subsurface(canvasRect).copy() #for the stamps, the screen is copied when the mouse changes to "down"
         mmouse="down" #since the mouse is being held down, we set the variable as down
         mouse.set_visible(False) #and the cursor disapears
         
    if mmouse=="down" and canvasRect.collidepoint(mx,my) and mb[0]==0: #if the mouse was held down and is now up
        screenBuff=screen.subsurface(canvasRect).copy() #the screen is copied again for the stamps
        mmouse="up" #set the variable as up
        mouse.set_visible(True) #and the cursor appears again
        
    ###############################################################
    #using tools
        
    if canvasRect.collidepoint(mx,my) and mb[0]==1: #if the mouse is on the canvas and is left clicking
        screen.set_clip(canvasRect) #set that only the canvas can be changed
        
        if tool=="pencil": #if the tool is pencil
            draw.line(screen,col,(omx,omy),(mx,my)) #draw a line from a point that the mouse use to be to where it is now

        if tool=="eraser": #if the tool is eraser
            dx=mx-omx #get the distance from where the mouse use to be to where it is now, horzontaly and vertically
            dy=my-omy
            dist=int(sqrt(dx**2+dy**2)) #and find the distance using distance formula
            for i in range (1,dist+1): #and for the length of the distance
                dotX=int(omx+i*dx/dist) #1i is added to the old point to get another point on the line 
                dotY=int(omy+i*dy/dist)
                draw.circle(screen,WHITE,(dotX,dotY),markerR) #and circles are drawn on each point on the line, so the eraser tool doesn't have gaps when drawing quickly
                                                    #the variable of the radius is used to determine how big the circle is
                
        if tool=="marker":#if the tool is marker
            dx=mx-omx #the same thing with the eraser tool is done
            dy=my-omy
            dist=int(sqrt(dx**2+dy**2))
            for i in range (1,dist+1):
                dotX=int(omx+i*dx/dist)
                dotY=int(omy+i*dy/dist)
                draw.circle(screen,col,(dotX,dotY),markerR)
                
        if tool=="spray": #if the tool is spray paint
            for i in range (int(sprayR/4*3)): #I loop depending on how big the radius is, so if the radius is smaller, I would loop fewer times and more times if the radius is bigger
                rx=randint((sprayR+1)*(-1),sprayR+2) #a random x and y coord is taken, ranging from the radius plus one to the negative of raduis plus one
                ry=randint((sprayR+1)*(-1),sprayR+2)  #this is so the points form a square that is larger than a circle, and when the boundaries are made, only the ones that form a circle are used

                if (rx)**2+(ry)**2<sprayR**2: #so as long as the distance from the point to the centre of the circle is in the range of the radius, it is drawn 
                    screen.set_at((mx+rx,my+ry),col)   #this creates a circle of spray paint

        if tool=="line": #if the tool is line
            screen.blit(back,(200,150)) #as long as the mouse is still down, a picture of the canvas is blit so there is only one line and it will only stay once the mouse is lifted
            draw.line(screen,col,(lx,ly),(mx,my),lineT) #and a line is drawn from the point the mouse was pressed down to where the mouse is currently
            
        if tool=="bucket": #if the tool is fill
             fill(screen,mx,my,col) #the fill function is used
                
        if tool=="rectangle": #if the tool is rectangle
            screen.blit(back,(200,150)) #a picture of the canvas is blit, so there is only one rectangle
             #4 rectangles are drawn , one for each side, so the rectangle does not have empty corners
            
            if reT<2:#but if the width is 1 or 0, a normal rectangle is drawn
                draw.rect(screen,col,[start[0],start[1],mx-start[0],my-start[1]],reT)
                
            elif mx<start[0] and my<start[1]: #this is if the rectangle is drawn in the quadrant where the difference of coordinates and of the starting point and the mouse is negative
                draw.rect(screen,col,[start[0],start[1],mx-start[0],-reT]) #this rectangle starts at the starting point, the width is the coord of the starting point to the x coord of the mouse and the width is the negative thickness, the width and height both being negative draws the rectangle to the left
                draw.rect(screen,col,[start[0],start[1],-reT,my-start[1]]) #this rectangle starts at the starting point and the width is now the negative thickness and the height is the distance of the y coord of the mouse to the starting point
                draw.rect(screen,col,[start[0]+mx-start[0]+reT,start[1],-reT,my-start[1]]) #this rectangle starts at how far the x coord of the mouse is from the start and the y coord of the starting point,the width is the negative thickness and the height is the distance of the y coord from the starting point
                draw.rect(screen,col,[start[0],start[1]+my-start[1]+reT,mx-start[0],-reT]) #this rectangle starts at the x coord of the starting point and the distance of the y coord of the mouse from the start, the width is the distance of the x coord of the mouse from the start and the height is the negative height
            else:
                draw.rect(screen,col,[start[0],start[1],mx-start[0],reT]) #these are drawn in the same way, but the height and width are positive
                draw.rect(screen,col,[start[0],start[1],reT,my-start[1]])
                draw.rect(screen,col,[start[0]+mx-start[0]-reT,start[1],reT,my-start[1]])
                draw.rect(screen,col,[start[0],start[1]+my-start[1]-reT,mx-start[0],reT])

        if tool=="ellipse": #if the tool is ellipse
            screen.blit(back,(200,150)) #the canvas is blit before drawing a new ellipse
            ellRect=Rect(start[0],start[1],mx*1.05-start[0],my*1.05-start[1]) #the coordinates of where the mouse currently is is taken and the rectangle used to draw the ellipse is normalized
            ellRect.normalize()
            
            #try and except: pass are used because the program will crash if the width is greater than the radius
            try:
                draw.ellipse(screen,col,ellRect,reT) #first we draw the ellipse
            except:
                pass
            
            if reT>1: #if the thickness is more than 1 , 4 more of the same ellipse, one pixel above, one pixel under, one pixel left and one pixel right are drawn to fill in the gaps
                ellRect=Rect(start[0]+1,start[1],mx*1.05-start[0],my*1.05-start[1])
                ellRect.normalize()
                try:
                    draw.ellipse(screen,col,ellRect,reT)
                except:
                    pass
                ellRect=Rect(start[0]-1,start[1],mx*1.05-start[0],my*1.05-start[1])
                ellRect.normalize()
                try:
                    draw.ellipse(screen,col,ellRect,reT)
                except:
                    pass
                ellRect=Rect(start[0],start[1]+1,mx*1.05-start[0],my*1.05-start[1])
                ellRect.normalize()
                try:
                    draw.ellipse(screen,col,ellRect,reT)
                except:
                    pass
                ellRect=Rect(start[0],start[1]-1,mx*1.05-start[0],my*1.05-start[1])
                ellRect.normalize()
                try:
                    draw.ellipse(screen,col,ellRect,reT)
                except:
                    pass
                
        screen.set_clip(None)#be able to modify entire screen after we're finished


    if canvasRect.collidepoint(mx,my): #for the polygon tool, I only need one point added to the list at a time, I use clicked, if I were to use mb[0]==1, then multiply points for one vertex would be appended to the list of points
        screen.set_clip(canvasRect) #only be able to modify the canvas again
        if tool=="polygon": #if the tool is polygon
            if clicked: #and the mouse was clicked
                polyPoints.append((mx,my)) #that point is appended into the list
            
            if len(polyPoints)>0: #as long as there is 1 point in the list
                if polyT==0: #if the thickness of the polygon is 0, a thickness 1 line still needs to be drawn
                    screen.blit(back,(200,150))
                    draw.line(screen,col,polyPoints[-1],(mx,my),1)
                else:
                    screen.blit(back,(200,150)) #if the thickness is not 0, a line from that point to the current position of the mouse is drawn, with the thickness of the polygon
                    draw.line(screen,col,polyPoints[-1],(mx,my),polyT)
            
        screen.set_clip(None) #be able to modify the entire screen after we are finished
        
    if rightClicked and tool=="polygon": #draws the polygon after the user right clicks after making vertices 
        try: #in case there are not enough points in the list and the user right clicks
            draw.polygon(screen,col,polyPoints,polyT) 
        except:
            pass
        polyPoints=[] #after drawing the polygon, the list is empty
        
    ##############################################################
    #stamps

    if mmouse=="down": #while the mouse is being held down
        screen.set_clip(canvasRect) #set that only the canvas is able to be changed
        
        if tool=="decoration": #if the tool is decoration
            sx=decoPics[decoPos].get_width() #the height and width of the current decoration is taken
            sy=decoPics[decoPos].get_height()
            screen.blit(screenBuff,(200,150)) #screenBuff is blit so only one stamp is there at a time
            screen.blit(decoPics[decoPos],(mx-int(sx/2),my-int(sy/2))) #the stamp is blit to where the mouse is, it will continue to until the mouse is released
            #when the mouse is released, the pic of the one stamp on the screen will stay
            
        if tool=="cake": #same thing for the cake and plate stamps
            sx=cakePics[cakePos].get_width()
            sy=cakePics[cakePos].get_height()
            screen.blit(screenBuff,(200,150))
            screen.blit(cakePics[cakePos],(mx-int(sx/2),my-int(sy/2)))
            
        if tool=="plate":
            sx=platePics[platePos].get_width()
            sy=platePics[platePos].get_height()
            screen.blit(screenBuff,(200,150))
            screen.blit(platePics[platePos],(mx-int(sx/2),my-int(sy/2)))
        screen.set_clip(None) #set that the rest of the screen can be modified again
        
    ###############################################################
    #selecting position/thickness
        
    if scrollUp: #if the user is scrolling up
        if tool=="marker" or tool=="eraser": #if the tool is marker or eraser
            if markerR<100: #if the marker/eraser radius is less than 100 
                markerR+=1 #1 is added to the radius variable 

        if tool=="spray"and sprayR<100: #if the spray radius is not 100 and the tool is spray 
            sprayR+=1 #1 is added to the spray radius variable

        if lineT<100 and tool=="line": #if the line thickness is not 100 and the tool is line
            lineT+=1 #1 is added

        if tool=="rectangle" or tool=="ellipse": #if the tool is rectangle or ellipse
            if 0<reT<50: #if the thickness is bigger than 0 and less than 50 
                reT+=1 #1 is added
            if reT==50: #if the thickness is 50 and the user wants the rectangle thicker, the rectangle thickness is set to 0; filled
                reT=0

        if tool=="polygon": #if the tool is polygon
            if 0<polyT<30: #if the thickness is between 0 and 30
                polyT+=1 #we add 1
            if polyT==30: #if the thickness is 30 and the user wants it to be thicker, the polygon thickness is set to 0; filled
                polyT=0
                
        if tool=="decoration": #if the tool is decoration
            draw.rect(screen,WHITE,decoRect) #the rectangle that displays the stamps is redrawn 
            draw.rect(screen,RED,decoRect,2)
            if decoPos<9: #if the position of the decorations is less than 9
                decoPos+=1 #1 is added to the position
                screen.blit(decoPics[decoPos],(864,270)) #and that picture is blit into the display box
            else: #if it is 9, the position is set back to 0 and the picture of that position is blit in the box
                decoPos=0
                screen.blit(decoPics[0],(864,270))     
        #and repeat for the cakes, plates and backgrounds with their number of stamps

        if tool=="cake":
            draw.rect(screen,WHITE,cakeRect)
            draw.rect(screen,RED,cakeRect,2)
            if cakePos<5:
                cakePos+=1
                screen.blit(cakeIcons[cakePos],(849,400))
            else:
                cakePos=0
                screen.blit(cakeIcons[0],(849,400))

        if tool=="plate":
            draw.rect(screen,WHITE,plateRect)
            draw.rect(screen,RED,plateRect,2)
            if platePos<4:
                platePos+=1
                screen.blit(plateIcons[platePos],(839,560))
            else:
                platePos=0
                screen.blit(plateIcons[0],(839,560))
                
        if tool=="background": #except for beckgrounds, the white box and outline are not needed
            if backGPos<2:
                backGPos+=1
                screen.blit(backGIcons[backGPos],(849,650))
                draw.rect(screen,RED,backGRect,2)
            else:
                backGPos=0
                screen.blit(backGIcons[0],(849,650))
                draw.rect(screen,RED,backGRect,2)

    if scrollDown: #if the user is scrolling down
        if tool=="marker" or tool=="eraser": #if the tool is eraser or marker 
            if markerR>10: #if the raduis variable is above the minimum
                markerR-=1 #1 is subtracted from the radius variable
            
        if tool=="line" and lineT>1: #if the tool is line and the line thickness variable is bigger than 1
            lineT-=1 #1 is subtracted
            
        if tool=="spray" and sprayR>20: #if the tool is spray and the radius variable is above 10
            sprayR-=1 #1 is subtracted
            
        if tool=="rectangle" or tool=="ellipse": #if the tool is rectangle or ellipse
            if reT>1: #if the thickness variable is above one 
                reT-=1 #1 is subtracted
            elif reT==0: #or if the thickness is 'filled' the variable is set to the largest thickness; 50
                reT=50
        if tool=="polygon": #if the tool is polygon
            if polyT>1: #if the thickness variable is above 1
                polyT-=1 #1 is subtracted
            elif polyT==0: #or if the thickness is 'filled', the variable is set to the largest thickness; 30
                polyT=30
        if tool=="decoration": #if the tool is decoration
            draw.rect(screen,WHITE,decoRect) #the display box is redrawn
            draw.rect(screen,RED,decoRect,2)
            
            if decoPos>0: #if the position variable is above 0
                decoPos-=1 #1 is subtracted from the position 
                screen.blit(decoPics[decoPos],(864,270)) #and the icon of that position is blit into the display box
            else: #or if the position is 0
                decoPos=9 #the position is set to 9 
                screen.blit(decoPics[9],(864,270)) #and the icon of that position is blit into the display box
         #repeat with the cakes, plates and background with their respective position variables and values       

        if tool=="cake":
            draw.rect(screen,WHITE,cakeRect)
            draw.rect(screen,RED,cakeRect,2)
            if cakePos>0:
                cakePos-=1
                screen.blit(cakeIcons[cakePos],(849,400))
            else:
                cakePos=5
                screen.blit(cakeIcons[5],(849,400))
                
        if tool=="plate":
            draw.rect(screen,WHITE,plateRect)
            draw.rect(screen,RED,plateRect,2)
            if platePos>0:
                platePos-=1
                screen.blit(plateIcons[platePos],(839,560))
            else:
                platePos=4
                screen.blit(plateIcons[0],(839,560))

        if tool=="background": #except the backgrounds don't need another white box or new outline
            if backGPos>0:
                backGPos-=1
                screen.blit(backGIcons[backGPos],(849,650))
                draw.rect(screen,RED,backGRect,2)
            else:
                backGPos=2
                screen.blit(backGIcons[2],(849,650))
                draw.rect(screen,RED,backGRect,2)
        
    ########################################################## 
    #position
    
    draw.rect(screen,WHITE,(100,719,65,19)) #draws a white box that covers the (x,y) coordinate so a new one can be blit there
    position=font.render(str(mx)+","+str(my),True,BLACK) #a font is rendered that displays the current position of the mouse in the form of x,y
    screen.blit(position,(100,720)) #and the text is blit into the position box

    ###############################################################
    #size display

    #for some tools, they have a variable that has the size/thickness of that tool
    #so for each tool that has such a variable, if the user is using a tool that has size/thickness the size is displayed in the size/thickness rectangle
    draw.rect(screen,WHITE,(136,740,38,22))

    if tool=="eraser" or tool=="marker":
        size=font.render(str(markerR),True,BLACK)
        screen.blit(size,(137,742))
    elif tool=="spray":
        size=font.render(str(sprayR),True,BLACK)
        screen.blit(size,(137,742))
    elif tool=="line":
        size=font.render(str(lineT),True,BLACK)
        screen.blit(size,(137,742))
    elif tool=="rectangle" or tool=="ellipse":
        if reT==0:                                  #for rectangle, ellipse and polygon, since 0 is filled, 'filled' is blit instead of the number 0
            size=font.render("filled",True,BLACK) 
        else:
            size=font.render(str(reT),True,BLACK)
        screen.blit(size,(137,742))
    elif tool=="polygon":
        if polyT==0:
            size=font.render("filled",True,BLACK)
        else:
            size=font.render(str(polyT),True,BLACK)
        screen.blit(size,(137,742))
                                             #if the user is not using a tool with a size/thickness, the white box drawn at the beginning will stay, displaying nothing

        
    ###############################################################
    #change colour
            
    if paletteRect.collidepoint(mx,my) and clicked: #if the palette was clicked on
        col=screen.get_at((mx,my)) #the colour at the position of the mouse is and the colour variable is set as the that colour
        draw.rect(screen,col,currentColRect) #and the current colour rectangle is drawn as that colour

    omx,omy=mx,my #for the pencil, eraser and marker tool, the current position of the mouse that may be used in the next loop
    display.flip() #displays everything done
    myClock.tick(60) #how many times loop runs in a second


quit() #closing the pygame window







    
