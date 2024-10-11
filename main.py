cook_book = {}
with open('recipes.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    list = text.split('\n\n')
    for item in list:
        item_data = item.split('\n')
        item_name = item_data.pop(0)
        item_ing_count = item_data.pop(0)
        ingredients = [
        (lambda ing = ing.split(' | '): {'ingredient_name': ing[0], 'quantity': ing[1], 'measure': ing[2]})()
        for ing in item_data
        ]
        cook_book[item_name] = ingredients

# Вывод Задания №1
# print(cook_book)

def get_shop_list_by_dishes(dishes, person_count: int):
    result = {}
    for dish in dishes:
        ings = cook_book.get(dish)
        for ing in ings:
            ing_name = ing.get('ingredient_name')
            ing_count = int(ing.get('quantity'))
            save_res = int((result.get(ing_name) or {}).get('quantity') or 0)
            result[ing_name] = {
                'measure': ing.get('measure'),
                'quantity': save_res + (ing_count * person_count)
            }

    # Вывод Задания №2
    # print(result)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 1)


def save_sorted_files(result_file_path: str):
    if (result_file_path is None):
         raise ValueError('Не передан путь сохранения')
    
    filte_names = ['1.txt', '2.txt', '3.txt']
    dir = './sorted/'

    res = []
    for file_name in filte_names:
        with open(dir + file_name, encoding='utf-8') as f:
                content_arr = f.readlines()
                file_len = len(content_arr)
                res.append({
                     'name': file_name,
                     'lenes_count': str(file_len),
                     'content': ''.join(content_arr)
                })
    res.sort(key=lambda elem: elem['lenes_count'])
    with open(result_file_path, mode='w', encoding='utf-8') as res_file:
         for res_item in res:
             write_content = f"""{res_item['name']}\n{res_item['lenes_count']}\n{res_item['content']}\n"""
             res_file.write(write_content)
        
         
# Сохранение файла Задание №3
# save_sorted_files('./res.txt')