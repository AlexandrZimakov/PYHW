'''
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
'''
x = int(input("Введите первое число:"))
y = int(input("Введите второе число:"))

s = x + y
p = x * y

found = False
for i in range(1000) :
    for j in range(1000) :
        if i + j == s and i * j == p :
            print(i,j)
            found = True
            break
    if found == True :
        break
        