lbd = ['3VO1', '1VR1', '3GR1',
       '3GR3', '1GS1', '2VS3',
       '2RR1', '3GS2', '3RO1',
       '1GR3', '2RO2', '2GS2']


def reload(str):
    lista = []
    for c in str:  # идем по строке
        lista.append(c)  # добавляем буквы в список
    return lista


def setect_pare(lbd):
    i = 0
    lists = []
    while i <= 11:
        newCard = lbd.copy()
        card1 = lbd[i]
        print("‖ ##### pares with", card1)
        newCard.remove(card1)
        dnf = 1
        for x in newCard:  # первый Элем...
            sefa = [card1, x]
            lists.append(sefa)
            print("‖ pare №", dnf)
            dnf += 1
        i += 1
        print("‖‗Done\n")


    return lists


pare_set = setect_pare(lbd)

def manage_set(pare_set):
    i = 0
    lists = []
    while i <= 11:
        newCard = lbd.copy()
        card1 = pare_set[i]
        card1 = card1[1]
        print("‖ ##### pares with", card2)
        newCard.remove(card)
        dnf = 1
        for x in newCard:  # первый Элем...
            sefa = [card1, x]
            lists.append(sefa)
            print("‖ pare №", dnf)
            dnf += 1
        i += 1
        print("‖‗Done\n")
print(pare_set)