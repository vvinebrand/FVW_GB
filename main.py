# Задача: Написать программу, которая из имеющегося массива формирует массив из строк, длина которых >= 3-м символам.

print('Enter the words you want to add to the array separated by space: ', end="")
arr = input().split()
print(f'\nYour array: {arr}\n')
words = [i for i in arr if len(i) <= 3]

