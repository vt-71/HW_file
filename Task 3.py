import os
path_1 = '1.txt'
path_2 = '2.txt'
path_3 = '3.txt'
os.chdir('text')
file1_path = os.path.join(os.getcwd(), path_1)
file2_path = os.path.join(os.getcwd(), path_2)
file3_path = os.path.join(os.getcwd(), path_3)


def catalog_reader(file_name):
# Подсчет строк в файле
    with open(file_name, encoding='utf-8') as file:
        list_file = file.readlines()
        len_file = len(list_file)
    return len_file
    

def file_result(lib, res_file):
# Функция сортировки файлов по количеству строк и запись в итоговый файл 
    dict_file = {}
    sorted_dict = {}
    lib = ['1.txt', '2.txt', '3.txt']
    for file in lib:
        len_file = catalog_reader(file)
        dict_file[file] = len_file
    sorted_values = sorted(dict_file.values())

    for v in sorted_values:
        for key in dict_file.keys():
            if v == dict_file[key]:
               sorted_dict[key] = v            
 
    with open(res_file, 'a', encoding='utf-8') as file_result:       
        for files in sorted_dict.keys():
            with open(files, encoding='utf-8') as file:
                    list_file = file.readlines()
                    file_result.write(f'{file.name}\n {sorted_dict[files]}\n')
            for i in list_file:
                    file_result.write(f'{i}')
            file_result.write('\n')


# lib = ['1.txt', '2.txt', '3.txt']
lib = [file1_path, file2_path, file3_path]
file_result(lib, 'res.txt')    #Список исходных файлов и итогового файла        

