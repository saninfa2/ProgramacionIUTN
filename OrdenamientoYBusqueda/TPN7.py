from medOrdenamiento import *

#Ejercicio 1
list_to_bubble = [3,4,2,6,-1]
bubble_sort(list_to_bubble)
showList(list_to_bubble)

#Ejercicio 2
list_to_select = ["hola", "manzana", "naranja", "banana"]
select_sort(list_to_select)
showList(list_to_select)

#Ejercicio 3
list_of_book = [{"Titulo": "Rayuela", "Autor": "Cortazar", "anioPublicacion" : 1963},
                {"Titulo": "Cien años de soledad", "Autor": "Marquez", "anioPublicacion" : 1967},
                {"Titulo": "Poemas", "Autor": "Neruda", "anioPublicacion" : 1924},
                {"Titulo": "Violeta", "Autor": "Allende", "anioPublicacion" : 2022}]

sorted_books_by_year = dictionary_sort(list_of_book, key="anioPublicacion")
print("Lista de libros ordenados por año de publicación:")
for book in list_of_book:
    print(f"Título: {book['Titulo']}, Autor: {book['Autor']}, Año: {book['anioPublicacion']}")
    
#Ejercicio 4
list_to_insert_str = ["hola", "manzana", "naranja", "banana"]
insert_sort_string(list_to_insert_str)
showList(list_to_select)

#Ejercicio 5
list_to_bubble = [3,4,2,6,-1]
bubble_sort_descending(list_to_bubble)
showList(list_to_bubble)


#Ejercicio 6
list_to_count = [3,4,2,6]
countsort(list_to_count,6)
showList(list_to_count)

#Ejercicio 7
list_to_bubble_mix = [3,4,2,"bye",6,-1,"hola"]
bubble_sort_mix(list_to_bubble)
showList(list_to_bubble_mix)


#Ejercicio 8
list_to_merge = [3,4,2,6,-1]
merge_sort(list_to_merge)
showList(list_to_merge)