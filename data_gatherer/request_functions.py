
def choose_tier():
    print("wybierz tier: ")
    print("1. CHALLENGER")
    print("2. GRANDMASTER")
    print("3. MASTER")
    print("4. DIAMOND")
    print("5. PLATINUM")
    print("6. GOLD")
    print("7. SILVER")
    print("8. BRONZE")
    print("9. IRON")
    good_answer = False
    possible_options = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    while not good_answer:
        choosen_option = input("podaj numer: ")
        if choosen_option not in possible_options:
            print("podałeś złą opcję podaj jeszcze raz")
        else:
            good_answer = True
    if int(str(choosen_option)) == 1:
        return "CHALLENGER"
    elif int(str(choosen_option)) == 2:
        return "GRANDMASTER"
    elif int(str(choosen_option)) == 3:
        return "MASTER"
    elif int(str(choosen_option)) == 4:
        return "DIAMOND"
    elif int(str(choosen_option)) == 5:
        return "PLATINUM"
    elif int(str(choosen_option)) == 6:
        return "GOLD"
    elif int(str(choosen_option)) == 7:
        return "SILVER"
    elif int(str(choosen_option)) == 8:
        return "BRONZE"
    elif int(str(choosen_option)) == 9:
        return "IRON"
    else:
        print("coś źle poszło")


def choose_division():
    print("wybierz dywizję: ")
    print("1. I")
    print("2. II")
    print("3. III")
    print("4. IV")
    good_answer = False
    possible_options = ['1', '2', '3', '4']
    while not good_answer:
        choosen_option = input("podaj numer: ")
        if choosen_option not in possible_options:
            print("podałeś złą opcję podaj jeszcze raz")
        else:
            good_answer = True
    if int(str(choosen_option)) == 1:
        return "I"
    elif int(str(choosen_option)) == 2:
        return "II"
    elif int(str(choosen_option)) == 3:
        return "III"
    elif int(str(choosen_option)) == 4:
        return "IV"
    else:
        print("coś źle poszło")

def choose_server():
    print("wybierz serwer: ")
    print("1. RU")
    print("2. KR")
    print("3. BR1")
    print("4. OC1")
    print("5. JP1")
    print("6. NA1")
    print("7. EUN1")
    print("8. EUW1")
    print("9. TR1")
    print("10. LA1")
    print("11. LA2")
    good_answer = False
    possible_options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
    while not good_answer:
        choosen_option = input("podaj numer: ")
        if choosen_option not in possible_options:
            print("podałeś złą opcję podaj jeszcze raz")
        else:
            good_answer = True
    if int(str(choosen_option)) == 1:
        return "RU"
    elif int(str(choosen_option)) == 2:
        return "KR"
    elif int(str(choosen_option)) == 3:
        return "BR1"
    elif int(str(choosen_option)) == 4:
        return "OC1"
    elif int(str(choosen_option)) == 5:
        return "JP1"
    elif int(str(choosen_option)) == 6:
        return "NA1"
    elif int(str(choosen_option)) == 7:
        return "EUN1"
    elif int(str(choosen_option)) == 8:
        return "EUW1"
    elif int(str(choosen_option)) == 9:
        return "TR1"
    elif int(str(choosen_option)) == 10:
        return "LA1"
    elif int(str(choosen_option)) == 11:
        return "LA2"
    else:
        print("coś źle poszło")