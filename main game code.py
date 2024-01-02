from bs4 import BeautifulSoup
import requests, random

bot_word = ''
user_word = 'asdasdasd'
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


message = 'кувалда'
def get_new_word(message):
    global bot_word
    global user_word

    print(user_word)
    user_word = str(message)
    print(user_word)

    base_url = "https://bezbukv.ru/mask/"
    print(user_word)
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
    word = word_on_page[random.randint(0, len(word_on_page) - 1)].get_text()
    for i in range(len(word)):
        if not word[i].isalpha():
            continue
        else:
            bot_word = word[i::].strip()
            break
    print("\n" + user_word)
    print(bot_word)

    response.close()

get_new_word('')

