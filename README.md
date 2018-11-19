# Задача (Вариант 2)

Имеется набор предметов, каждый из которых имеет два параметра – вес
и ценность – и рюкзак определённой вместимости. Задача заключается в
том, чтобы собрать рюкзак с максимальной ценностью предметов внутри,
соблюдая при этом ограничение рюкзака на суммарный вес.

## Задание 1

С помощью любой существующей библиотеки Python, реализующей 
генетические алгоритмы получить решение задачи о рюкзаке 
для своего набора данных.

## Задание 2

Реализовать генетический алгоритм решения задачи о рюкзаке,
используя свой набор генетических операторов, и получить
результаты на своем наборе данных.

## Генетические операторы

0. Кодирование – выбор «генетического кода».
Особь – битовая последовательность размера n (кол-во грузов);
1. Начальная популяция – кол-во особей всегда = 200: __случайная генерация__;
2. Отбор особей для скрещивания: __выбрать только 20% самых приспособленных особей__;
3. Скрещивание (кроссинговер) между выбранными особями. Каждая особь;
скрещивается 1 раз за 1 поколение, 1 пара дает 2 потомка: __многоточечный с 3мя точками__;
4. Мутация: __случайное изменение 3х битов у 5% особей__;
5. Формирование новой популяции (кол-во особей - константа): __замена не более 30% худших особей на потомков__;
6. Оценка результата.
Наступила сходимость (функция приспособленности лучшей особи в популяциях
отличается не более, чем на 10%) или прошло 500 поколений.