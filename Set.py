from typing import Any

n = 0
tabs_c = ["|_#_|___|___|\n|___|___|___|\n|___|___|___|\n|___|___|___|",
          "|___|_#_|___|\n|___|___|___|\n|___|___|___|\n|___|___|___|",
          "|___|___|_#_|\n|___|___|___|\n|___|___|___|\n|___|___|___|",
          "|___|___|___|\n|_#_|___|___|\n|___|___|___|\n|___|___|___|",
          "|___|___|___|\n|___|_#_|___|\n|___|___|___|\n|___|___|___|",
          "|___|___|___|\n|___|___|_#_|\n|___|___|___|\n|___|___|___|",
          "|___|___|___|\n|___|___|___|\n|_#_|___|___|\n|___|___|___|",
          "|___|___|___|\n|___|___|___|\n|___|_#_|___|\n|___|___|___|",
          "|___|___|___|\n|___|___|___|\n|___|___|_#_|\n|___|___|___|",
          "|___|___|___|\n|___|___|___|\n|___|___|___|\n|_#_|___|___|",
          "|___|___|___|\n|___|___|___|\n|___|___|___|\n|___|_#_|___|",
          "|___|___|___|\n|___|___|___|\n|___|___|___|\n|___|___|_#_|"
          ]
lbd: list[str | Any] = ['2RO2', '3VR2', '1RO3',
                        '2GR2', '2GR1', '2VO2',
                        '2VS2', '2RR1', '1GR1',
                        '3GS1', '2VR1', '2RR3']


# search


def select_pare(l_b_d):
    i = 0
    lists = []
    print("‖ Генерация пар ...")

    while i <= 11:

        newCard = l_b_d.copy()  # создаем копию введеного поля
        card1 = l_b_d[i]  # выбираем 1 карту по порядку 1 --- 12
        newCard.remove(card1)  # из копии поля удаляем выбранную карту

        for x in newCard:  # первый Элем...
            # print(f"‖ ‖ создаем {dnf}/11 пару для {i + 1}/12 карт")
            sefa = [card1, x]
            # print(f"‖ ‖⋙ пара {sefa}")
            lists.append(sefa)
            # print(f"‖ ‖                  {card1} {x}")
        print(f"‖ ‖ {i} пара с карточкой {card1} готова! [x11]")
        # print(f"‖ ‖  пары с карточкой {card1} готовы!\n"
        #       f"‖ ‖‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗\n"
        #       f"‖ ‖")
        i += 1

    i = 0
    clear_list = lists.copy()
    print("‖ Удаление повторяющихся пар ...")
    while i <= 65:
        t_pare = clear_list[i]
        fe, se = t_pare[0], t_pare[1]
        t_pare = [se, fe]
        clear_list.remove(t_pare)
        i += 1

    print(f"‖‗ В итоге мы получили {len(clear_list)} пар ...\n")
    return clear_list


def manage_set(pare_set):
    i = 0
    print("‖ select set")
    lists = []  # сеты

    while i <= 65:

        newCard = lbd.copy()  # список доступных карт
        card_pare = pare_set[i]
        card1 = card_pare[0]
        card2 = card_pare[1]
        newCard.remove(card1)
        newCard.remove(card2)

        for x in newCard:  # первый Элем...
            sefa = [card1, card2, x]
            lists.append(sefa)
        i += 1
        print(f"‖ ‖ {i} сет с карточками {card1} {card2} готов! [x10]")
    print(f"‖‗ В итоге мы получили {len(lists)} сетов ...\n")
    return lists


# search


def reload(s_t_r):
    lista = []
    for c in s_t_r:  # идем по строке
        lista.append(c)  # добавляем буквы в список
    return lista


def dont_false(chars_f, chars_s, chars_t):
    if chars_f != chars_s and chars_f != chars_t and \
            chars_s != chars_f and chars_s != chars_t and \
            chars_t != chars_f and chars_t != chars_s:
        return "False"
    if chars_f == chars_s == chars_t:
        return "True"


