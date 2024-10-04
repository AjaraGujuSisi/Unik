print("Общество в начале XXI века")
x =int(input("Введите возраст = "))
if(x>=0 and x<=7):
    print("Вам в детский сад")
elif(x>=7 and x<18):
    print("Вам в школу")
elif(x>=18 and x<25):
    print("Вам в профессиональное учебное заведение")
elif(x>=25 and x<60):
    print("Вам на работу")
elif(x>=60 and x<120):
    print("Вам предоставляется выбор")
else:
   for i in range(5):
        print("Ошибка")