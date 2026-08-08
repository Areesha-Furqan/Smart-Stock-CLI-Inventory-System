
import json
import os

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

def load_data():
    if os.path.exists(json_file):
        with open(json_file,'r') as f:
            loaded_data=json.load(f)
        return loaded_data.get('inventory',[]), loaded_data.get('deleted_products',[])
    else:
        return [],[]

def save_data(inventory_list,deleted_prod):
    data_to_save={
        'inventory':inventory_list,
        'deleted_products':deleted_prod
    }
    with open(json_file,'w') as f:
        json.dump(data_to_save,f,indent=4)

  
def add_product(inventory_list):
    name=input('\nProduct Name: ').strip().title()
    categ=input('Category: ').strip().title()
    while True: # to avoid wrong input for price
        try:
            p_no=abs(float(input('Price: ')))
            price=f'{p_no}$'
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
    pro_id=len(inventory_list)+1
    data_dict={ # a new element in inventory list
        'id':pro_id,
        'name':name,
        'price':price,
        'quantity':qntity,
        'category':categ,
        'threshold':threshold
    }
    inventory_list.append(data_dict)
    print('\n Product Added Succesfully ------------')
    return inventory_list

def view_products(inventory_list):
    if inventory_list != []:
        for dict in inventory_list:
            print(f'\n___________Product id: {dict['id']}___________')
            for k,v in dict.items():
                if k=='id': #to skip id print
                    continue
                if k=='quantity': # to track alert
                    if dict['quantity']<=dict['threshold']:
                        print(f'| {k.capitalize()} : {v} (❗❗LOW STOCK❗❗)')
                    else:
                        print(f'| {k.capitalize()} : {v}')
                else:
                    print(f'| {k.capitalize()} : {v}')
    else:
        print('\nNo Inventory Data Stored Yet --------------')
    return inventory_list #must return even if the func is for printing, otherwise it will return None

def search_product(invventory_list):
    if invventory_list != []:
        found=False
        term=input('\nSearch: ').strip().lower()
        print('_____________Matchings______________')
        for dict in invventory_list:
            if term in dict['name'].lower() or term in dict['category'].lower():
                found=True
                print('| ',end='')
                for k,v in dict.items():
                    print(f' {k.upper()} : {v} ',end='')
                print('\n')
        if not found:
            print('None\n')
    else:
        print('\nNo Inventory Data Stored Yet --------------')
    return invventory_list
                
def reduce_stock_qnty(inventory_list):
    '''prompt user for id and optionally a search for id, and if reducement is greater than current quantity then either total reducement or no reduce'''
    if inventory != []:
        print('\nWhich Product needs Stock reduce?')
        s=input('\nDo you want to search for Id? [yes/no] ')
        if s=='yes':
            search_product(inventory_list) #to make them easy to find their product by search and find its ID
        else:
            print(end='')
        id=int(input('\nProduct id: ')) #now they can easily write correct id for their required product
        found=False
        for dict in inventory_list:
            if dict['id']==id:
                found=True #for safe side, inncase user input a wrong id instead the required one
                while True:
                    try:
                        red=int(input('Sold Quantity: '))
                        break
                    except ValueError:
                        print('\nPlease Give Correct Answer ---')
                if red>=dict['quantity']:
                    print(f'\nWe only have {dict['quantity']} products available ❗')
                    ask=input('Do you want to sell all? (❗RESTOCK RIGHT AFTER❗) [yes/no]: ')
                    if ask.lower()=='yes':
                        dict['quantity']=0
                        print('\nReduced Stock Succesfully \nRESTOCK NOW❗❗')
                    else:
                        print('\nReducing Stock Cancelled -------------')
                else:
                    dict['quantity']-=red # current amount - reduce amount
                    print('\nReduced Stock Successfully -------------')
        if not found:
            print('\nThis product is not available -----------')
    else:
        print('\nNo inventory stored yet ------------')
    return inventory_list
        
def increase_stock_qnty(inventory_list):
    '''same as redduce stock function, just uses + instead of minus'''
    if inventory_list != []:
        print('\nWhich Product needs Stock Increase?')
        s=input('\nDo you want to search for Id? [yes/no] ')
        if s=='yes':
            search_product(inventory_list) #to make them easy to find their product by search and find its ID
        else:
            print(end='')
        id=int(input('\nProduct id: ')) #now they can easily write correct id for their required product
        found=False
        for dict in inventory_list:
            if dict['id']==id:
                found=True #for safe side, inncase user input a wrong id instead the required one
                while True:
                    try:
                        inc=int(input('Stock Increament of: '))
                        break
                    except ValueError:
                        print('\nPlease Give Correct Answer ---')
                dict['quantity']+=inc # current amount - reduce amount
                print('\nIncreased Stock Successfully -------------')
        if not found:
            print('\nThis product is not available -----------')
    else:
        print('\nNo inventory stored yet ------------')
    return inventory_list
        
def remove_product(inventory_list,deleted_prod_dict):
    if inventory_list !=[]:
        print('\n______Which Product You Want to Remove?_____')
        s=input('\nDo you want to search for Id? [yes/no] ')
        if s=='yes':
            search_product(inventory_list) #to make them easy to find their product by search and find its ID
        else:
            print(end='')
        id=int(input('\nProduct id: ')) #now they can easily write correct id for their required product
        found=False
        index=0 #for inc index as iteration goes to find right index of the product
        for dict in inventory_list:
            if dict['id']==id:
                found=True #for safe side, inncase user input a wrong id instead the required one
                conf=input('Are you sure? [y/n]')
                if conf == 'y' or conf=='yes':
                    index_dict=inventory_list.pop(index)
                    deleted_prod_dict.append(index_dict) #to add the product dictionary in deleted products list
                    print('\nProduct Removed Succesfully ------------')
                else:
                    print('\nDeletion Cancelled -----------')
            index+=1
        if not found:
            print('\nThis product is not available -----------')
    else:
        print('\nNo inventory stored yet ------------')
    return inventory_list,deleted_prod_dict           
        
def exit():
    print('\nGoodBye ------------👋😥')


json_file='inventory_data.json'
json_file2='deleted_prod.json'

inventory,deleted_products=load_data()

while True:
    printmenu()
    opt=int(input('\nPlease Select an Option: '))
    if opt==1:
        inventory=add_product(inventory)
        save_data(inventory,deleted_products)
    elif opt==2:
        inventory=view_products(inventory)
    elif opt==3:
        inventory=search_product(inventory)
    elif opt==4:
        inventory=reduce_stock_qnty(inventory)
        save_data(inventory,deleted_products)
    elif opt==5:
        inventory=increase_stock_qnty(inventory)
        save_data(inventory,deleted_products)
    elif opt==6:
        inventory,deleted_products=remove_product(inventory,deleted_products)
        save_data(inventory,deleted_products)
    elif opt==7:
        exit()
        break
    else:
        print('\nInvalid selection please try again ---------')
