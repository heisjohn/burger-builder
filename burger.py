import turtle
import time
import random
 
 
validIngredients = ["patty", "cheese", "tomato", "lettuce",
                    "pickles", "onions", "ketchup", "mustard", "mayonnaise"]
isFinishedMakingBurger = False
 
wn = turtle.Screen()
wn.title("BURGER BUILDER")
wn.setup(width = 800, height = 800)
 
backdrop = turtle.Turtle()
backdrop.ht()
backdrop.up()
 
pen = turtle.Turtle()
pen.speed("fastest")
pen.width(5)
buttonCoordinates = [(150, 335, "patty", "saddlebrown"), (150, 265, "cheese", "yellow"),
                     (150, 195, "lettuce", "#77AA11"), (150, 125, "pickles", "olivedrab"),
                     (150, 55, "onions", "whitesmoke"), (150, -15,"tomato","firebrick"),
                     (150, -85, "mustard", "gold"), (150, -155, "ketchup", "darkred"),
                     (150,-225, "mayonnaise", "lightyellow"), (150, -295, "delete", "white"),
                     (150, -365, "finished?", "white")]
 
listwriter = turtle.Turtle()
 
detector = turtle.Turtle()
detector.up()
detector.speed("fastest")
 
listwriter.ht()
detector.ht()
pen.ht()
 
def compareLists1(list1, list2):
    ingredients = ["patty", "cheese", "tomato", "lettuce",
                    "pickles", "onions", "ketchup", "mustard", "mayonnaise"]
    list1Count = []
    list2Count = []
 
    for x in ingredients:
        list1Count.append(list1.count(x))
    for y in ingredients:
        list2Count.append(list2.count(y))
 
    score = 0
    for i in range(len(list1Count)):
        score += abs(list1Count[i] - list2Count[i])
    return score
 
def compareLists2(list1, list2):
    difference = len(list1) - len(list2)
    
    if abs(difference) > 3:
        if difference > 0:
            difference = 3
        else:
            difference = -3
    score = 0
 
    for i in range(len(list1)):
        isSuccess = False
        minimum = i
        maximum = i
        
        if difference > 0:
            minimum = i - difference
        if difference < 0:
            maximum = i - difference
            
        if minimum < 0:
            mimimum = 0
        if maximum >= len(list2):
            maximum = len(list2)-1
 
        for j in range(minimum, maximum +1):
            if list1[i] == list2[j]:
                isSuccess = True
 
        if not isSuccess:
            score += 1
 
    return score
 
def buttonClick(x,y, detector, buttonCoordinates, burgerList):
    for coor in buttonCoordinates:
        if x > coor[0] and x < coor[0] + 200 and y > coor[1] and y < coor[1] + 50:
            if coor[2] == "finished?":
                return True
            elif coor[2] == "delete" and not burgerList[len(burgerList)-2] == "bun":
            
                burgerList.pop(len(burgerList)-2)
            elif not coor[2] == "delete":
                burgerList.insert(len(burgerList) - 1, coor[2])
    detector.goto(-300,-300)
    return False
 
def buttonClick2(x,y,detector, coor):
    if x > coor[0] and x < coor[0] + 200 and y > coor[1] and y < coor[1] + 50:
        return True
    detector.goto(-600,-600)
    return False
 
def buttonClick3(x,y,detector, buttonList):
    for coor in buttonList:
        if x > coor[0] and x < coor[0] + 200 and y > coor[1] and y < coor[1] + 50:
            return coor[2]
    detector.goto(-300,-300)
    return 0
    
def writeList(x,y,turtle, burgerList, text):
    turtle.up()
    burgerString = text
    for i in range(len(burgerList)-1, -1, -1):
        burgerString += str(len(burgerList)-(i)) + ". " + burgerList[i] + "\n"
 
    turtle.goto(x,y-len(burgerList) * 16)
    turtle.down()
    turtle.write(burgerString, align = "center", font = ("Comic Sans MS",12,"normal"))
    turtle.up()
 
