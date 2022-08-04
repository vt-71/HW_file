file_name = 'data.txt'

def catalog_reader(file_name):
# Функция конвертирует файл в словарь, убирает из меню Фахитос
    menu = {}
    cook_book = {}

    keys = ['ingredient', 'quantity', 'measure' ]
    with open(file_name, encoding='utf-8') as file:
        for line in file:
            list_ingr = []
            cook = line.strip()
            if cook != 'Фахитос': 
                circle_number = int(file.readline())
                for i in range(circle_number):
                    ingr = file.readline().strip()
                    menu = ingr.split('|')
                    menu_dict = dict(zip(keys, menu))
                    list_ingr.append(menu_dict)
                cook_book[cook] = list_ingr
            else:
                circle_number = int(file.readline())
                for i in range(circle_number):
                    file.readline()                                    
                              
            file.readline()
    return cook_book
        
# print(catalog_reader(file_name))
catalog_reader(file_name)

def get_shop_list_by_dishes(menu, person):
# Функция рассчитывает список покупок, в зависимости от меню и кол-ва человек
    shop_list = {}
    cook_book = catalog_reader(file_name)
    for dish in menu:
         if dish in cook_book:             
             for i in cook_book[dish]:
                    shop_quantity = dict() 
                    if i['ingredient'] not in shop_list:                        
                        shop_quantity['measure'] = i['measure']
                        shop_quantity['quantity'] = int(i['quantity'])*person 
                        shop_list[i['ingredient']] = shop_quantity 
                    else:
                        shop_list[i['ingredient']]['quantity'] = shop_list[i['ingredient']]['quantity'] + int(i['quantity']) * person
            
         else:
                print("Такого блюда нет в меню")
                
    return shop_list      


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
print(get_shop_list_by_dishes(['Омлет', 'Омлет'], 1))
