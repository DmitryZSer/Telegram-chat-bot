import telebot
from telebot import types

from bs4 import BeautifulSoup
import requests, random


bot = telebot.TeleBot(('your token'))

reply_markup=types.ReplyKeyboardRemove()

user_name = ''

name = ''
surname = ''
age = 0

user_word = 'error'
bot_word = 'error'
first_try = True

best_score = 0
total_attempts = 0

score = 0
list_of_user_words = []

list_of_bot_words = []

@bot.message_handler(content_types=['text'])
def ru_get_text_messages(message):
    print(message.text)
    global user_name

    global first_try
    global bot_word
    global user_word
    global score
    global list_of_user_words
    global list_of_bot_words

    user_name = message.from_user.first_name

    if message.text == '/help':
        bot.send_message(message.from_user.id, f'Привет {user_name}, это бот для игры в слова! \n'
                                               'Правила просты как и в оригинальной игре:\n'
                                               'Пишешь слово, я отвечаю словом которое начинается на ту же букву, какой оканчивается твое.\n'
                                               'Если слово бота заканчивается на ый, пиши слово на 3 букву с конца, если на ь, ъ, ы или й на 2\n'
                                               'Для того чтобы начать игру напиши /start\n'
                                               'Для того чтобы узнать статистику напиши /stats')
    elif message.text == '/stats':
        bot.send_message(message.from_user.id, f'Вот твоя статистика, {user_name}!')
        bot.send_message(message.from_user.id, f'Лучший результат: {best_score}')
        bot.send_message(message.from_user.id, f'Количество попыток: {total_attempts}')
    elif message.text == '/start':
        bot.send_message(message.from_user.id, "Напиши какое-нибуть слово ")
        first_try = True
        user_word = 'error'
        bot_word = 'error'
        score = 0
        list_of_user_words = []
        list_of_bot_words = []
        bot.register_next_step_handler(message, ru_get_new_word)
    else:
        bot.send_message(message.from_user.id, 'Напиши /help, если что!)')



mockery = [
"ну чтодаже компьютер быстрее думает!",
"в следующей жизни попробуй выбрать что-то короче",
"слова-ответыкак карликовая эстафета",
"ты точно не отыгрываешь роль зомби в словах?",
"а где кнопка ""Ускоренная Печать""?",
"это не спринтчтобы так долго загружаться",
"ты уверенчто клавиши не залипли?",
"даже улитка быстрее ползает",
"думаешь, где-то есть рекорд по медлительности?",
"это не сончтобы вяло тянуться",
"как на дороге - тормозишь на каждом слове!",
"даже калькулятор быстрее подсчитает",
"это не вечность, чтобы так долго висеть в воздухе",
"слова бегут, а ты стоишь на старте",
"у тебя что, клавиши на пенсию отправили?",
"скорость мысли - не про тебя?",
"не в лесу, а словах заблудился?",
"народ уже заснулдожидаясь твоего следующего слова",
"это не кроссворд, чтобы так замедляться",
"слова, как котики - не любят долго ждать",
"ты не торт, чтобы расползаться со словом",
"даже ленивец бы устал от такого темпа",
"слова в рекордное время на выводе!",
"не детектив, чтобы так медленно раскрываться",
"даже в шахматах быстрее ходят!",
"как долго тебе нужно было подумать?",
"а я думал, это слово на экспрессе!",
"ну что, дальше плавно переходим к азбуке?",
"это слово, или ты случайно пошутил?",
"не угадал, держи билет в словарь.",
"у меня уже дождь прошела ты только начал.",
"даже старик в деревне быстрее угадывает.",
"ну что, дальше или уже устал?",
"даже моя кофеварка быстрее работает.",
"это слово на каникулах, поэтому так долго.",
"я ведь прошу просто словоне оперу.",
"сколько тебе нужно времени на одно слово?",
"я чуть не заснулпока ты думал.",
"такие слова тут как гости - не задерживаются."]