def comparison(selected_set):
    first_elem = selected_set[0]
    second_elem = selected_set[1]
    third_elem = selected_set[2]

    F_e = reload(first_elem)
    S_e = reload(second_elem)
    T_e = reload(third_elem)
    chars_f = F_e[0]
    chars_s = S_e[0]
    chars_t = T_e[0]
    color_f = F_e[1]
    color_s = S_e[1]
    color_t = T_e[1]
    form_f = F_e[2]
    form_s = S_e[2]
    form_t = T_e[2]
    bright_f = F_e[3]
    bright_s = S_e[3]
    bright_t = T_e[3]

    if "True" == dont_false(chars_f, chars_s, chars_t):  # одинаковое количество фигур
        if "True" == dont_false(color_f, color_s, color_t):  #
            if "True" == dont_false(form_f, form_s, form_t):
                if "True" == dont_false(bright_f, bright_s, bright_t):
                    return "True"
                if "False" == dont_false(bright_f, bright_s, bright_t):
                    return "True"
                else:
                    return "False"
            if "False" == dont_false(form_f, form_s, form_t):
                if "True" == dont_false(bright_f, bright_s, bright_t):
                    return "True"
                if "False" == dont_false(bright_f, bright_s, bright_t):
                    return "True"
                else:
                    return "False"
            else:
                return "False"
        if "False" == dont_false(color_f, color_s, color_t):
            if "True" == dont_false(form_f, form_s, form_t):
                if "True" == dont_false(bright_f, bright_s, bright_t):
                    return "True"
                if "False" == dont_false(bright_f, bright_s, bright_t):
                    return "True"
                else:
                    return "False"
            if "False" == dont_false(form_f, form_s, form_t):
                if "True" == dont_false(bright_f, bright_s, bright_t):
                    return "True"
                if "False" == dont_false(bright_f, bright_s, bright_t):
                    return "True"
                else:
                    return "False"
            else:
                return "False"
        else:
            return "False"

    if "False" == dont_false(chars_f, chars_s, chars_t):  # разное
        if "True" == dont_false(color_f, color_s, color_t):  #
            if "True" == dont_false(form_f, form_s, form_t):
                if "True" == dont_false(bright_f, bright_s, bright_t):
                    return "True"
                if "False" == dont_false(bright_f, bright_s, bright_t):
                    return "True"
                else:
                    return "False"
            if "False" == dont_false(form_f, form_s, form_t):
                if "True" == dont_false(bright_f, bright_s, bright_t):
                    return "True"
                if "False" == dont_false(bright_f, bright_s, bright_t):
                    return "True"
                else:
                    return "False"
            else:
                return "False"
        if "False" == dont_false(color_f, color_s, color_t):
            if "True" == dont_false(form_f, form_s, form_t):
                if "True" == dont_false(bright_f, bright_s, bright_t):
                    return "True"
                if "False" == dont_false(bright_f, bright_s, bright_t):
                    return "True"
                else:
                    return "False"
            if "False" == dont_false(form_f, form_s, form_t):
                if "True" == dont_false(bright_f, bright_s, bright_t):
                    return "True"
                if "False" == dont_false(bright_f, bright_s, bright_t):
                    return "True"
                else:
                    return "False"
            else:
                return "False"
        else:
            return "False"
    else:
        return "False"


def search_sets(set_variat):
    listseww = []
    i = 0
    ddrs = set_variat.copy()

    while i <= len(ddrs) - 1:
        selected_set = ddrs[i]
        exit_set = comparison(selected_set)
        if exit_set == "True":
            listseww.append(selected_set)
        else:
            pass
        i += 1
    return listseww


# print


def print_set_sh(list_set):
    i = 0
    j = 0
    set_card_numb = []

    print(f"\nBы ввели: \n\n"
          f"| {lbd[0]} | {lbd[1]} | {lbd[2]} |\n"
          f"| {lbd[3]} | {lbd[4]} | {lbd[5]} |\n"
          f"| {lbd[6]} | {lbd[7]} | {lbd[8]} |\n"
          f"| {lbd[9]} | {lbd[10]} | {lbd[11]} |\n\n"
          f"из этих карточек можно собрать такие сеты:\n")

    while j <= len(list_set)-1:
        list = []
        set_wr = list_set[j - 1]
        for x in set_wr:
            list.append(lbd.index(x))
        list.sort()
        set_card_numb.append(list)
        j += 1

    set_card_numb.sort()
    print(set_card_numb)

    while i <= len(list_set)-1:
        exit_print_set = ""
        set_numb = 0

        list = set_card_numb[i]

        print(f"cет № {i+1}")
        while set_numb <= 11:
            if set_numb == list[0] or set_numb == list[1] or set_numb == list[2]:
                exit_print_set = exit_print_set + "|_#_|"
            else:
                exit_print_set = exit_print_set + "|___|"
            if set_numb == 2 or set_numb == 5 or set_numb == 8 or set_numb == 11:
                exit_print_set = exit_print_set + "\n"
            set_numb += 1
        print(exit_print_set)
        i += 1


# print

# input
# while n <= 11:
#     si = tabs_c[n]
#
#     print("Введи значение карточки согласно образцу, снизу указано расположение карточки ⇓")
#     print(si, "\n")
#     sel_tab = input("Ex: 2RO1 \n "
#                     "# 2 - количество фигур (1, 2, 3) \n "
#                     "# R - цвет рисунка (R - красный, V - фиолетовый, G - зелёный) \n "
#                     "# O - форма(O - круг, S - волна, R - ромб)\n "
#                     "# 1 - окрас(1 - закрашено, 2 - штрих, 3 - нет заливки) \n "
#                     "# : ")
#     n += 1
#
#     print("Ok :)")
#     time.sleep(0.8)
#     os.system('CLS')
#     lbd.append(sel_tab)

def main():
    pare_set = select_pare(lbd)  # documented
    set_variations = manage_set(pare_set)  # ~~~~
    list_set = search_sets(set_variations)  #
    print_set_sh(list_set)  # ok
    input("To exit code press enter")


main()
