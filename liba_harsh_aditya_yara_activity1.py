import turtle

turtle.speed(10000) 

'''defines function for left front and back legs with different lengths for each'''
def rectangleleft(x,y,height,length): 
    turtle.penup() 
    turtle.goto(x,y) 
    turtle.pendown() 
    turtle.forward(length//2)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward((length//2)+1)

'''defines function for right front and back leg with different lengths'''
def rectangleright(x,y,height,length):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.forward(length//2)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward((length//2)+1)

'''define circle for cherry'''
def circle(x,y,radius): 
    turtle.penup()
    turtle.goto(x,y)
    turtle.down()
    turtle.circle(radius)


'''table top using function for rectangleleft and symmetrical position for legs '''
def table(tableheight,tablelength,color): 
    halftable=tablelength//2 
    turtle.fillcolor(color)
    turtle.pencolor(color)
    turtle.begin_fill()
    rectangleleft(0,0,tableheight,tablelength) 
    turtle.end_fill()
    turtle.begin_fill()
    rectangleright((halftable)-20,0,tablelength//2,tableheight) 
    turtle.end_fill()
    turtle.begin_fill()
    rectangleright((-(halftable))+20,0,tablelength//2,tableheight) 
    turtle.end_fill()
    turtle.begin_fill()
    rectangleright(((halftable)-20) - (tableheight+10),0,tablelength//3,tableheight) 
    turtle.end_fill()
    turtle.begin_fill()
    rectangleright(((-(halftable))+20) +(tableheight+10),0,tablelength//3,tableheight) 
    turtle.end_fill()
    turtle.penup()

'''function for cake using rectangleleft from above and adjusting height for each layer to be visible'''
def cake(height, length, color1, color2, color3, tableheight):
    turtle.fillcolor(color1) 
    turtle.pencolor(color1)
    turtle.begin_fill()
    rectangleleft(0, tableheight, height // 3, length) 
    turtle.end_fill()
    turtle.penup()
    turtle.pendown() 
    turtle.fillcolor(color2)
    turtle.pencolor(color2)
    turtle.begin_fill()
    rectangleleft(0, tableheight + height // 3, height // 3, length/1.25)
    turtle.end_fill()
    turtle.fillcolor(color3)
    turtle.pencolor(color3)
    turtle.begin_fill()
    rectangleleft(0, tableheight + (2 * height // 3), height // 3, length/1.8)
    turtle.end_fill()

'''cherry function mentioning cake height so its at the very top'''
def cherry(cakeheight): 
    turtle.fillcolor('red')
    turtle.pencolor('red')
    turtle.begin_fill()
    circle(0,cakeheight,4) 
    turtle.end_fill()

'''semicircle function for frosting'''
def semicircle(x,y,radius):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.right(90)
    turtle.fillcolor('white')
    turtle.pencolor('white')
    turtle.begin_fill()
    turtle.circle(radius,180)
    turtle.right(180)
    turtle.circle(radius,180)
    turtle.right(180)
    turtle.circle(radius,180)
    turtle.right(180)
    turtle.circle(radius,180)
    turtle.right(180)
    turtle.circle(radius,180)
    turtle.right(180)
    turtle.end_fill()

'''calling semi circle for frosting'''
def decoration(cakeheight,cakelength):
    semicircle(-cakelength//2, cakeheight ,cakelength//10)

'''candle function using rectangle from above and adjusting size by -/+ 45'''
def candle(height,length):
    x=length//2
    turtle.fillcolor('orange')
    turtle.pencolor('orange')
    turtle.begin_fill()
    turtle.left(90)
    rectangleleft(x-45,height,height//4,10) 
    rectangleleft((-x)+45,height,height//4,10) 
    turtle.end_fill()

'''function for fire with side and center adjustments'''
def fire(height,length):
    turtle.fillcolor('red')
    turtle.pencolor('red')
    turtle.begin_fill()
    circle((length//2)-45,height+height//4,3)
    turtle.end_fill()
    turtle.begin_fill()
    circle(-(length//2)+45,height+height//4,3)
    turtle.end_fill()

'''main function where all other functions are called'''
def main():
    turtle.bgcolor('lavender')
    table_height=int(input('Enter table height between 10 and 15: '))
    table_length=int(input('Enter table length between 180 and 200: '))
    table_color=input('Enter the table color: ')
    len=str(table_length-20)
    cakelengthinput='Enter cake length between 140 and '+len+': ' 
    cake_height=int(input('Enter the cake height between 100 and 150: '))
    cake_length=int(input(cakelengthinput))
    layer1=input('Enter the color of first layer of the cake: ')
    layer2=input('Enter the color of second layer of the cake: ')
    layer3=input('Enter the color of third layer of the cake: ')

    table(table_height,table_length,table_color)
    cake(cake_height,cake_length,layer1,layer2,layer3,table_height)
    cherry(cake_height+table_height)
    decoration(cake_height+table_height,cake_length/1.8)
    candle(cake_height+table_height,cake_length)
    fire(cake_height+table_height,cake_length)

    turtle.penup()
    turtle.goto(0,0)
    input("your cake is loading! happy birthday")
    input("enter to exit")
main() 