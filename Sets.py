lbd = ['3VO1', '1VR1', '3GR1',
       '3GR3', '1GS1', '2VS3',
       '2RR1', '3GS2', '3RO1',
       '1GR3', '2RO2', '2GS2']


def reload(str):
    lista = []
    for c in str:  # идем по строке
        lista.append(c)  # добавляем буквы в список
    return lista


def dont_false(chars_f,chars_s,chars_t):
    if chars_f != chars_s and chars_f != chars_t and chars_s != chars_f and chars_s != chars_t and chars_t != chars_f and chars_t != chars_s:
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

    if "True" == dont_false(chars_f, chars_s, chars_t):# одинаковое количество фигур
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
                print("dont set")
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
                print("dont set")
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
        print("isdont")


def setect_pare(lbd):
    i = 0
    lists = []
    while i <= 11:
        newCard = lbd.copy()
        card1 = lbd[i]
        newCard.remove(card1)
        dnf = 1
        for x in newCard:  # первый Элем...
            sefa = [card1, x]
            lists.append(sefa)
            dnf += 1
        i += 1

    return lists


def manage_set(pare_set):
    i = 0
    lists = []
    while i <= 11:
        newCard = lbd.copy()
        cardsek1 = pare_set[i]
        card1 = cardsek1[0]
        card2 = cardsek1[1]

        newCard.remove(card1)
        newCard.remove(card2)

        dnf = 1
        for x in newCard:  # первый Элем...
            sefa = [card1, card2, x]
            lists.append(sefa)
            dnf += 1
        i += 1

    print("‖‗Done!\n")
    return lists


def search_sets(set_variat):
    listseww = []
    i = 0
    ddrs = set_variat.copy()

    while i <= 119:
        selected_set = ddrs[i]
        exit_set = comparison(selected_set)
        if exit_set == "True":
            listseww.append(selected_set)
        else:
            pass
        i += 1
    return listseww


def print_set_sh(list_set_view,lbd):
    i = 1
    i = int(i)
    list = []
    print(f"вы ввели\n"
          f"|{lbd[0]}|{lbd[1]}|{lbd[2]}|\n"
          f"|{lbd[3]}|{lbd[4]}|{lbd[5]}|\n"
          f"|{lbd[6]}|{lbd[7]}|{lbd[8]}|\n"
          f"|{lbd[9]}|{lbd[10]}|{lbd[11]}|\n"
          f"из этих карточек можно собрать такие сеты:")
    exit_print_set = ""
    set_numb = 0
    lisset = None
    while i <= len(list_set_view):

        set_wr = list_set_view[0]
        for x in set_wr:
            list.append(lbd.index(x))
        list.sort()
        if list == lisset:
            break
        print(f"cет № {i}")
        lisset = list
        while set_numb <= 11:
            if set_numb == list[0] or set_numb == list[1] or set_numb == list[2]:
                exit_print_set = exit_print_set + "|_#_|"
            else:
                exit_print_set = exit_print_set + "|___|"
            if set_numb == 2 or set_numb == 5 or set_numb == 8:
                exit_print_set = exit_print_set + "\n"
            set_numb += 1
        print(exit_print_set)
        i = i + 1
print("‖ Making pares ...")
pare_set = setect_pare(lbd)
set_variations = manage_set(pare_set)
list_set_view = search_sets(set_variations)
print_set_sh(list_set_view,lbd)

input("to Exit code press Enter")