def drawButton(x,y,turtle, color, name):
    turtle.seth(0)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.width(4)
    turtle.begin_fill()
    turtle.color("black")
    for i in range(2):
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(50)
        turtle.left(90)
    turtle.color(color)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(x+100, y+16)
    turtle.color("black")
    turtle.write(name,align="center",font=("Comic Sans MS",18,"normal"))
 
def createSeeds(x,y,turtle):
    turtle.shape("circle")
    turtle.color("white")
    turtle.shapesize(.35,.15,.25)
    turtle.penup()
    for i in range(90):
        turtle.seth(random.randint(0,360))
        turtle.goto(x + random.randint(-150,150), y + random.randint(0,60))
        turtle.stamp()
 
def createTopBun(x, y, turtle):
    turtle.up()
    turtle.setheading(0)
    turtle.color("#cc9944")
    turtle.goto(x,y)
    turtle.down()
    turtle.begin_fill()
    turtle.forward(300)
    turtle.left(90)
    turtle.forward(40)
 
    turtle.seth(150)
    for i in range(60):
        turtle.left(.97)
        turtle.forward(5.215)
        
    turtle.goto(x,y)
    turtle.end_fill()
    createSeeds(x+150,y+20,turtle)
    return 53
 
def createBottomBun(x,y,turtle):
    turtle.up()
    turtle.setheading(0)
    turtle.color("#cc9944")
    turtle.goto(x+15,y)
    turtle.down()
    turtle.begin_fill()
    turtle.forward(270)
    turtle.left(90)
    turtle.forward(40)
 
    for i in range(135):
        turtle.seth(180)
        turtle.forward(2)
        turtle.seth(90)
        turtle.forward(-(i-67.5)/160)
        
    turtle.goto(x+15,y)
    turtle.end_fill()
    return 47
 
def createPatty(x, y, turtle):
    turtle.up()
    turtle.setheading(0)
    turtle.color("saddlebrown")
    turtle.goto(x,y)
    turtle.down()
    turtle.begin_fill()
    turtle.forward(300)
    turtle.left(90)
    turtle.forward(25)
 
    turtle.seth(150)
    for i in range(60):
        turtle.left(.97)
        turtle.forward(5.215)
        
    turtle.goto(x,y)
    turtle.end_fill()
    return 38
 
def createLettuce(x, y, turtle):
    turtle.up()
    turtle.goto(x,y+5)
    turtle.color("#77AA11")
    turtle.shape("circle")
    turtle.shapesize(1.5,3)
 
    for i in range(75):
        turtle.up()
        turtle.setheading(random.randint(0,360))
        turtle.goto(x+random.randint(10,290), y+random.randint(0,12))
        turtle.down()
        turtle.stamp()
    turtle.shapesize(1/1.5,1/3)
    turtle.ht()
    return 20
    
def createCondiment(x,y,condimentName, turtle):
    if condimentName == 'mayonnaise':
        turtle.color("lightyellow")
    if condimentName == "ketchup":
        turtle.color("darkred")
    if condimentName == "mustard":
        turtle.color("gold")
    turtle.up()
    turtle.shape("circle")
    turtle.setheading(0)
    for i in range(25):
        w = random.randint(30,40)/10
        turtle.up()
        turtle.shapesize(1,w)
        
        turtle.goto(x+random.randint(40,260), y+random.randint(0,15))
        turtle.down()
        turtle.stamp()
        turtle.shapesize(1,1/w)
    return 10
 
def createCheese(x,y, turtle):
    turtle.up()
    
    turtle.color("yellow")
    
    turtle.goto(x+170,y-15)
    turtle.down()
    turtle.begin_fill()
    turtle.goto(x+310,y+8)
    turtle.goto(x+130,y+30)
    turtle.goto(x-10,y+10)
    turtle.goto(x+170,y-15)
    turtle.end_fill()
    return 10
 
