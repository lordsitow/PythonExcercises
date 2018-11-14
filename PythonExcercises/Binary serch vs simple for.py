list_do_search = ['a']

def ssearch(lista, szukana):
    for i in lista:
        if i == szukana:
            return True
    return False

def binsearch(posortowana_lista, szukana):
    start_index = 0
    middle_index = 0
    end_index = len(posortowana_lista)-1
    while True:
        middle_index=int(round((start_index+end_index)/2, 0))
        if middle_index < start_index or middle_index > end_index or middle_index < 0:
            return False

        middle_element = posortowana_lista[middle_index]

        if middle_element == szukana:
            return True
        elif middle_element > szukana:
            end_index=middle_index
        elif middle_element < szukana:
            start_index = middle_index
        if end_index-start_index == 1:
            return ssearch(posortowana_lista, szukana)
        if len(posortowana_lista) == 1:
            if posortowana_lista[0] == szukana:
                return True
            else:
                return False

print(binsearch(list_do_search, 'a'))