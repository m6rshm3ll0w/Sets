lbd = ['3VO1', '1VR1', '3GR1',
       '3GR3', '1GS1', '2VS3',
       '2RR1', '3GS2', '3RO1',
       '1GR3', '2RO2', '2GS2']


def reload(str):
    lista = []
    for c in str:  # идем по строке
        lista.append(c)  # добавляем буквы в список
    return lista


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
    if chars_f == chars_s == chars_t:
        print(chars_f, chars_s, chars_t,"111")# одинаковое количество фигур
        if color_f == color_s == color_t:  #
            if form_f == form_s == form_t:
                if bright_f == bright_s == bright_t:
                    return "True"
                if bright_f != bright_s != bright_t:
                    return "True"
                else:
                    return "False"
            if form_f != form_s != form_t:
                if bright_f == bright_s == bright_t:
                    return "True"
                if bright_f != bright_s != bright_t:
                    return "True"
                else:
                    return "False"
            else:
                print("dont set")
                return "False"
        if color_f != color_s != color_t:
            if form_f == form_s == form_t:
                if bright_f == bright_s == bright_t:
                    return "True"
                if bright_f != bright_s != bright_t:
                    return "True"
                else:
                    return "False"

            if form_f != form_s != form_t:
                if bright_f == bright_s == bright_t:
                    return "True"
                if bright_f != bright_s != bright_t:
                    return "True"
                else:
                    return "False"
            else:
                return "False"
        else:
            return "False"

    if chars_f != chars_s and chars_f != chars_t and chars_s != chars_f and chars_s != chars_t and chars_t != chars_f and chars_t != chars_s:  # разное
        print(chars_f, chars_s, chars_t, "123")
        if color_f == color_s == color_t:  #
            if form_f == form_s == form_t:
                if bright_f == bright_s == bright_t:
                    return "True"
                if bright_f != bright_s != bright_t:
                    return "True"
                else:
                    return "False"
            if form_f != form_s != form_t:
                if bright_f == bright_s == bright_t:
                    return "True"
                if bright_f != bright_s != bright_t:
                    return "True"
                else:
                    return "False"
            else:
                return "False"
        if color_f != color_s != color_t:
            if form_f == form_s == form_t:
                if bright_f == bright_s == bright_t:
                    return "True"
                if bright_f != bright_s != bright_t:
                    return "True"
                else:
                    return "False"

            if form_f != form_s != form_t:
                if bright_f == bright_s == bright_t:
                    return "True"
                if bright_f != bright_s != bright_t:
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

    while i <= len(ddrs):
        selected_set = ddrs[i]
        exit_set = comparison(selected_set)
        if exit_set == "True":
            listseww.append(selected_set)
            print(f"{selected_set} it's set")
        else:
            pass
        i += 1


print("‖ Making pares ...")
pare_set = setect_pare(lbd)
set_variat = manage_set(pare_set)
search_sets(set_variat)

