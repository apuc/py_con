#-*- coding: utf-8 -*-

#на всякий случай вдруг запуститься не в UTF-8
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#основной код
import re
from fractions import Fraction

#проверка на то присутсвует что либо кроме цифр
def only_numbers(data):
    res = re.search(r'[^.,\d]+', data)
    if res == None:
        return True
    else:
        return False

#ввод данных
def inputArr():
    while True:
        arr = input('Введите последовательность чисел через запятую: ')
        if arr == 'exit':
            sys.exit(1)
        elif arr != '' and only_numbers(arr):
            arr = arr.split(',')
            if len(arr) > 1:
                break
    arr = [float(elem) for elem in arr]
    return arr

#проверка на геометрическую прогрессию
def geometricProgression(data):
    q = round(data[1] / data[0], 5)
    dopInf = ''
    for i in range(len(data)-1):
        if data[i+1] != round(data[i]*q, 5):
            return False, dopInf


    if -1 < q < 1:
        dopInf = ', бесконечно убывающая'

    return True, dopInf

#проверка на арифметическую прогрессию
def arithmeticProgression(data):
    d = round(data[1] - data[0], 5)
    dopInf = ''
    for i in range(len(data)-1):
        if data[i+1] != round(data[i]+d, 5):
            return False, dopInf

    if d > 0:
        dopInf = ', возрастающая'
    elif d < 0:
        dopInf = ', убывающая'
    else:
        dopInf = ', стационарная'

    return True, dopInf


def main():
    try:
        arr = inputArr()
        print(arr)
        arithmeticProgressionRes, arithmeticDopInf = arithmeticProgression(arr)
        geometricProgressionRes, geometricDopInf = geometricProgression(arr)
        if arithmeticProgressionRes:
            print('Это арифметическая прогрессия' + arithmeticDopInf)
        elif geometricProgressionRes:
            print('Это геометрическая прогрессия' + geometricDopInf)
        else:
            print('Прогрессия отсутствует')
    except:
        print('Что то пошло не так')



if __name__ == '__main__':
    main()
