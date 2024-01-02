import telebot
from telebot import types

from bs4 import BeautifulSoup
import requests, random

bot = telebot.TeleBot(('6937234108:AAGuTKWvrHfAEf_yvnja7LmMHbBY2iFxUP4'))


name = ''
surname = ''
age = 0

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    print(message.text)
    if message.text == 'Привет' or message.text == 'Привет!' or message.text == 'привет' or message.text == 'привет!':
        bot.send_message(message.from_user.id, 'Какой послушный, ну ладно, двигаем дальше!'
                                               '\nНапиши /reg для регистрации')
    elif message.text == '/help':
        bot.send_message(message.from_user.id, 'Напиши привет!')
    elif message.text == '/reg':
        bot.send_message(message.from_user.id, "Напиши свое имя")
        bot.register_next_step_handler(message, get_name)
    elif message.text == '/start':
        bot.send_message(message.from_user.id, "Напиши слово какое-нибуть")
        bot.register_next_step_handler(message, get_new_word)
    else:
        bot.send_message(message.from_user.id, 'Напиши /help, если что!)')

def get_name(message):
    print(message.text)
    global name
    try:
        if not (message.text.isalpha()):
            raise ValueError
    except ValueError:
        bot.send_message(message.from_user.id, "Введи слово!")
        bot.register_next_step_handler(message, get_name)
    else:
        name = message.text
        bot.send_message(message.from_user.id, 'Напиши свою фамилию')
        bot.register_next_step_handler(message, get_surname)
def get_surname(message):
    print(message.text)
    global surname
    try:
        if not (message.text.isalpha()):
            raise ValueError
    except ValueError:
        bot.send_message(message.from_user.id, "Введи слово!")
        bot.register_next_step_handler(message, get_surname)
    else:
        surname = message.text
        bot.send_message(message.from_user.id, 'Напиши свой возраст')
        bot.register_next_step_handler(message, get_age)



def get_age(message):
    print(message.text)
    global age
    try:
        age = int(message.text)
    except ValueError:
        bot.send_message(message.from_user.id, 'Тут должно быть число!')
        bot.register_next_step_handler(message, get_age)
    else:
        bot.send_message(message.from_user.id, 'Ты успешно зарегистрировался!')
        bot.send_message(message.from_user.id, f'Тебя зовут {name} {surname} и тебе {age} лет \nТолько это нигде не будет использоваться, ну да ладно)')
        bot.send_message(message.from_user.id, 'Напиши /start для начала')
        bot.register_next_step_handler(message, start)
def start(message):
    print(message.text)
    if message.text == '/start':
        bot.send_message(message.from_user.id, 'Игра началась! Напиши слово')
        bot.send_message(message.from_user.id, 'Для окончания игры напиши /end')
        bot.register_next_step_handler(message, get_new_word)
    else:
        bot.send_message(message.from_user.id, 'Давай по-новой, напиши /help')


user_word = ''
bot_word = ''

mockery = [
", ну что, даже компьютер быстрее думает!",
", в следующей жизни попробуй выбрать что-то короче",
", слова-ответы, как карликовая эстафета",
", ты точно не отыгрываешь роль зомби в словах?",
" а где кнопка ""Ускоренная Печать""?",
", это не спринт, чтобы так долго загружаться",
", ты уверен, что клавиши не залипли?",
", даже улитка быстрее ползает",
", думаешь, где-то есть рекорд по медлительности?",
", это не сон, чтобы вяло тянуться",
", как на дороге - тормозишь на каждом слове!",
", даже калькулятор быстрее подсчитает",
", это не вечность, чтобы так долго висеть в воздухе",
", слова бегут, а ты стоишь на старте",
", у тебя что, клавиши на пенсию отправили?",
", скорость мысли - не про тебя?",
", не в лесу, а словах заблудился?",
", народ уже заснул, дожидаясь твоего следующего слова",
", это не кроссворд, чтобы так замедляться",
", слова, как котики - не любят долго ждать",
", ты не торт, чтобы расползаться со словом",
", даже ленивец бы устал от такого темпа",
", не на треке, чтобы бежать по кругу",
", слова в рекордное время на выводе!",
", не слова, а словесная пауза!",
", не детектив, чтобы так медленно раскрываться",
", даже в шахматах быстрее ходят!",
", как долго тебе нужно было подумать?",
", а я думал, это слово на экспрессе!",
", ну что, дальше плавно переходим к азбуке?",
", это слово, или ты случайно пошутил?",
", не угадал, держи билет в словарь.",
", у меня уже дождь прошел, а ты только начал.",
", даже старик в деревне быстрее угадывает.",
", ну что, дальше или уже устал?",
", даже моя кофеварка быстрее работает.",
", это слово на каникулах, поэтому так долго.",
", я ведь прошу просто слово, не оперу.",
", сколько тебе нужно времени на одно слово?",
", я чуть не заснул, пока ты думал.",
", такие слова тут как гости - не задерживаются."]

def get_new_word(message):
    print(message.text)
    try:
        if message.text == '/end':
            bot.send_message(message.from_user.id, 'Игра окончена!')
            bot.register_next_step_handler(message,get_text_messages)
        elif message.text.isdigit():
            raise ValueError
        elif not (message.text.isalpha()):
            raise ValueError
    except ValueError:
        bot.send_message(message.from_user.id, "Введи слово!")
        bot.register_next_step_handler(message, get_new_word)
    else:
        print(message.text)
        global bot_word
        global user_word
        user_word = message.text

        base_url = "https://bezbukv.ru/mask/"
        letter = user_word[-1]
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
            message.text = "daslkd"
            bot.register_next_step_handler(message, get_new_word)
            return
        for i in range(len(word)):
            if not word[i].isalpha():
                continue
            else:
                bot_word = word[i::].strip()
                break
        print("\n" + user_word)
        print(bot_word)

        response.close()

        bot.send_message(message.from_user.id, f'Слово: {bot_word}{random.choice(mockery)}')
        bot.register_next_step_handler(message, get_new_word)



bot.polling(none_stop=True, interval=0)