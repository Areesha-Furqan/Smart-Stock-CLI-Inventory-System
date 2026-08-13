import json
import os

# Not directly used to create Product, it will automatically creates product by a method
class Product:
    def __init__(self,id,name,category,price,quantity,threshold): #when we creating a product and it was stored in form of dict, now it stores in form of obj
        self.id=id #will be automatically given when product is added
        self.name=name
        self.category=category
        self.price=price
        self.quantity=quantity
        self.threshold=threshold
    
    def __str__(self): #when we try to print a product, this def will automatically be called
        return f'\nID: {self.id} -------------\nName: {self.name}\nCategory: {self.category}\nPrice: {self.price}\nQuantity: {self.quantity} {'low stock!!' if self.quantity<=self.threshold else ''}'

#initializes the object which is the inventory containing products and operations of the inventory management
class InventorySystem:
    def __init__(self): 
        self.inventory_system_data_file='inv_sys_database.json'
        self.inventory=[] #Inventory containing OBJECTS instead of dict
        self.deleted_products=[]
        self.id=1
    
    def add_product(self,n,c,p,q,th): #takes products details and return the Object created
        product=Product(self.id,n,c,p,q,th)
        self.inventory.append(product) #added the product in inventory AS OBJECT
        self.id+=1
        print('\nProduct Added Successfully-----------------')
        return product
    
    def view_products(self):
        if self.inventory != []:
            for obj in self.inventory: #gets product objects in every iteration
                print(obj)
        else:
            print('\nNo Products in the Inventory-----------')
    
    def search_product(self,term):
        if self.inventory != []:
            found=False
            print('_____________Matchings______________')
            for obj in self.inventory:
                if term in obj.name.lower() or term in obj.category.lower():
                    found=True
                    print('| ','ID: ',obj.id,'Name: ',obj.name,'Category: ',obj.category,'Price: ',obj.price,'Quantity: ',obj.quantity)
            if not found:
                print('\nNo such Product in Inventory-------------')
        else:
            print('\nNo Products in the Inventory-----------')
     
    def reduce_stock(self,req_id):
        if self.inventory != []:
            found=False
            for obj in self.inventory:
                if obj.id==req_id:
                    found=True
                    while True:
                        try:
                            reducement=int(input('Sold quantity: '))
                            break
                        except:
                            print('Give correct answer!')
                    if reducement>=obj.quantity:
                        print(f'\nWe only have {obj.quantity} products available ❗')
                        ask=input('Do you want to sell all? (❗RESTOCK RIGHT AFTER❗) [yes/no]: ')
                        if ask.lower()=='yes':
                            obj.quantity=0
                            print('\nReduced Stock Succesfully \nRESTOCK NOW❗❗')
                        else:
                            print('\nReducing Stock Cancelled -------------')
                    else:
                        obj.quantity-=reducement # current amount - reduce amount
                        print('\nReduced Stock Successfully -------------')
            if not found:
                print('\nThis Product is not available ----------------')
        else:
            print('\nNo product in Inventory ----------------')
     
    def increase_stock(self,id):
        if self.inventory != []:
            found=False
            for obj in self.inventory:
                if obj.id==id:
                    found=True
                    while True:
                        try:
                            increment=int(input('Stock Increament of: '))
                            break
                        except ValueError:
                            print('\nPlease Give Correct Answer ---')
                    obj.quantity+=increment # current amount - reduce amount
                    print('\nIncreased Stock Successfully -------------')
            if not found:
                print('\nThis product is not available -----------')
        else:
            print('\nNo inventory stored yet ------------')

    def remove_product(self,req_id):
        if self.inventory != []:
            found=False
            for obj in self.inventory:
                if obj.id==req_id:
                    found=True
                    conf=input('Are you sure? [y/n]')
                    if conf == 'y' or conf=='yes':
                        self.inventory.remove(obj)
                        print('\nProduct Removed Succesfully ------------')                        
                    else:
                        print('\nDeletion Cancelled -----------')
            if not found:
                print('\nThis product is not available -----------')
        else:
            print('\nNo inventory stored yet ------------')        
            
    def load(self):
        if os.path.exists(self.inventory_system_data_file):
            with open(self.inventory_system_data_file,'r') as f:
                data=json.load(f)
            self.id=data.get('recent_id_track',1) #to get recently saved id no to keep continue from it
            self.inventory=[Product(**p) for p in data.get('inventory',[])]
            self.deleted_products=[Product(**p) for p in data.get('deleted_products',[])] 
        else:
            self.inventory=[]
            self.deleted_products=[]
    
    def save(self):
        dict={
            'recent_id_track': self.id,
            'inventory': [p.__dict__ for p in self.inventory],
            'deleted_products': [d.__dict__ for d in self.deleted_products]
        }
        
        with open(self.inventory_system_data_file,'w') as f:
            json.dump(dict,f,indent=4)


