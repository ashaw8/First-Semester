# FIrst-Semester
Projects completed during my first semester of learning Python and Java
 
 #Aidan Shawyer & Zhen Yu
# Returns the price for a given item.
def getItemPrice(categoryDict, item):
    options = categoryDict.keys()
    if item in options:
      return categoryDict[item]
    else:
      return 0 
def getOrderTotal(menuDict, orderList):
    totalPrice = 0.00
    for category in menuDict.keys():
        for order in orderList:
            totalPrice += getItemPrice(menuDict[category], order)
    return totalPrice
# This is given DO NOT change, if this function is not working
# there is an error somewhere else in your code.
def printOrder(orderNumber, orderItems, orderTotal, orderType):
    print("For the following order number: " + str(orderNumber) + ", you ordered a " 
 + orderType + " with the following selections: ", orderItems , "the total for this order will be:$" + str(orderTotal))
    print()
# Print only, Do not use return
def printOrders(finalOrders):
    for item in finalOrders: #item is each list in the 2d-list
        print(item[0:2],item[2:-1],"$",item[-1]) #prints 

def makeOrder(menuDict):
    theOrder = []
    for k, v in menuDict.items():
            if type(v)== dict:
                print("\nFor the category:",k,"\nThese are your options:")
                makeOrder(v)
                print("What do you want from the category",k,":")
                newOrder = input()
                if newOrder in v:      
                    theOrder.append(newOrder)
                    continue
                else:
                    print("Not on the menu, start over")
                    exit()                   
            else:
                print(k)
    return theOrder
             
def main():
    # DO NOT modify this dictionary
    menuItems = {"Rice": {"White": 7.95, "Brown": 7.95, "No Rice": 7.95},\
    "Beans": {"Black": 0.00, "Pinto": 0.00, "No Beans": 0.00},\
    "Protein" : {"Smoked Brisket": 2.35, "Chicken": 0.00, "Steak": 1.35, 
"Barbacoa": 1.35, "Carnitas": 0.50, "Sofritas": 0.00, "Veggie": 0.00},\
    "Toppings" : {"Guacamole": 2.50, "Fresh Tomato Salsa": 0.00, "Corn Salsa": 
0.00, "Green Chili Salsa": 0.00, "Red Chili Salsa": 0.00, "Sour Cream": 0.00, 
"Fajitas": 0.00, "Cheese": 0.00, "Lettuce": 0.00, "Queso": 1.45},\
    "Drinks" : {"Fountain Drink": 2.50, "Juice": 3.00, "Bottled Water": 2.60, "No Drink": 0.00},\
    "Sides": {"Chips": 1.70, "Chips w/ Guac": 4.20, "Chips w/ Queso": 4.20, "Chips w/ Salsa": 2.15, "No Side": 0.00}}
    # Create a variable that keeps track of whether the user has entered stop or not
    flag = True
    # Create a variable that keeps track of the order number
    orderNumber = 1
    # Create your outer list that will have the following values:
    # order number, order type (bowl or burrito), a list that holds the current order list, 
    # and the total cost of the order
    finalList = []
    # As long as the user has not entered stop then continue
    while flag:
        # Ask whether the user would like a bowl, burrito, or stop adding orders
        orderType = input("Do you want a bowl or a burrito, 'stop' to end order.")
        # If the input was stop then come out of the while loop
        if orderType == "stop":
            flag = False
        # If the input was not stop then you should do the following
        else:
            # We will prompt our user to select an order type.
            print("What would you like on your " + orderType + "?")
            # We will call the makerOrder() function to ask the user for a selection for each category.
            currentOrder = makeOrder(menuItems)
            # We will call the getOrderTotal() function to get the total cost for our order. 
            currentOrderTotal = getOrderTotal(menuItems, currentOrder)
            # We will print out our current order 
            printOrder(orderNumber, currentOrder, currentOrderTotal, orderType)
            # We will add our order as the inner list to our outer list
            # The format can be seen below.
            finalList.append([orderNumber, orderType, currentOrder, currentOrderTotal])
            # We increase the order number after we make an order.
            orderNumber += 1
    # Once the user enters "stop" then we print all the orders inside our 2-D list.
    printOrders(finalList)

main()
        
