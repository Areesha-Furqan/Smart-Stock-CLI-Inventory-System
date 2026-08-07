
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
          '\n| (7) Set Monthly Budget           |',
          '\n| (8) Exit                         |',
          '\n|__________________________________|')

def load_data():
    if os.path.exists(json_file):
        with open(json_file,'r') as f:
            loaded_data=json.load(f)
        return loaded_data.get('inventory',[])
    else:
        return []

def save_data(inventory_list):
    data_to_save={
        'inventory':inventory_list
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
                


json_file='inventory_data.json'
inventory=load_data()

while True:
    printmenu()
    opt=int(input('\nPlease Select an Option: '))
    if opt==1:
        inventory=add_product(inventory)
        save_data(inventory)
    elif opt==2:
        inventory=view_products(inventory)
    elif opt==3:
        inventory=search_product(inventory)