#-----------Helper Function----------------------------------------------
def printmenu():
    '''Print Menu of the System'''
    print('\n __________________________________',
          '\n|   SmartStock Inventory System    |',
          '\n|_____________ MENU _______________|',
          '\n|                                  |'
          '\n| (1) Add a New Product            |',
          '\n| (2) View All Products            |',
          '\n| (3) Search a Product             |',
          '\n| (4) Reduce Stock Quantity        |',
          '\n| (5) Increase Stock Quantity      |',
          '\n| (6) Remove a Product Permanently |',
          '\n| (7) Exit                         |',
          '\n|__________________________________|')

#-----------Main CLI Program Logic----------------------------------------
system=InventorySystem() #creates an obbject of the whole system
system.load() #loads the data from json storage

while True:
    printmenu()
    opt=int(input('\nselect an option: '))
    if opt==1:
        name=input('\nProduct Name: ').strip().title()
        categ=input('Category: ').strip().title()
        while True: # to avoid wrong input for price
            try:
                p_no=abs(float(input('Price: ')))
                price=p_no
                break
            except ValueError:
                print('\nPlease Enter Correctly ---\n')
        while True: #to avoid wrong input for quantity
            try:
                qntity=abs(int(input('Quantity: ')))
                break
            except ValueError:
                print('\nPlease Enter Correctly ---\n')                
        while True: #for threshold
            try:
                threshold=int(input('Low Stock Threshold: '))
                break
            except ValueError:
                print('\nPlease Enter Correctly ---\n')                      
        system.add_product(name,categ,price,qntity,threshold)
        system.save()
    elif opt==2:
        system.view_products()
    elif opt==3:
        term=input('\nSearch: ').strip().lower()
        system.search_product(term)
    elif opt==4:
        print('\nWhich Product needs Stock reduce?')
        s=input('\nDo you want to search for Id? [yes/no] ')
        if s=='yes':
            term=input('\nSearch: ').strip().lower()
            system.search_product(term)
        else:
            print(end='')
        id=int(input('\nProduct id: ')) #now they can easily write correct id for their required product
        system.reduce_stock(id)
        system.save()
    elif opt==5:
        print('\nWhich Product needs Stock Increase?')
        s=input('\nDo you want to search for Id? [yes/no] ')
        if s=='yes':
            term=input('\nSearch: ').strip().lower()            
            system.search_product(term)
        else:
            print(end='')
        id=int(input('\nProduct id: ')) #now they can easily write correct id for their required product
        system.increase_stock(id)
        system.save()
    elif opt==6:
        print('\n______Which Product You Want to Remove?_____')
        s=input('\nDo you want to search for Id? [yes/no] ')
        if s=='yes':
            term=input('\nSearch: ').strip().lower()            
            system.search_product(term)
        else:
            print(end='')
        id=int(input('\nProduct id: ')) #now they can easily write correct id for their required product
        system.remove_product(id)
        system.save()
    elif opt==7:
        print('\nGoodBye ------------👋😥')
        break
    else:
        print('\nInvalid selection please try again ---------')        


