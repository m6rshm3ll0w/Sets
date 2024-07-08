import time

table = ["2VS3", "1VS3", "1GS2",
         "1GO1", "2RR1", "2GR1",
         "2RS2", "1RS3", "3VO1",
         "2GR2", "2GS2", "3RR3"]

card_icon = ["|_#_|___|___|\n|___|___|___|\n|___|___|___|\n|___|___|___|",
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


def input_cards():
    table = []
    card_number = 0
    while card_number <= 11:
        si = card_icon[card_number]

        print("Введи значение карточки согласно образцу, снизу указано расположение карточки ⇓")
        print(si, "\n")
        sel_tab = input("‖ Ex: 2RO1 \n "
                        "‖ 2 - количество фигур (1, 2, 3) \n "
                        "‖ R - цвет рисунка (R - красный, V - фиолетовый, G - зелёный) \n "
                        "‖ O - форма(O - круг, S - волна, R - ромб)\n "
                        "‖ 1 - окрас(1 - закрашено, 2 - штрих, 3 - нет заливки) \n "
                        "‖‗ : ")
        card_number += 1

        print("Ok :)")
        time.sleep(0.8)
        # os.system('CLS')
        table.append(sel_tab)
    return table


def make_pares(cards):
    pares = set()
    card_number = 0
    number_pare_card = 0
    print("‖ запущено создание пар.....\n"
          "‖ создаю пары [", end="")
    while card_number <= 11:
        # print(f"‖ создаю пары для карточки {cards[card_number]} [", end="")
        print("#", end="")
        cards_for_pare = cards.copy()
        cards_for_pare.remove(cards[card_number])

        while number_pare_card <= 10:
            # print("#", end="")
            pare = [cards[card_number], cards_for_pare[number_pare_card]]
            pare.sort()
            pare = tuple(pare)
            pares.add(pare)
            number_pare_card += 1
            time.sleep(0.007)
        number_pare_card = 0
        # print("]")
        card_number += 1
    print("]")
    print(f"‖‗ создание пар окончено! всего {len(pares)} пар.....\n")
    return pares


def make_combinations(pares, cards):
    combinations = set()
    pare_number = 0
    number_comb_card = 0

    pares_l = list(pares)
    print("‖ запущено создание комбинаций.....\n"
          "‖ создаю комбинации [", end="")
    i = len(pares) - 1
    while pare_number <= i:
        if pare_number % 6 == 0:
            print("#", end="")
        # print(f"‖ создаю комбинации для карточек {pares_l[pare_number]} [", end="")
        cards_for_comb = cards.copy()  # список доступных карт
        select_pare = pares_l[pare_number]
        cards_for_comb.remove(select_pare[0])
        cards_for_comb.remove(select_pare[1])

        while number_comb_card <= 9:
            # print("#", end="")
            pare = pares_l[pare_number]
            comb = [pare[0], pare[1], cards_for_comb[number_comb_card]]
            comb.sort()
            comb = tuple(comb)
            combinations.add(comb)
            number_comb_card += 1
            time.sleep(0.006)
        # print("]")
        number_comb_card = 0
        pare_number += 1
    print("]")
    print(f"‖‗ создание комбинаций окончено! всего {len(combinations)} комбинаций.....\n")
    return combinations


def search_sets(combinations):
    sets = set()
    selected_comb_number = 0
    comb_l = list(combinations.copy())
    print("‖ перехожу к поиску сетов.....\n"
          "‖ ищу сеты [", end="")
    i = len(comb_l) - 1
    while selected_comb_number <= i:
        if selected_comb_number % 20 == 0:
            print("#", end="")
        selected_comb = comb_l[selected_comb_number]
        time.sleep(0.02)
        if check_combination(selected_comb) == "True":
            sets.add(selected_comb)
        else:
            pass
        selected_comb_number += 1
    print("]")
    print(f"‖‗ поиск сетов окончен! всего {len(sets)} сет\сета\сетов .....\n")
    return sets


def check_combination(selected_comb):
    first_elem = list(selected_comb[0])
    second_elem = list(selected_comb[1])
    third_elem = list(selected_comb[2])

    chars_1, color_1, form_1, bright_1 = first_elem[0], first_elem[1], first_elem[2], first_elem[3]
    chars_2, color_2, form_2, bright_2 = second_elem[0], second_elem[1], second_elem[2], second_elem[3]
    chars_3, color_3, form_3, bright_3 = third_elem[0], third_elem[1], third_elem[2], third_elem[3]

    if "True" == check(chars_1, chars_2, chars_3):  # == кол-во
        if "True" == check(color_1, color_2, color_3):
            if "True" == check(form_1, form_2, form_3):
                if "True" == check(bright_1, bright_2, bright_3):
                    return "True"
                if "False" == check(bright_1, bright_2, bright_3):
                    return "True"
                else:
                    return "False"
            if "False" == check(form_1, form_2, form_3):
                if "True" == check(bright_1, bright_2, bright_3):
                    return "True"
                if "False" == check(bright_1, bright_2, bright_3):
                    return "True"
                else:
                    return "False"
            else:
                return "False"
        if "False" == check(color_1, color_2, color_3):
            if "True" == check(form_1, form_2, form_3):
                if "True" == check(bright_1, bright_2, bright_3):
                    return "True"
                if "False" == check(bright_1, bright_2, bright_3):
                    return "True"
                else:
                    return "False"
            if "False" == check(form_1, form_2, form_3):
                if "True" == check(bright_1, bright_2, bright_3):
                    return "True"
                if "False" == check(bright_1, bright_2, bright_3):
                    return "True"
                else:
                    return "False"
            else:
                return "False"
        else:
            return "False"
    if "False" == check(chars_1, chars_2, chars_3):  # != кол-во
        if "True" == check(color_1, color_2, color_3):
            if "True" == check(form_1, form_2, form_3):
                if "True" == check(bright_1, bright_2, bright_3):
                    return "True"
                if "False" == check(bright_1, bright_2, bright_3):
                    return "True"
                else:
                    return "False"
            if "False" == check(form_1, form_2, form_3):
                if "True" == check(bright_1, bright_2, bright_3):
                    return "True"
                if "False" == check(bright_1, bright_2, bright_3):
                    return "True"
                else:
                    return "False"
            else:
                return "False"
        if "False" == check(color_1, color_2, color_3):
            if "True" == check(form_1, form_2, form_3):
                if "True" == check(bright_1, bright_2, bright_3):
                    return "True"
                if "False" == check(bright_1, bright_2, bright_3):
                    return "True"
                else:
                    return "False"
            if "False" == check(form_1, form_2, form_3):
                if "True" == check(bright_1, bright_2, bright_3):
                    return "True"
                if "False" == check(bright_1, bright_2, bright_3):
                    return "True"
                else:
                    return "False"
            else:
                return "False"
        else:
            return "False"


def check(arg_1, arg_2, arg_3):
    if arg_1 != arg_2 and arg_1 != arg_3 and arg_2 != arg_3:
        return "False"
    if arg_1 == arg_2 and arg_1 == arg_3 and arg_2 == arg_3:
        return "True"


def view_sets(sets):
    i = 0
    sel_set = 0
    set_card_numb = []

    print(f"\n‖ На столе лежат эти карты: \n\n"
          f"‖ | {table[0]} | {table[1]} | {table[2]} |\n"
          f"‖ | {table[3]} | {table[4]} | {table[5]} |\n"
          f"‖ | {table[6]} | {table[7]} | {table[8]} |\n"
          f"‖ | {table[9]} | {table[10]} | {table[11]} |\n\n"
          f"‖‗ из этих карт можно собрать такие сеты:\n")

    while sel_set <= len(sets) - 1:
        list = []
        set_wr = sets[sel_set - 1]
        for x in set_wr:
            list.append(table.index(x))
        list.sort()
        set_card_numb.append(list)
        sel_set += 1

    set_card_numb.sort()
    # print(set_card_numb)

    while i <= len(sets) - 1:
        exit_print_set = ""
        set_numb = 0

        list = set_card_numb[i]

        print(f"cет №{i + 1}")
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


def main():
    # table = input_cards()
    pares = make_pares(table)
    combinations = make_combinations(pares, table)
    sets = search_sets(combinations)
    view_sets(list(sets))


main()
