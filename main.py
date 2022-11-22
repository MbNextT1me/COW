import numpy as np
import re

def read_cow_text(name):
    print(f"File {name} Execution Result:")
    file = open(name, 'r')
    f=file.read()

    str = re.sub(r'\n', r' ', f).split(' ')

    arr=[]
    d = {}
    ind=0

    for i in str:
        if i == 'MOO':
            arr.append(ind)
        if i == 'moo':
            d[ind]=arr[len(arr)-1]
            d[arr.pop()]=ind
        ind+=1

        
    res = np.zeros(10000)
    ind = 0
    i = 0

    while(i != len(str)):
        # MoO - значение текущей ячейки увеличить на 1
        if str[i] == 'MoO':
            res[ind] += 1

        # MOo - значение ​текущей ячейки уменьшить на 1
        if str[i] == 'MOo':
            res[ind] -= 1

        # moO - следующая ячейка
        if str[i] == 'moO':
            ind += 1

        # mOo - предыдущая ячейка
        if str[i] == 'mOo':
            ind -= 1

        # moo - начало цикла
        if str[i] == 'moo':
            i = d[i]-1

        # MOO - конец цикла
        if str[i] == 'MOO':
            if res[ind] == 0:
                i = d[i]

        # OOM - вывод значения текущей ячейки  
        if str[i] == 'OOM':
            print(int(res[ind]),end='')

        # oom - ввод значения в текущую ячейку
        if str[i] == 'oom':
            res[ind] = input()

        # mOO - выполнить инструкцию с номером из текущей ячейки              
        if str[i] == 'mOO':
            res[ind] = i
        
        # Moo - если значение в ячейке равно 0, то ввести с клавиатуры, если значение не 0, то вывести на экран
        if str[i] == 'Moo':
            if str[ind] != 0:
                print(chr(int(res[ind])), end=" ")
            else:
                input("Enter your value")
        
        # OOO - обнулить значение в ячейке        
        if str[i] == 'OOO':
            str[ind] = 0
        else:
            i += 1
            continue
        i += 1
    print("\n")

if __name__ == "__main__":
    read_cow_text("fib.cow")
    read_cow_text("hello.cow")