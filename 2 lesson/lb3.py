a=input("Введите строку : ") 
b=input("Введите слово для поиска : ") 
if b in a: 
    print(f"Слово '{b}' найдено в строке") 
else: 
    print(f"Слово '{b}' нет в строке!")