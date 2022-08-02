file_name = 'data.txt'

def catalog_reader(file_name):
    menu = {}
    cook_book = {}

    keys = ['ingredient', 'quantity', 'measure' ]
    with open(file_name, encoding='utf-8') as file:
        for line in file:
            list_ingr = []
            cook = line.strip()
            circle_number = int(file.readline())
            for i in range(circle_number):
                ingr = file.readline().strip()
                menu = ingr.split('|')
                menu_dict = dict(zip(keys, menu))
                list_ingr.append(menu_dict)
            cook_book[cook] = list_ingr                
            file.readline()
    return cook_book
        
print(catalog_reader(file_name))
# catalog_reader(file_name)

def get_shop_list_by_dishes(menu, person):
# Функция рассчитывает список покупок, в зависимости от меню и кол-ва человек
    cook_book = catalog_reader(file_name)
    shop_list = {}
    if menu in cook_book:
        list_ingr = cook_book[menu]
          
        for i in list_ingr: 
            shop_quantity = {}
            shop_quantity['measure'] = i['measure']
            shop_quantity['quantity'] = int(i['quantity'])*person
            shop_list[i['ingredient']] = shop_quantity
        return shop_list
            
    else:
        print("Такого блюда нет в меню")      


# get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

# print(get_shop_list_by_dishes('Запеченный картофель', 4))


# {
#    'Картофель': {'measure': 'кг', 'quantity': 2}   
# }