def ru_get_new_word(message):
    global user_word
    global bot_word
    global first_try

    global best_score
    global total_attempts

    global score
    global list_of_user_words

    print("\n" + user_word)
    print(bot_word)

    if message.text == '/end':
        bot.send_message(message.from_user.id, 'Игра окончена!')
        if score > best_score:
            best_score = score
            bot.send_message(message.from_user.id, f'Ты поставил новый рекорд, со счетом: {best_score}')
            bot.send_message(message.from_user.id, 'Напиши /start чтобы попробовать еще раз')
            bot.register_next_step_handler(message, ru_get_text_messages)
        elif score < best_score:
            bot.send_message(message.from_user.id, f'Твой счет: {score}')
            bot.send_message(message.from_user.id, f'Попробуй еще раз, может получится лучше!')
        bot.send_message(message.from_user.id, 'Напиши /start чтобы попробовать еще раз')
        bot.register_next_step_handler(message, ru_get_text_messages)
    elif message.text == '/help':
        bot.send_message(message.from_user.id,'Правила просты как и в оригинальной игре:\n'
        'Пишешь слово, я отвечаю словом которое начинается на ту же букву, какой оканчивается твое.\n'
        'Если слово бота заканчивается на ый, пиши слово на 3 букву с конца, если на ь, ъ, ы или й на 2\n'
        'Для того чтобы закончить игру, напиши /end')
        bot.register_next_step_handler(message, ru_get_new_word)
    else:
        user_word = message.text

        if user_word in list_of_user_words:
            bot.send_message(message.from_user.id, "Ты проиграл! Ты уже писал это слово!")
            if score > best_score:
                best_score = score
                bot.send_message(message.from_user.id, f'Ты поставил новый рекорд, со счетом: {best_score}')
            elif score < best_score:
                bot.send_message(message.from_user.id, f'Твой счет: {score}')
                bot.send_message(message.from_user.id, f'Попробуй еще раз, может получится лучше!')
            bot.send_message(message.from_user.id, 'Напиши /start чтобы попробовать еще раз')
            total_attempts += 1
            bot.register_next_step_handler(message, ru_get_text_messages)
        elif user_word[0] == bot_word[-1] or first_try or bot_word.__contains__('ый') or (bot_word[-1] in ('ы', 'ь', 'ъ', 'й') and bot_word[-2] == user_word[0]):
            first_try = False
            try:
                if message.text.isdigit():
                    raise ValueError
                elif not (message.text.isalpha()):
                    raise ValueError
            except ValueError:
                bot.send_message(message.from_user.id, "Введи слово!")
                first_try = True
                bot.register_next_step_handler(message, ru_get_new_word)
            else:

                if user_word[-1] in ('ы', 'ь', 'ъ') and not(bot_word.__contains__('ый')):
                    letter = user_word[-2]
                #elif bot_word.__contains__('ый'):
                    #letter = user_word[-3]
                else:
                    letter = user_word[-1]


                base_url = "https://bezbukv.ru/mask/"
                url = base_url + letter + "$"

                response = requests.get(url)
                html_page = BeautifulSoup(response.content, "lxml")

                max_pages = html_page.find_all("li", class_="last")
                try:
                    last_href = str(max_pages[0].getText)
                    ravno_pos = last_href.rfind('=')
                    end_num = last_href.rfind('"')
                    max_pages = int(last_href[ravno_pos + 1:end_num])
                except:
                    max_pages = 20

                url = base_url + letter + '%24?page=' + str(random.randint(1, max_pages))
                response = requests.get(url)
                html_page = BeautifulSoup(response.content, "lxml")

                word_on_page = html_page.find_all('div', class_='view')
                try:
                    word = word_on_page[random.randint(0, len(word_on_page))].get_text()
                except:
                    bot.send_message(message.from_user.id, "Что-то не то написал, давай еще раз")
                    first_try = True
                    bot.register_next_step_handler(message, ru_get_new_word)
                    return
                for i in range(len(word)):
                    if not word[i].isalpha():
                        continue
                    else:
                        bot_word = word[i::].strip()
                        break

                response.close()

                bot.send_message(message.from_user.id, bot_word.capitalize())
                if score > 3:
                    if random.randint(1,4) == 1:
                        bot.send_message(message.from_user.id, random.choice(mockery).capitalize())


                score += 1
                list_of_user_words.append(user_word)
                list_of_bot_words.append(bot_word)
                bot.register_next_step_handler(message, ru_get_new_word)
        else:
            bot.send_message(message.from_user.id, "Игра окончена!")
            if score > best_score:
                best_score = score
                bot.send_message(message.from_user.id, f'Ты поставил новый рекорд, со счетом: {best_score}')
            elif score < best_score:
                bot.send_message(message.from_user.id, f'Твой счет: {score}')
                bot.send_message(message.from_user.id, f'Попробуй еще раз, может получится лучше!')
            bot.send_message(message.from_user.id, 'Напиши /start чтобы попробовать еще раз')
            total_attempts += 1
            bot.register_next_step_handler(message, ru_get_text_messages)


bot.polling(none_stop=True, interval=0)
