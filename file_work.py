file_name = 'data.txt'

def catalog_reader(file_name):
    menu = {}
    cook_book = {}
    list_ingr = []
    keys = ['ingredient', 'quantity', 'measure' ]
    with open(file_name, encoding='utf-8') as file:
        for line in file:
            cook = line.strip()
            for i in range(int(file.readline())):
                ingr = file.readline().strip()
                menu = ingr.split('|')
                menu_dict = dict(zip(keys, menu))
                list_ingr.append(menu_dict)
                print(list_ingr)
            cook_book[cook] = list_ingr
            file.readline()
    return cook_book
        
# print(catalog_reader(file_name))
catalog_reader(file_name)