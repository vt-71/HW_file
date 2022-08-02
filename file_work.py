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

# get_shop_list_by_dishes(['Запеченый картофель', 'Омлет'], 2)


# {
#    'Картофель': {'measure': 'кг', 'quantity': 2}   
# }