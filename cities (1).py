import random
print('Игра в города')
#base = open('C:\\Users\\test\Downloads\\Baza_gorodov.txt')
base = open('Baza.txt')
done = []
score = 0
cities = base.readlines()
if random.randint(0, 1) == 0:
    city = random.choice(cities)
    print('Ход компьютера: ', city)
    done.append(city)
    while True:
        ur_choice = input('Введите город с заглавной буквы: ')
        if ur_choice + '\n' in cities:
            if ur_choice + '\n' not in done:
                done.append(ur_choice)
                score += 1
                print('Ваш счёт:', score)
            else:
                print('Этот город уже был')
                continue
        else:
            print('Такого города нет')
            continue
        ch = ur_choice[-1].upper()
        for elem in cities:
            if ch == elem[0]:
                city = elem
                if city not in done:
                    done.append(city)
                    print('Ход компьютера: ', city)
                    break
                else:
                    continue
            else:
                continue
else:
    while True:
        ur_choice = input('Введите город с заглавной буквы: ')
        if ur_choice + '\n' in cities:
                if ur_choice + '\n' not in done:
                    done.append(ur_choice)
                    score =+ 1
                    print('Ваш счёт:', score)
                else: print('Этот город уже был')

        ch = ur_choice[-1].upper()
        for elem in cities:
            if ch == elem[0]:
                city = elem
                if city + '\n' not in done:
                    done.append(city)
                    print('Ход компьютера: ', city)
                    break
                else:
                    continue
            else:
                continue