def createTomato(x,y,turtle):
    turtle.up()
    turtle.setheading(0)
    turtle.color("darkred")
    turtle.goto(x+10,y)
    turtle.down()
    turtle.begin_fill()
    turtle.forward(280)
    turtle.left(90)
    turtle.forward(10)
    
    for i in range(70):
        turtle.seth(180)
        turtle.forward(4)
        turtle.seth(90)
        turtle.forward((35-i)/25)
        
    turtle.goto(x+10,y)
    turtle.color("firebrick")
    turtle.end_fill()
    return 17
 
def createOnions(x,y,turtle):
    turtle.up()
    
    pen.width(8)
    turtle.color("whitesmoke")
    turtle.down()
    for j in range(1,4):
        pen.up()
        turtle.goto(x + 10 + (j-1)*(random.randint(55,65)),y+random.randint(-5,10))
        pen.down()
        for i in range(40):
            turtle.seth(0)
            turtle.forward(4)
            turtle.seth(90)
            turtle.forward((20-i)/10)
        for i in range(40):
            turtle.seth(180)
            turtle.forward(4)
            turtle.seth(270)
            turtle.forward((20-i)/10)
 
    pen.width(5)
    return 3
 
def createPickles(x,y, turtle):
    turtle.up()
    turtle.goto(x,y)
    turtle.shape("circle")
    
    turtle.setheading(0)
    for i in range(50,300,50):
        turtle.up()
        turtle.goto(x+i, y+random.randint(-10,10))
        turtle.color("olivedrab")
        turtle.shapesize(1.8,4.4)
        turtle.stamp()
        turtle.shapesize(1/1.8,1/4.4)
        turtle.shapesize(1.5,4.1)
        turtle.color("yellowgreen")
        turtle.stamp()
    turtle.shapesize(1/2,1/4)
    turtle.ht()
    return 5
 
def createBurger(burgerList, x, height, pen, delay):
    if not delay == 0:
        wn.update()
        time.sleep(delay)
    height = height + createBottomBun(x,height,pen)
    if not delay == 0:
        wn.update()
        time.sleep(delay)
    for i in range(1, len(burgerList)-1):
        if burgerList[i] == "patty":
            height = height + createPatty(x,height,pen)
        if burgerList[i] == "cheese":
            height = height + createCheese(x,height,pen)
        if burgerList[i] == "tomato":
            height = height + createTomato(x,height,pen)
        if burgerList[i] == "lettuce":
            height = height + createLettuce(x,height,pen)
        if burgerList[i] == "pickles":
            height = height + createPickles(x,height,pen)
        if burgerList[i] == "onions":
            height = height + createOnions(x,height,pen)
        if burgerList[i] == "ketchup" or burgerList[i] == "mustard" or burgerList[i] == "mayonnaise":
            height = height + createCondiment(x,height,burgerList[i],pen)
        if not delay == 0:
            wn.update()
            time.sleep(delay)
    height = height + createTopBun(x,height,pen)
    if not delay == 0:
        wn.update()
        time.sleep(delay)
 
def createRandomBurger(burgerList, pen):
    createTopBun(random.randint(-280,-110), random.randint(-100,50),pen)
    createBottomBun(random.randint(-280,-110), random.randint(-100,50),pen)
    for i in range(1, len(burgerList)-1):
        x = random.randint(-280,-110)
        y = random.randint(-100,50)
        if burgerList[i] == "patty":
            createPatty(x,y,pen)
        if burgerList[i] == "cheese":
            createCheese(x,y,pen)
        if burgerList[i] == "tomato":
            createTomato(x,y,pen)
        if burgerList[i] == "lettuce":
            createLettuce(x,y,pen)
        if burgerList[i] == "pickles":
            createPickles(x,y,pen)
        if burgerList[i] == "onions":
            createOnions(x,y,pen)
        if burgerList[i] == "ketchup" or burgerList[i] == "mustard" or burgerList[i] == "mayonnaise":
            createCondiment(x,y,burgerList[i],pen)
    pen.up()
 
