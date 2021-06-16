import test_module as tmod

def ex21():  # N + 2
    string = input('Write the number: ')
    print(float(string) + 2)


def ex22():  # exponentiation
    while True:
        string = input('Write number 0 <= N <= 10: ')
        if 0 <= float(string) <= 10:
            print(float(string) ** 2)
            break
        else:
            print('Incorrect number')


def ex23():  # medical help
    while True:
        mass = []
        cond = 'undefined'
        for i in range(3):
            mass.append(input())
        if int(mass[1]) < 30 and int(mass[2]) <= 120:
            cond = 'good condition'
        elif int(mass[1]) >= 30 and 50 <= int(mass[2]) <= 120:
            cond = 'good condition'
        elif 30 <= int(mass[1]) <= 40 and (int(mass[2]) > 120 or int(mass[2]) < 50):
            cond = 'take care of yourself'
        elif int(mass[1]) >= 40 and (int(mass[2]) > 120 or int(mass[2]) < 50):
            cond = 'medical help required'
        print(f'{mass[0]}, {mass[1]} years old, weight {mass[2]} - {cond}')


def ex41():  # is 2 in 1 list
    my_list_1 = [2, 5, 8, 2, 12, 12, 4]
    my_list_2 = [2, 7, 12, 3]
    for item in my_list_2:
        if item in my_list_1:
            my_list_1.pop(my_list_1.index(item))
    print(my_list_1)


def ex42():  # date to text
    dict_days = {
        '01': 'первое', '02': 'второе', '03': 'третье', '04': 'четвёртое', '05': 'пятое',
        '06': 'шестое', '07': 'седьмое', '08': 'восьмое', '09': 'девятое', '10': 'десятое',
        '11': 'одиннадцатое', '12': 'двенадцатое', '13': 'тринадцатое', '14': 'четырнадцатое', '15': 'пятнадцатое',
        '16': 'шестнадцатое', '17': 'семнадцатое', '18': 'восемнадцатое', '19': 'девятнадцатое', '20': 'двадцатое',
        '21': 'двадцать первое', '22': 'двадцать второе', '23': 'двадцать третье', '24': 'двадцать четвёртое',
        '25': 'двадцать пятое', '26': 'двадцать шестое', '27': 'двадцать седьмое', '28': 'двадцать восьмое',
        '29': 'двадцать девятое', '30': 'тридцатое', '31': 'тридцать первое'
    }
    dict_months = {
        '01': 'января',
        '02': 'феврал',
        '03': 'марта',
        '04': 'апреля',
        '05': 'мая',
        '06': 'июня',
        '07': 'июля',
        '08': 'августа',
        '09': 'сентября',
        '10': 'октября',
        '11': 'ноября',
        '12': 'декабря'
    }
    date = list(map(str, input().split('.')))
    print(f'{dict_days[date[0]].capitalize()} {dict_months[date[1]]} {date[2]} года')


def ex43():  # remove repeated elements in list
    my_list_1 = [2, 2, 5, 12, 8, 2, 12]
    for item in my_list_1:
        if my_list_1.count(item) > 1:
            [my_list_1.remove(item) for _ in range(my_list_1.count(item))]
    print(my_list_1)


#  ex61 written not in this project
def armor_resistance(damage, armor):
    print(damage)
    print(armor)
    print(damage / armor)

    return damage / armor


def attack(attacker, defender):
    defender['health'] -= int(armor_resistance(attacker['damage'], defender['armor']))
    print(f"{defender['name']}\'s health = {defender['health']} ")


def ex83():
    player_name = input('write player\'s name')
    player = {'name': player_name, 'health': 100, 'damage': 10, 'armor': 1.2}
    enemy_name = input('write enemy\'s name')
    enemy = {'name': enemy_name, 'health': 100, 'damage': 10, 'armor': 1.2}
    attack(enemy, player)


def ex141():
    fruits1 = ['apple', 'banana', 'pineapple', 'lemon', 'orange']
    fruits2 = ['apple', 'pear', 'banana', 'mango', 'lemon']
    print()