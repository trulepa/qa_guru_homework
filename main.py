# Найти среднее количество символов в словах любой строки
def average(list):

    # Блок 1 - убираем перенос строки - "\n"
    massive_1 = list.split("\n")
    # print(massive_1)
    buffer = ""

    for element in massive_1:
        buffer = buffer + " " + element.strip()
        # print(buffer)
        buffer = buffer.strip()
    # print(buffer)

    # Блок 2 - исключаем основные символы из подсчета
    massive_2 = buffer.split(" ")
    # print("massive = ", massive)
    summ_words_length = 0
    other_symbol = 0

    for element in massive_2:
        if element[-1] in ("!", ",", ".", "?", ":"):
            element = element[0:-1]
            summ_words_length += len(element)
        elif "-" in element:
            other_symbol += 1
        else:
            summ_words_length += len(element)
    # print(summ_words_length)
    # print(len(massive_2))
    result = summ_words_length / (len(massive_2) - other_symbol)
    return result

list = "Hello, \nmy - name - is \n Alex!"
print(average(list))