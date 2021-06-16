import telebot
import config

bot = telebot.TeleBot(config.token)


def pers_def(user_id):
    if user_id == 388287605:
        return 'Господин Администратор'
    elif user_id == 903245834:
        return 'Хозяин'
    elif user_id == 456804887 or user_id == 366297736:
        return 'Хозяйка'
    else:
        return 'Гость'


@bot.message_handler(commands=['start'])
def start_command(message):
    pers = pers_def(message.chat.id)
    bot.send_message(
        message.chat.id, f'Доброго времени суток, {pers}!\n'
                         f'Доступные для Вас команды: /help, /start, /walk\n'
                         f'Вы можете воспользоваться переводом муки или сахара в гр или мл\n'
                         f'Переведи (число) (гр/мл) (сахар/мука)'
                         f'Я могу составить для вас список покупок, напишите "Запиши сп", '
                         f'а потом вводите нужные продукты по одному. '
                         f'Когда решите закончить - напишите "Стоп".\n'
                         f'Напишите "сп", если хотите посмотреть список продуктов.\n'
                         f'Напишите "Удали сп", если хотите удалить список покупок.\n'
                         f'Напишите "Удали", если хотите удалить только определенные товары из списка покупок.'
                         f'Не забудте, что список покупок один, так что удаляйте, если он уже выполнен.')
    with open('bot_users.txt', 'r', encoding='utf-8') as rf:
        flag = False
        for line in rf.readlines():
            if int(line.strip().split(' ')[0]) == message.chat.id:
                flag = True
                break
    if not flag:
        bot.send_message(message.chat.id, 'Вы записаны')
        with open('bot_users.txt', 'a', encoding='utf-8') as af:
            af.write(f'{message.chat.id} {message.chat.first_name} {message.chat.last_name} \n')


@bot.message_handler(commands=['help'])
def help_command(message):
    pers = pers_def(message.chat.id)
    bot.send_message(
        message.chat.id, f'Доброго времени суток, {pers}!\n'
                         f'Доступные для Вас команды: /help, /start, /walk\n'
                         f'Вы можете воспользоваться переводом муки или сахара в гр или мл\n'
                         f'Переведи (число) (гр/мл) (сахар/мука)'
                         f'Я могу составить для вас список покупок, напишите "Запиши сп", '
                         f'а потом вводите нужные продукты по одному. '
                         f'Когда решите закончить - напишите "Стоп".\n'
                         f'Напишите "сп", если хотите посмотреть список продуктов.\n'
                         f'Напишите "Удали сп", если хотите удалить список покупок.\n'
                         f'Напишите "Удали", если хотите удалить только определенные товары из списка покупок.'
                         f'Не забудте, что список покупок один, так что удаляйте, если он уже выполнен.')


def prod_func(message):
    if message.text.lower() == 'стоп':
        bot.send_message(message.chat.id, f'Прекрасный список продуктов у Вас получился, {pers_def(message.chat.id)}!')
    else:
        with open('prod_file.txt', 'a', encoding='utf-8') as wf:
            wf.write(message.text.strip().lower() + '\n')
        bot.register_next_step_handler(message, prod_func)


def del_prod_func(message, prods):
    pers = pers_def(message.chat.id)
    numbers = message.text.strip().split()
    if numbers[0].lower().strip() == 'отмена':
        bot.send_message(message.chat.id, f'Как прикажете, {pers}')
    else:
        prods = [prods[i] for i in range(len(prods)) if str(i + 1) not in numbers]
        with open('prod_file.txt', 'w', encoding='utf-8') as wf:
            wf.writelines(prods)
            bot.send_message(message.chat.id, f'Список продуктов изменен, {pers}!')


@bot.message_handler(content_types='sticker')
def sticker_id(message):
    bot.send_message(message.chat.id, message.sticker.file_id)


@bot.message_handler(commands=['share_list'])
def share_list_command(message):
    with open('prod_file.txt', 'r', encoding='utf-8') as rf:
        temp_prod_list = rf.readlines()
        if not temp_prod_list:
            bot.send_message(message.chat.id, f'Список продуктов пуст, {pers_def(message.chat.id)}!')
            return None
    with open('bot_users.txt', 'r', encoding='utf-8') as user_file:
        for items in user_file.readlines():
            if int(items.split()[0]) != message.chat.id:
                bot.send_message(int(items.split()[0].strip()),
                                 f'{pers_def(int(items.split()[0]))}, С Вами поделились списком продуктов!')
                bot.send_message(int(items.split()[0].strip()), ''.join(temp_prod_list))
            else:
                bot.send_message(int(items.split()[0].strip()), 'Список продуктов отправлен.')


