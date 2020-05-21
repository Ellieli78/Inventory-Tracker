#Inventory tracker Project - Create an application which manages an inventory of products. 
#Create a product class which has a price, id, and quantity on hand. Then create an inventory class 
#which keeps track of various products and can sum up the inventory value.

# Project Scope:
# In product class, we need product price, id, and quantity. 
# In inventory class, we need to track inventory out and in, and sum up the inventory value.

# Step 1: Create product class
import pandas as pd

class Product():
    
    def __init__(self):
        self.product_dic = {}
        # self.product_dic[self.idname] = [self.quantity,self.price]

    def add_new_items(self, price, idname, quantity):
        self.product_dic[idname] = [quantity,price]
        print("The item has successfully added to the system.")
        print(self.product_dic)
        
    def show_dic(self):
        print (self.product_dic) 

# Step 2: Create inventory class
class Inventory(Product):
    
    def __init__(self):
        Product.__init__(self)

    # Create 2 functions for updating Qty after product buy in and sell 
    def add(self, idname, buy_qty):
            ori_qty = self.product_dic[idname][0]
            update_qty = int(ori_qty) + int(buy_qty)
            self.product_dic[idname][0] = update_qty
            print( "we buy {} QTY of {} into our inventory, the total QTY is {}".format(buy_qty, idname, update_qty))

    def minus(self, idname, sell_qty):
        ori_qty = self.product_dic[idname][0]
        if ori_qty < sell_qty:
            print("Sorry, you don‘t have enough stocks of this item to sell.\nPlease inform sales immediately!!!")
        
        else:
            update_qty = int(ori_qty) - int(sell_qty)
            self.product_dic[idname][0] = update_qty
            print( "we sell {} QTY of {} from our inventory, the total QTY is {}".format(sell_qty, idname, update_qty))
       
        
    # Check existing inventory QTY
    def check_item_inventory(self, idname):
        item_inv = self.product_dic[idname][0]
        print(item_inv) 

    # Create a function to sum up an item's inventory value  
    def item_total_value(self, idname):
        total = int(self.product_dic[idname][0]) * int(self.product_dic[idname][1]) 
        print("$"+str(total))
    
    # Create a function to sum up the total inventory value
    # @ self.product_dic
    def total_value(self):
        total = []
        for d in self.product_dic:
            sum = int(self.product_dic[d][0]) * int(self.product_dic[d][1]) # if there's not int() it will be string?
            total.append(sum)

        sum_up = 0
        for i in total:
            sum_up += int(i)
        print ("$"+str(sum_up))

        # original:
        # for d in self.product_dic.keys():
        #     sum = self.product_dic[d][0] * self.product_dic[d][1]
        #     sum += sum
        #     print(sum)

    def check_availabe(self, idname):
        check = self.product_dic.get(idname,0)
        return check
# Product(input("Please key in the product information, enter price, id , and quantity accordingly\n"))
   
    def excel_file(self):
        df = pd.DataFrame(self.product_dic).T
        df.columns =['Quantity', 'Price']
        df.to_excel('Inventory.xlsx')