def drawDivider(turtle):
    for i in range(2):
        turtle.goto(0,-400)
        turtle.down()
        turtle.width(4)
        turtle.goto(0,400)
        turtle.up()
        wn.update()
 
def main():
    burgerList = ["bun", "bun"]
    wn.tracer(0)
    listwriter.up()
    titleBurger = ["bun", "bun"]
 
    #title screen
 
    isFinishedViewing = False
 
    while not isFinishedViewing:
        titleBurger = ["bun", "bun"]
        wn.onclick(detector.goto)
        isFinishedViewing = buttonClick2(detector.xcor(), detector.ycor(), detector, (-100, -200))
        for i in range(random.randint(10,40)):
            ingredient = validIngredients[random.randint(0, len(validIngredients)-1)]
            while (titleBurger[1] == ingredient):
                ingredient = validIngredients[random.randint(0, len(validIngredients)-1)]
            titleBurger.insert(1, ingredient)
        createBurger(titleBurger,-150, -350, pen, 0)
        drawButton(-100, -200, pen, "white", "play")
        listwriter.goto(0,200)
        listwriter.color("black")
        listwriter.write("BURGER BUILDER", align = "center", font = ("Comic Sans MS",70,"bold"))
    
        wn.update()
        pen.clear()
        #detector.clear()
    
    time.sleep(0.2)
    wn.clear()
    detector.goto(-400,-400)
    listwriter.clear()
    
    wn.tracer(0)
 
    #difficulty screen
    difficulty = 0
    difficultyButtonList = [(-100, 200, 1, "easy"), (-100, 50, 2, "medium"),
                            (-100,-100,3, "hard"), (-100,-250,4, "impossible")]
 
    titleBurger = ["bun", "bun"]
    for i in range(60):
        ingredient = validIngredients[random.randint(0, len(validIngredients)-1)]
        while (titleBurger[1] == ingredient):
            ingredient = validIngredients[random.randint(0, len(validIngredients)-1)]
        titleBurger.insert(1, ingredient)
    createBurger(titleBurger,-150, -400, pen, 0)
 
    pen.down()
    pen.color("black")
    for i in difficultyButtonList:
        drawButton(i[0], i[1], pen, "white", i[3])
        
    while(difficulty == 0):
        wn.onclick(detector.goto)
        difficulty = buttonClick3(detector.xcor(), detector.ycor(), detector, difficultyButtonList)
        wn.update()
        #detector.clear()
 
    randomBurger = ["bun", "bun"]
 
    for i in range(random.randint(11*difficulty,11*difficulty + 5)):
        ingredient = validIngredients[random.randint(0, len(validIngredients)-1)]
        while (randomBurger[1] == ingredient):
            ingredient = validIngredients[random.randint(0, len(validIngredients)-1)]
        randomBurger.insert(1, ingredient)
 
    if difficulty == 4:
        randomBurger = ["bun", "bun"]
        for i in range(random.randint(15,20)):
            ingredient = validIngredients[random.randint(0, len(validIngredients)-1)]
            while (randomBurger[1] == ingredient):
                ingredient = validIngredients[random.randint(0, len(validIngredients)-1)]
            randomBurger.insert(1, ingredient)
            
    wn.clear()
    wn.tracer(0)
 
    if difficulty == 4:
        isFinishedViewing = False
        while not isFinishedViewing:
            wn.onclick(detector.goto)
            isFinishedViewing = buttonClick2(detector.xcor(), detector.ycor(), detector, (-100, -200))
            wn.update()
            drawButton(-100, -200, pen, "white", "continue...")
            pen.goto(-350,100)
            pen.write("When you click continue, \nyou will have 10 seconds to memorize your burger. \nAfter the 10 seconds are up you will have \nto reconstruct the burger from the menu.", align = "left", font = ("Comic Sans MS",27,"bold"))
        wn.clear()
        pen.goto(0,300)
        pen.write("MEMORIZE BURGER", align = "center", font = ("Comic Sans MS",55,"bold"))
        wn.tracer(0)
        createBurger(randomBurger, -150, -300, pen, 0)
        for i in range(10):
            listwriter.goto(0,150)
            listwriter.write(10-i, align = "center", font = ("Comic Sans MS",70,"bold"))
            wn.update()
            time.sleep(1)
            listwriter.clear()
 
    wn.clear()
    wn.tracer(0)
        
    #set up menu and target burger
    for i in range(2):
        for coor in buttonCoordinates:
            drawButton(coor[0],coor[1],pen, coor[3], coor[2])
    drawDivider(pen)
    wn.tracer(0)
    if not difficulty == 4:
        createBurger(randomBurger, -350, -360, pen, 0)
    else:
        pen.goto(-200,100)
        pen.write("What", align = "center", font = ("Comic Sans MS",60,"bold"))
        pen.goto(-200,25)
        pen.write("was", align = "center", font = ("Comic Sans MS",60,"bold"))
        pen.goto(-200,-50)
        pen.write("the", align = "center", font = ("Comic Sans MS",60,"bold"))
        pen.goto(-200,-125)
        pen.write("burger???", align = "center", font = ("Comic Sans MS",60,"bold"))
 
    #write instructions
    pen.up()
    pen.goto(-200, 286)
    pen.down()
    pen.color("black")
    pen.write("A customer would like this burger.\nPlease recreate it.\nClick the buttons to add ingredients to the list.\nThey will be added from the bottom to the top\nin between the buns.", align = "center", font = ("Comic Sans MS",14,"normal"))
    pen.up()
 
    isFinishedMakingBurger = False
    #loop where you add ingredients to your burger
    while not isFinishedMakingBurger:
        listwriter.color("black")
        listwriter.clear()
        writeList(76,334, listwriter, burgerList, "Ingredient List\n(from top to bottom):\n")
        
        wn.onclick(detector.goto)
        isFinishedMakingBurger = buttonClick(detector.xcor(), detector.ycor(), detector, buttonCoordinates, burgerList)
        wn.update()
        #detector.clear()
 
    #when finished button is clicked everything is cleared
    pen.goto(0,0)
    pen.color("royalblue")
    pen.write("PROCESSING BURGER...", align = "center", font = ("Comic Sans MS",50,"bold"))
    pen.color("black")
    time.sleep(2.5) 
    wn.clear()
    wn.tracer(0)
 
    #set up next page: draws burgers side by side
    drawDivider(pen)
    pen.goto(-200,325)
    pen.write("Customer's order:", align = "center", font = ("Comic Sans MS",20,"normal"))
    pen.goto(200,325)
    pen.write("Your burger:", align = "center", font = ("Comic Sans MS",20,"normal"))
    createBurger(randomBurger, -350, -360, pen, 0)
    wn.update()
    createBurger(burgerList, 50, -360, pen, 0.5)
 
    #calculate the percent accuracy of the burgers
    burgerListWithoutBuns = burgerList[1:len(burgerList)-1]
    randomBurgerWithoutBuns = randomBurger[1:len(randomBurger)-1]
 
    ingredientScore = 100*(1 - (compareLists1(burgerListWithoutBuns, randomBurgerWithoutBuns))/((len(randomBurgerWithoutBuns)+len(burgerListWithoutBuns))/2))
    if ingredientScore <= 0:
        ingredientScore = 0
    ingredientScore = round(ingredientScore, 1)
 
    orderScore = 100*((len(burgerListWithoutBuns)-compareLists2(burgerListWithoutBuns, randomBurgerWithoutBuns))/
                                                   (len(randomBurgerWithoutBuns)))
    if orderScore <=0:
        orderScore = 0
    orderScore = round(orderScore, 1)
 
    averageScore = (ingredientScore + orderScore)/2
    averageScore = round(averageScore,1)
 
    #wait for player to click continue button
    drawButton(100, 260, pen, "white", "continue...")
    wn.update()
 
    isFinishedViewing = False
    while not isFinishedViewing:
        wn.onclick(detector.goto)
        isFinishedViewing = buttonClick2(detector.xcor(), detector.ycor(), detector, (100, 260))
        wn.update()
        #detector.clear()
    wn.clear()
    wn.tracer(0)
 
    #next page: grades you on your performance
 
    createBurger(randomBurger, -350, -360, pen, 0)
    createBurger(burgerList, 50, -360, pen, 0)
    writeList(-300,300, listwriter, randomBurger, "Ingredients of \ntarget burger:\n")
    writeList(-150,300, listwriter, burgerList, "Ingredients of \nyour burger:\n")
    listwriter.goto(175,100)
    listwriter.write("Percent accuracy of ingredients:", align = "center", font = ("Comic Sans MS",25,"normal"))
    listwriter.goto(175,60)
    listwriter.write(ingredientScore, align = "center", font = ("Comic Sans MS",25,"normal"))
    listwriter.goto(175,0)
    listwriter.write("Percent accuracy of arrangement:", align = "center", font = ("Comic Sans MS",25,"normal"))
    listwriter.goto(175,-40)
    listwriter.write(orderScore, align = "center", font = ("Comic Sans MS",25,"normal"))
    listwriter.goto(175,-100)
    listwriter.write("Overall accuracy:", align = "center", font = ("Comic Sans MS",25,"normal"))
    listwriter.goto(175,-140)
    listwriter.write(averageScore, align = "center", font = ("Comic Sans MS",25,"normal"))
    wn.update()
 
    #wait for player to click continue button
    for i in range(2):
        drawButton(100, 260, pen, "white", "continue...")
    detector.goto(0,0)
    isFinishedViewing = False
    while not isFinishedViewing:
        wn.onclick(detector.goto)
        isFinishedViewing = buttonClick2(detector.xcor(), detector.ycor(), detector, (100, 260))
        wn.update()
        #detector.clear()
    wn.clear()
 
    wn.tracer(0)
    isSuccessful = False
    if averageScore > 80:
        isSuccessful = True
 
    if not isSuccessful:
        wn.addshape("dumpster2.gif")
        backdrop.shape("dumpster2.gif")
        backdrop.goto(200,0)
        backdrop.stamp()
        createRandomBurger(burgerList, pen)
        pen.goto(0,0)
        pen.color("royalblue")
        pen.down()
        pen.write("CUSTOMER THINKS YOUR BURGER IS TRASH", align = "center", font = ("Comic Sans MS",30,"bold"))
        pen.up()
        pen.goto(0,-40)
        pen.write("HE THREW IT AWAY!!!!!!", align = "center", font = ("Comic Sans MS",30,"bold"))
        wn.update()
    else:
        wn.tracer(0)
        createBurger(burgerList, -360, -360, pen, 0)
        pen.goto(0,300)
        pen.color("black")
        pen.down()
        pen.write("CUSTOMER LOVED YOUR BURGER! CLICK TO EAT!", align = "center", font = ("Comic Sans MS",26,"bold"))
    if isSuccessful:
        buttonX = 100
        buttonY = -25
    else:
        buttonX = -100
        buttonY = 200
    drawButton(buttonX, buttonY, pen, "white", "play again?")
 
    isFinishedViewing = False
    detector.color("white")
    detector.shape("circle")
    detector.shapesize(3,5)
    detector.goto(100,0)
    while not isFinishedViewing:
        
        wn.onclick(detector.goto)
        isFinishedViewing = buttonClick2(detector.xcor(), detector.ycor(), detector, (buttonX, buttonY))
        pen.goto(0,300)
        if isSuccessful:
            pen.write("CUSTOMER LOVED YOUR BURGER! CLICK TO EAT!", align = "center", font = ("Comic Sans MS",26,"bold"))
        wn.update()
        if isSuccessful and detector.xcor() < 0:
            detector.stamp()
    
    wn.clear()
    main()
 
main()