@bot.message_handler(commands=['stop'])
def stop_command(message):
    non_stop_sticker_id = 'CAACAgIAAxkBAAICMWCjsveZsJ0j4te5npGfxx_Awc1jAAIfiAACns4LAAE5vslj-SZ_Gh8E'
    if message.chat.id == 388287605:
        with open('bot_users.txt', 'r') as rf:
            for item in rf.readlines():
                bot.send_message(int(item.split()[0]), 'Я выключаюсь.')
        bot.stop_bot()
    else:
        bot.send_message(message.chat.id, 'Чтобы меня выключить, Вам придется написать Админстратору!')
        bot.send_sticker(message.chat.id, non_stop_sticker_id)


@bot.message_handler(content_types=["text"])
def content_text(message):
    pers = pers_def(message.chat.id)
    hoz_string = f'Как прикажете, {pers}! \n'
    # bot.send_message(message.chat.id, f'Ты написал {message.text}')
    temp = message.text.lower().strip().split(' ')
    if temp[0] == 'переведи':
        if temp[3] == 'мука':
            if temp[2] == 'гр':
                bot.send_message(message.chat.id, hoz_string + f'Объем муки в мл = {int(int(temp[1]) * 1.695)}')
            if temp[2] == 'мл':
                bot.send_message(message.chat.id, hoz_string + f'Вес муки в гр = {int(int(temp[1]) / 1.695)}')
        if temp[3] == 'сахар':
            if temp[2] == 'гр':
                bot.send_message(message.chat.id, hoz_string + f'Объем сахара в мл = {int(int(temp[1]) * 1.31)}')
            if temp[2] == 'мл':
                bot.send_message(message.chat.id, hoz_string + f'Вес сахара в гр = {int(int(temp[1]) / 1.31)}')
    elif ' '.join(temp) == 'запиши сп':
        bot.send_message(message.chat.id, f'Что записать, {pers}?')
        bot.register_next_step_handler(message, prod_func)
    elif ' '.join(temp) == 'удали сп':
        f = open('prod_file.txt', 'w')
        f.close()
        bot.send_message(message.chat.id, f'Сделано, {pers}!')
    elif temp[0] == 'удали':
        with open('prod_file.txt', 'r', encoding='utf-8') as wrf:
            lines = wrf.readlines()
            if not lines:
                bot.send_message(message.chat.id, f'Список продуктов пуст, {pers}.')
            else:
                temp_list = []
                for ind, item in enumerate(lines):
                    temp_list.append(f'{ind + 1}) {item.capitalize()}')
                bot.send_message(message.chat.id, ''.join(temp_list))
                bot.send_message(message.chat.id, f'Введите через пробел номера продуктов, '
                                                  f'которые необходимо удалить, или введите "Отмена"?')
                bot.register_next_step_handler(message, del_prod_func, lines)
    elif temp[0] == 'сп':
        with open('prod_file.txt', 'r', encoding='utf-8') as rf:
            try:
                bot.send_message(message.chat.id, ''.join(rf.readlines()))
            except Exception:
                bot.send_message(message.chat.id, f'Список продуктов пуст, {pers}!')
    elif temp[0] == 'привет':
        bot.send_message(message.chat.id, f'Доброго времени суток, {pers}!')
    elif temp[0] == 'спасибо':
        bot.send_message(message.chat.id, f'Вы слишко добры, {pers}!')
    else:
        bot.send_message(message.chat.id, f'Я Вас не понимаю, {pers}.\n'
                                          f' Доступные команды: /help, /start, /walk\n')


"""
@bot.message_handler(content_types=["document"])
def content_document(message):
    # https://ru.stackoverflow.com/questions/1176757/Как-получить-файл-присланный-пользователем-боту-в-telegram-на-python
    print('Боту отправили документ')
    if not os.path.isdir("Telegram files"):
        os.mkdir("Telegram files")
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = 'C:/Users/serge/TeleBot/Telegram files/' + message.document.file_name
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)

    bot.reply_to(message, "Пожалуй, я сохраню это")
"""
"""
with open('bot_users.txt', 'r') as user_file:
    for items in user_file.readlines():
        bot.send_message(int(items.split()[0]), 'Я включился.')"""
bot.polling(none_stop=True)
