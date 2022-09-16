# 1. Дано целое число (int). Определить сколько нулей в этом числе.
number = 1010100001111100000
number_to_str = str(number)
number_of_zeroes = number_to_str.count("0")
print(number_of_zeroes)
# 2. Дано целое число (int). Определить сколько нулей в конце этого числа. Например для числа 1002000 - три нуля
number_of_zeroes_in_the_end = 0
for symbol in number_to_str[::-1]:
    if symbol == "0":
        number_of_zeroes_in_the_end += 1
    else:
        break
print(number_of_zeroes_in_the_end)
# 3. Даны списки my_list_1 и my_list_2.
# Создать список my_result в который вначале поместить
# элементы на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.
my_list_1 = [12,89,63,77]
my_list_2 = [53,68,31,2,5,112]
my_result = my_list_1[::2] + my_list_2[1::2]
print(my_result)
# 4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
# стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]
my_list = [1,2,3,4]
new_list = my_list[1:] + [my_list[0]]
print(new_list, id(my_list))
# 5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
# [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)
first_element = my_list.pop(0)
my_list += [first_element]
print(my_list, id(my_list))
# 6. Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
# Для данного примера ответ - 133. (используйте split и проверку isdigit)
my_str = "43 больше чем 34 но меньше чем 56"
str_to_list = my_str.split()
sum = 0
for element in str_to_list:
    if element.isdigit():
        sum += int(element)
print(sum)
# 7. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
# my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin". (rfind, find - методы строк)
l_limit = "о"
r_limit = "е"
sub_str = my_str[my_str.find(l_limit) + 1:my_str.rfind(r_limit)]
print(sub_str)
# 8. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
# Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
# быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
# (используйте срезы длинны 2)
my_str_list = []
index = 0
while True:
    my_str_list.append(my_str[index:index+2])
    index += 2
    if index > len(my_str) - 1:
        break
if len(my_str_list[-1]) == 1:
    my_str_list[-1] += "_"
print(my_str_list)
# 9. Дан список чисел. Определите, сколько в этом списке элементов,
# которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
# Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.
list_of_numbers = [2,4,1,5,3,9,0,7]
number_of_elements = 0
for num in list_of_numbers[1:-1]:
    previous_number = list_of_numbers.index(num) - 1
    next_number = list_of_numbers.index(num) + 1
    if num > (list_of_numbers[previous_number] + list_of_numbers[next_number]):
        number_of_elements += 1
print(number_of_elements)
# 10. Дан список my_list в котором могут быть как строки (type str) так и целые числа (type int).
# Например [1, 2, 3, "11", "22", 33]
# Создать новый список в который поместить только строки из my_list.
list_of_str_and_int = [1, 2, 3, "11", "22", 33]
my_only_str_list = []
for element_of_list in list_of_str_and_int:
    if type(element_of_list) == str:
        my_only_str_list.append(element_of_list)
print(my_only_str_list)
# 11. Дана строка my_str. Создать список в который поместить те символы из my_str,
# которые встречаются в строке ТОЛЬКО ОДИН раз.
my_string = "111123333344445666666667789999999999AAAAa£££££$QQQQq"
my_another_list = []
for symbols in my_string:
    if list(my_string).count(symbols) == 1:
        my_another_list += symbols
print(my_another_list)
# 12. Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.
my_string_1 = "qq%werctyuii£oopp"
my_string_2 = "uaiis£doofpp%qqgc"
intersection = set(my_string_1).intersection(set(my_string_2))
print(intersection)
# 13. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# но в каждой ТОЛЬКО ПО ОДНОМУ разу.
# Пример: для строк "aaaasdf1" и "asdfff2" ответ ["s", "d"], т.к. эти символы есть в каждой строке по одному разу
the_list_of_uniques_1 = []
the_list_of_uniques_2 = []
for unique_char_1 in my_string_1:
    if list(my_string_1).count(unique_char_1) == 1:
        the_list_of_uniques_1 += unique_char_1
for unique_char_2 in my_string_2:
    if list(my_string_1).count(unique_char_2) == 1:
        the_list_of_uniques_2 += unique_char_2
intersection_of_uniques = list(set(the_list_of_uniques_1).intersection(set(the_list_of_uniques_2)))
print(intersection_of_uniques)