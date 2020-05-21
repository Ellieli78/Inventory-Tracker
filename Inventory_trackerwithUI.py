from product_inventory_project_UI_ellie import Inventory, Product

inv = Inventory()
switch = True
# print (inv.product_dic)
print("Welcome to Inventory System")
while switch:
    answer = input("Please enter 'a'(add inventory), 'an'(add new items), 's'(sold inventory),\n'i'(item inventory),'iv'(item inventory value),\
't'(total value) to monitor the system, 'o'(output as excel file), or 'e'(Exit).\n >")
    
    if answer.lower() == "a":
            idname = input("Enter product idname\n>")
            checkitem = inv.check_availabe(idname)
            if checkitem == 0:  #the item is not in the dictionary
                try:
                    price = int(input("Sorry, the product is not in the system.\nEnter information to build the new item in the database.\nEnter price of the new item\n>"))
                    quantity = int(input("Enter product quantaity\n>"))  #It will accour error if user did not input int
                    inv.add_new_items(price, idname, quantity)
                except:
                    print("Opps, it seems like you enter wrong information. We'll direct you to the main page.")

            else: 
                try:
                    buy_qty = int(input("Enter buy in quantity.\n >"))
                    inv.add(idname, buy_qty)               
                except:     
                    print("Opps, it seems like you enter wrong information. We'll direct you to the main page.")
                    
    elif answer.lower() == "an":
        idname = input("Enter product idname\n>")
        checkitem = inv.check_availabe(idname)
        if checkitem != 0: #the item already in the dictionary
            try:
                print("The product is already existed. Please add buy in quantity.")
                buy_qty = int(input("Enter buy in quantity.\n >"))  #It will accour error if user did not input int     
                inv.add(idname, buy_qty)  #we need to consider the price change
            except:
                print("Opps, it seems like you enter wrong information. We'll direct you to the main page.")
        
        else:
            try:
                price = int(input("Enter information to build the new item in the database.\nEnter price of the new item\n>"))
                quantity = int(input("Enter product quantaity\n>"))
                inv.add_new_items(price, idname, quantity)
            except:
                print("Opps, it seems like you enter wrong information. We'll direct you to the main page.")
        
    elif answer.lower() == "s":
        idname = input("Enter product idname\n>")
        checkitem = inv.check_availabe(idname)
        if checkitem == 0:
            try:
                price = int(input("Sorry, the product is not in the system.\nNeed to inform sales to cancel the order immediately!!!\nAfterwards, enter information to build the new item in the database.\nEnter price of the new item\n>"))
                quantity = int(input("Enter product quantaity\n>"))  #It will accour error if user did not input int
                inv.add_new_items(price, idname, quantity)
            except:
                print("Opps, it seems like you enter wrong information. We'll direct you to the main page.")
        
        else:
            try:
                sell_qty = int(input("Enter sold quantity.\n >"))
                inv.minus(idname, sell_qty)
            except:
                print("Opps, it seems like you enter wrong information. We'll direct you to the main page.")
        
    elif answer.lower() == "i":
        count = 1
        while count <= 3:
            idname = input("Enter product idname\n>")
            checkitem = inv.check_availabe(idname)
            if checkitem == 0 and count == 3:
                print("The product still can not be found in the system. Please restart.") 
                break

            elif checkitem == 0:  #the item is not in the dictionary
                correct = input("Sorry, the product is not in the system.\nDo you want to reenter product idname or to build the product in the database?\nEnter 'reenter' or 'build'\n>")
                if correct.lower() == "reenter":
                    count += 1
                            
                else:
                    try:
                        price = int(input("Enter information to build the new item in the database.\nEnter price of the new item\n>"))
                        quantity = int(input("Enter product quantaity\n>"))  #It will accour error if user did not input int
                        inv.add_new_items(price, idname, quantity)
                        break
                    except:
                        print("Opps, it seems like you enter wrong information. We'll direct you to the main page.")
                        count = 4
            
            else:
                inv.check_item_inventory(idname)
                break

    elif answer.lower() == "iv":
        count = 1
        while count <= 3:
            idname = input("Enter product idname\n>")
            checkitem = inv.check_availabe(idname)
            if checkitem == 0 and count == 3:
                print("The product still can not be found in the system. Please restart.") 
                break

            elif checkitem == 0:  #the item is not in the dictionary   
                correct = input("Sorry, the product is not in the system.\nDo you want to reenter product idname or to build the product in the database?\nEnter 'reenter' or 'build'\n>")
                if correct.lower() == "reenter":
                    count += 1 

                else:
                    try:
                        price = int(input("Enter information to build the new item in the database.\nEnter price of the new item\n>"))
                        quantity = int(input("Enter product quantaity\n>"))  #It will accour error if user did not input int
                        inv.add_new_items(price, idname, quantity)
                        break
                    except:
                        print("Opps, it seems like you enter wrong information. We'll direct you to the main page.")
                        count = 4
       
            else:
                inv.item_total_value(idname)
                break
  
    elif answer.lower() == "t":
        inv.total_value()

    elif answer.lower() == "o":
        inv.excel_file()

    elif answer.lower() == "e":
        on = input("Are you sure you want to exit? 'yes' or 'no'\n")
        if on.lower() == "yes":
            switch = False
            print("Thank you for using!")
       
    else:
        print("Please enter correct abbreviation again, thank you.")

