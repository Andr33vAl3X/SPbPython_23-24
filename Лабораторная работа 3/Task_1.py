#Вы работаете в компании, которая разрабатывает программное обеспечение для управления запасами на складе.
#Вашей задачей является написать функцию для поиска индекса первого вхождения элемента в списке товаров.

def find_item_index(items_list, find_item):
   if find_item in items_list:
       return items_list.index(find_item)
   else:
       return None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_item_index(items_list, find_item)  
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
