# Leet-Code-Integer_To_Roman
>## Описание проекта
>Семь различных символов представляют римские цифры со следующими значениями:
>|символ|значение|
>|:-:|:-:|
>|I|1|
>|V|5|
>|X|10|
>|L|50|
>|C|100|
>|D|500|
>|M|1000|
>
>Римские цифры формируются путем сложения преобразований десятичных значений от самых высоких к самым низким. Преобразование десятичного значения римскую цифру имеет следующие правила:
>
>Если значение не начинается с 4 или 9, выберите символ максимального значения, которое можно вычесть из ввода, приложите этот символ к результату, вычтите его значение и преобразуйте остаток в римскую цифру.
>
>Если значение начинается с 4 или 9, используйте субтрактивную форму, представляющую один символ, вычтенный из следующего символа, например, 4 - 1 (I) меньше 5 (V): IV и 9 - 1 (I) меньше 10 (X): IX. Используются только следующие субтрактивные формы: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) и 900 (CM).
>
>Только степени 10 (I, X, C, M) могут быть добавлены последовательно не более 3 раз, чтобы представить кратные 10. Вы не можете добавить 5 (V), 50 (L) или 500 (D) несколько раз. Если вам нужно добавить символ 4 раза, используйте субтрактивную форму.
>Учитывая целое число, преобразуйте его в римское число.
>
>ссылка на задачу: <https://leetcode.com/problems/integer-to-roman/>

>## результаты работы кода
>![потребление памяти](img/memory.png "потребление памяти")
>![время выполнения](img/runtime.png "время выполнения")

>## Стек
> 1. Python3
> 2. Makefile

>### Автор
>[Михаил Пономарёв](https://github.com/bizarrol423)
