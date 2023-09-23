#Обратная пара
#Обратной парой будем называть два символа в строке, идущих справа налево. В строке «egh» две обратные пары hg и ge. Посчитайте число таких пар, начинающихся с 'a'.

#Формат входных данных
#В единственной строке содержится исходная последовательность символов, содержащая не менее двух символов и состоящая из строчных латинских букв.
#Форматы выходных данных
#В единственной строке необходимо вывести целое число - количество обратных пар, начинающихся с буквы 'a'.
#Для примера:

#Ввод	Результат
#aaa    2
#baaa   3

dataInput = input()
count = 0

if len(dataInput) < 2:
    print("wrong data")

for index, value in enumerate(dataInput): 
    if value == "a" and index > 0:
        count = count + 1
print(count)
    