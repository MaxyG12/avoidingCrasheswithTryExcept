debugMode = False
pizzaOrder = []

try:
  f = open("pizzaOrder.txt", "r")
  pizzaOrder = eval(f.read())
  f.close()
except:
  print("ERROR: Unable to load")
  if debugMode:
    print(traceback)

def prettyPrint():
  print()
  for row in pizzaOrder:
    print("\nOrder Confirmation")
    print("-------------------")
    print(f"Size:{row[0]} \nCrust:{row[1]} \nSauce:{row[2]} \nCheese:{row[3]} \nToppings:{row[4]} \nSoda: {row[5]}")
  print()

while True:
  print("Romino's Pizza")
  print("----------------")
  print("Welcome to Romino's Pizza")
  print("----------------")
  print("Please select from the following options:")
  print("1. Order a pizza")
  print("2. Exit")
  print("----------------")
  choice = input("Enter your choice (1 or 2): ")
  if choice == "2": 
    break
  else:
      print("----------------")
      print("Please select the size of the pizza:")
      print("1. Small")  
      print("2. Medium")
      print("3. Large")
      print("----------------")
      size_choice = input("Enter your choice (1, 2, or 3): ")
      if size_choice == "1":
          size = "Small"
      elif size_choice == "2":
          size = "Medium"
      elif size_choice == "3":
          size = "Large"
      else:
          print("Invalid choice. Please try again.")
          exit()
  
      print("----------------")
      print("Please select the type of crust:")
      print("1. Thin")
      print("2. Thick")
      print("3. Stuffed")
      print("----------------")
      crust_choice = input("Enter your choice (1, 2, or 3): ")
      if crust_choice == "1":
          crust = "Thin"
      elif crust_choice == "2":
          crust = "Thick"
      elif crust_choice == "3":
          crust = "Stuffed"
      else:
          print("Invalid choice. Please try again.")
          exit()
  
      print("----------------")
      print("Please select the type of sauce:")
      print("1. Tomato")
      print("2. BBQ")
      print("3. No sauce")
      print("----------------")
      sauce_choice = input("Enter your choice (1, 2, or 3): ")
      if sauce_choice == "1":
          sauce = "Tomato"
      elif sauce_choice == "2":
          sauce = "BBQ"
      elif sauce_choice == "3":
          sauce = "No sauce"
      else:
          print("Invalid choice. Please try again.")
          exit()
  
      print("----------------")
      print("Please select the type of cheese:")
      print("1. Mozzarella")
      print("2. Cheddar")
      print("3. No cheese")
      print("----------------")
      cheese_choice = input("Enter your choice (1, 2, or 3): ")
      if cheese_choice == "1":
          cheese = "Mozzarella"
      elif cheese_choice == "2":
          cheese = "Cheddar"
      elif cheese_choice == "3":
          cheese = "No cheese"
      else:
          print("Invalid choice. Please try again.")
          exit()
  
      print("----------------")
      print("Please select the type of toppings:")
      print("1. Pepperoni")
      print("2. Mushrooms")
      print("3. Onions")
      print("4. Sausage")
      print("5. Bacon")
      print("6. Pineapple")
      print("7. Extra cheese")
      print("8. Black olives")
      print("9. Green peppers")
      print("10. Jalapenos")
      print("----------------")
      toppings = []  # Create an empty list to store                          selected toppings
      while True:
        topping_choice = input("Enter your choice              (1- 10) or 'done' to finish: ")
        if topping_choice == "done":
            break
        elif topping_choice in ["1", "2", "3", "4",            "5", "6", "7", "8", "9", "10"]:
          # Map the topping_choice to the actual                 topping name
          toppings_dict = {
              "1": "Pepperoni",
              "2": "Mushrooms",
              "3": "Onions",
              "4": "Sausage",
              "5": "Bacon",
              "6": "Pineapple",
              "7": "Extra cheese",
              "8": "Black olives",
              "9": "Green peppers",
              "10": "Jalapenos"
              }
        toppings.append(toppings_dict[topping_choice])
        
  
      print("----------------")
      print("Please select the type of drink:")
      print("1. Coke")
      print("2. Pepsi")
      print("3. Sprite")
      print("4. Fanta")
      print("5. No drink")
      print("----------------")
      drink_choice = input("Enter your choice (1-5): ")
      if drink_choice == "1":
          drink = "Coke"
      elif drink_choice == "2":
          drink = "Pepsi"
      elif drink_choice == "3":
          drink = "Sprite"
      elif drink_choice == "4":
          drink = "Fanta"
      elif drink_choice == "5":
          drink = "No drink"
      else:
          print("Invalid choice. Please try again.")
          exit()

  row = [size, crust, sauce, cheese, toppings, drink]
  pizzaOrder.append(row)
  prettyPrint()
  
  f = open("pizzaOrder.txt", "w")
  f.write(str(pizzaOrder))
  f.close()






