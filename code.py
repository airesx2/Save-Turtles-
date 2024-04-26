#imports
import turtle as text
import turtle as trtl
import random as rand
# Order:(funcs, variables, function calling, mainloop)

#-------- FUNCTIONS -----------

#starting questions
# change below function to take in a parameter that is used in the function in someway (if statement)
def starter():
  global sea
  sea = input("Do you like the sea?")
  if(sea == 'yes'):
    print(":)")
  else:
    print(":(")
  

def para(sea):
  if sea == 'yes':
    liketurtle = input("Do you like turtles?")
    sea = 'done'
  else: 
    quit()
  if(liketurtle == "yes"):
    print("Help save Sea Turtles! :D")
  else:
    for i in range(100):
      print("Sea Turtles are endangered :(")
    
  
  #saveturtles text colorinput
  while True: 
    pickcolor = input("what color are the sea turtles?")  
  
    if pickcolor in color_list:
      saveturtles_color = pickcolor.lower()
      break # leave while loop
  
    print ("that's plastic, choose again...")

  cover_save(color_list) 
  
   

# Cover Design/Text
def cover_save(color_list):
    #Name Input
    name = input("Name?")
    #Random Text color
    text_color = rand.choice(color_list) 
    #Font Setup
    font_setup = ('Monaco',70)
    text.color(str(text_color)) 

    #"up to you" text displace
    text.pu() 
    text.goto(-600,150)
    text.pd()
    text.write("It's up to you, " + str(name) +  '\n ' + 'to save the Sea Turtle!', font = font_setup)
    text.hideturtle()

#Cover Image
def cover_app(cover, cover_trtl):
  cover_trtl.shape(cover)
  wn.update()
  
#Bubbles Flash
def bubbles():
  bubbles = 'bubbles.gif'
  for i in range (100):
    wn.addshape(bubbles)
    sparkle = trtl.Turtle(shape=bubbles)
    sparkle.hideturtle()

#Print saveturtles
def saveturtles(x,y):
  saveturtles = trtl.Turtle()
  saveturtles.hideturtle()
  saveturtles.color(saveturtles_color)
  saveturtles.penup()
  saveturtles.goto(x,y)
  saveturtles.pendown()
  saveturtles.write('Save the Sea Turtles!')
  
#turtles/nostraw movement
def turtle_straw():
  #turtle
  turtle = 'turtle.gif'
  wn.addshape(turtle)
  turt = trtl.Turtle(turtle)
  turt.penup()
  i=0
  turt.goto(-300,-100)
  #nostraw
  straw = 'nostraw.gif'
  wn.addshape(straw)
  nostraw = trtl.Turtle(straw)
  nostraw.penup()
  nostraw.goto(-650,300)

  #movement loop
  while(i==0):
    turt.setheading(270)
    turt.forward(50)
    turt.setheading(-270)
    turt.forward(50)
    nostraw.setheading(270)
    nostraw.forward(50)
    nostraw.setheading(-270)
    nostraw.forward(50)

#Inside Image 
def inside(x,y):
  #inside_image
  Inside = 'Inside.gif'
  wn.addshape(Inside)
  inside_trtl = trtl.Turtle(Inside)
  def inside_app(Inside):
    inside_trtl.shape(Inside)
    wn.update()
  cover_trtl.hideturtle()
  inside_app(Inside)
  inside_trtl.penup()
  inside_trtl.goto(350,-150)

  turtle_straw()

# ------- VARIABLES -------
color_list = ['red','orange','green','yellow','light blue','purple','pink','brown','black','white']
bg_color = 'blue'
saveturtles_color = 'yellow'

wn = trtl.Screen()
wn.bgcolor(bg_color)


#--------- FUNCTION CALLINGS -------
starter() #put something in the ()
para(sea)

#cover image
cover = 'Front.gif' 
wn.addshape(cover)
cover_trtl = trtl.Turtle()

#cover_app
cover_app(cover, cover_trtl)
cover_trtl.showturtle()
cover_trtl.penup()
cover_trtl.goto(100,-100)

bubbles()

#onclicks
wn.onscreenclick(saveturtles)
cover_trtl.onclick(inside)


#--------mainloop---------
mainloop = wn.mainloop()
