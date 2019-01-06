import turtle
points = [[-175,-125],[0,175],[175,-125]] #size of triangle

def getMidle(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

def draw_frac_triangle(myPen, points,depth):
   
    myPen.up()
    myPen.goto(points[0][0],points[0][1])
    myPen.down()
    myPen.goto(points[1][0],points[1][1])
    myPen.goto(points[2][0],points[2][1])
    myPen.goto(points[0][0],points[0][1])

    if depth>0:
        draw_frac_triangle(myPen, [points[0],getMidle(points[0], points[1]),
                        getMidle(points[0], points[2])],depth-1)
        draw_frac_triangle(myPen, [points[1],getMidle(points[0], points[1]),
                        getMidle(points[1], points[2])], depth-1)
        draw_frac_triangle(myPen, [points[2],getMidle(points[2], points[1]),
                         getMidle(points[0], points[2])],depth-1)
     
window  = turtle.Screen()
myPen = turtle.Turtle()
myPen.speed(50)
myPen.color("#000000")
draw_frac_triangle(myPen, points,4)
window.exitonclick() 