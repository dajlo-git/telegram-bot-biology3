import telebot
import os
from telebot import types
import threading

bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))

# --- Словарь для хранения File ID ---
file_ids = {
    "grade7": [],
    "grade8": [],
    "grade9": [],
    "grade10": [],
    "grade11": [],
    "grade12": []
}

# --- Меню ---
def get_start_markup():
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton("Нұсқа талдаулар📷", callback_data="btn1")
    btn2 = types.InlineKeyboardButton("Чек-листтер📁", callback_data="btn2")
    btn3 = types.InlineKeyboardButton("Оқулықтар тізімі📚", callback_data="btn3")
    btn4 = types.InlineKeyboardButton("Биологиядан ҰБТ спецификациясы📄", callback_data="btn4")
    btn6 = types.InlineKeyboardButton("JUZ40 әлеуметтік желіде📱", callback_data="btn5")
    btn5 = types.InlineKeyboardButton(" Аура✨", callback_data="aura")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    return markup

def send_aura_files(chat_id):
    aura_files = [
            "./Аура-1.pdf",
            "./Аура-2.pdf",
            "./Аура-3.pdf",
            "./Аура-4.pdf",
            "./Аура-6.pdf",
            "./Аура-7.pdf",
            "./Аура-8.pdf",
            "./Аура-10.pdf",
        ]

    for file_path in aura_files:
        try:
            with open(file_path, "rb") as f:
                    bot.send_document(chat_id, f)
        except FileNotFoundError:
            bot.send_message(chat_id, f"Файл {file_path} табылмады ❌")


def get_checklist_markup():
    markup = types.InlineKeyboardMarkup(row_width=1)

    topics = [
        ("Тірі ағзалардың көптүрлілігі🐾", "check_1"),
        ("Қоректену🍭", "check_2"),
        ("Заттардың тасымалдануы🩸", "check_3"),
        ("Тыныс алу🩻", "check_4"),
        ("Бөліп шығару🗑", "check_5"),
        ("Қозғалыс. Биофизика🦾", "check_6"),
        ("Координация және реттелу🧠", "check_7"),
        ("Көбею. Өсу және даму🧬", "check_8"),
        ("Жасушалық айналым. Жасушалық биология🦠", "check_9"),
        ("Тұқым қуалаушылық пен өзгергіштік заңдылықтары🩺", "check_10"),
        ("Молекулалық биология мен биохимия🧫", "check_11"),
        ("Микробиология және биотехнология. Биомедицина🧪", "check_12"),
    ]

    for text, data in topics:
        markup.add(types.InlineKeyboardButton(text, callback_data=data))

    markup.add(types.InlineKeyboardButton("⬅ Кері қайту", callback_data="back"))
    return markup

def get_juz40_markup():
    markup = types.InlineKeyboardMarkup(row_width=1)

    insta = types.InlineKeyboardButton(
        "140 Instagram 📸",
        url="https://www.instagram.com/juz40_online/"
    )
    platform = types.InlineKeyboardButton(
        "140 Платформа 🌐",
        url="https://juz40-edu.kz/"
    )
    telegram = types.InlineKeyboardButton(
        "140 Telegram 💬",
        url="https://t.me/s/juz40_online"
    )
    back = types.InlineKeyboardButton("⬅ Кері қайту", callback_data="back")

    markup.add(insta, platform, telegram, back)
    return markup


def get_classes_markup():
    markup = types.InlineKeyboardMarkup()
    btn7 = types.InlineKeyboardButton("7 сынып", callback_data="grade7")
    btn8 = types.InlineKeyboardButton("8 сынып", callback_data="grade8")
    btn9 = types.InlineKeyboardButton("9 сынып", callback_data="grade9")
    btn10 = types.InlineKeyboardButton("10 сынып", callback_data="grade10")
    btn11 = types.InlineKeyboardButton("11 сынып", callback_data=" grade11")
    back = types.InlineKeyboardButton("⬅ Кері қайту", callback_data="back")
    books = types.InlineKeyboardButton(
        "📚 Оқулықтар (Google Disk)",
        callback_data="books_google"
    )

    back = types.InlineKeyboardButton("⬅ Кері қайту", callback_data="back")

    markup.add(btn7, btn8, btn9, btn10, btn11)
    markup.add(books)
    markup.add(back)

    return markup



def get_teachers_markup():
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton("Айтуған ағай", callback_data="teacher1")
    btn2 = types.InlineKeyboardButton("Айбота апай", callback_data="teacher2")
    btn3 = types.InlineKeyboardButton("Мират ағай", callback_data="teacher3")
    btn4 = types.InlineKeyboardButton("Нұрасыл ағай", callback_data="teacher4")
    btn5 = types.InlineKeyboardButton("Жасұлан ағай", callback_data="teacher5")
    btn6 = types.InlineKeyboardButton("Ботагөз апай", callback_data="teacher6")
    btn7 = types.InlineKeyboardButton("НТ ГУГЛ ДИСК", callback_data="teacher7")
    back = types.InlineKeyboardButton("⬅ Кері қайту", callback_data="back")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, back)
    return markup

# Словарь с ссылками для преподавателей
teacher_links = {
    "teacher1": "Айтуған ағай : https://docs.google.com/document/d/14JHtZRqtDnyRlZRooP0B4yuFf2uxcY48bNMLdorOAj4/edit?usp=drivesdk",
    "teacher2": "Айбота апай : https://docs.google.com/document/d/1a6AVsd_qgfmxB0V1ru1TgCGaL2MRWnf1/edit?usp=drivesdk",
    "teacher3": "Мират ағай : https://docs.google.com/document/d/147EDLYZM84hAxQwaqX2f4KmBARhC4Q5uCeWnVcHdys4/edit?usp=drivesdk",
    "teacher4": "Нұрасыл ағай : https://docs.google.com/document/d/13S900yvVCWhTsCWtzuDI2s-AEKmlTE9YX3ffj0myKQc/edit?usp=drivesdk",
    "teacher5": "Жасұлан ағай : https://docs.google.com/document/d/14TEZaiSDpE7uruaJN5wh0fGAsHaRfNGhoLFaZ-UAVmU/edit?usp=drivesdk",
    "teacher6": "Ботагөз апай : https://docs.google.com/document/d/14SzM7nN4c0tnytBWd8k5pYudDz0YD6cvp4nxAcvUsCQ/edit?usp=drivesdk",
    "teacher7": "НТ ГУГЛ ДИСК : https://docs.google.com/spreadsheets/d/1yMKy_GbOSO6v-BNzpmZLJqm7gOXGTx6Qli8PPJ1-QYc/edit?usp=sharing"
}

# --- Функция отправки файлов ---
def send_files(chat_id, class_name, class_files_map):
    files = class_files_map[class_name]
    for i, file_path in enumerate(files):
        try:
            if len(file_ids[class_name]) > i:
                bot.send_document(chat_id, file_ids[class_name][i])
            else:
                with open(file_path, "rb") as f:
                    msg = bot.send_document(chat_id, f)
                    file_ids[class_name].append(msg.document.file_id)
        except FileNotFoundError:
            bot.send_message(chat_id, f"Файл {file_path} не найден!")

# --- Старт ---
@bot.message_handler(content_types=['start','text'])
def start(message):
    bot.send_message(
        message.chat.id,
        f"Сәлем, {message.from_user.first_name}👋 Биологияны меңгеруге дайынсың ба? Бастау үшін төмендегі батырмаларды қолданып, материалдарды қолдана аласың👇🏻 ",
        reply_markup=get_start_markup()
    )

# --- Callback ---
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    bot.answer_callback_query(call.id)

    # Меню классов
    if call.data == "btn3":
        bot.edit_message_text(
            "Сыныпты таңдаңыз🔢:",
            call.message.chat.id,
            call.message.message_id,
            reply_markup=get_classes_markup()
        )

    # Выбор класса
    elif call.data in ["grade7","grade8","grade9","grade10","grade11"]:
        class_files_map = {
            "grade7": ["./7-сынып Атамұра.pdf", "./7-сынып Очкур.pdf"],
            "grade8": ["./8-сынып биология.pdf"],
            "grade9": ["./9-сынып биология.pdf"],
            "grade10": ["./10-сынып 1-бөлім.pdf", "./10-сынып 2-бөлім.pdf"],
            "grade11": ["./11-сынып 1-бөлім.pdf", "./11-сынып 2-бөлім.pdf"],
        }
        threading.Thread(target=send_files, args=(call.message.chat.id, call.data, class_files_map)).start()
        bot.send_message(call.message.chat.id, "Файл жүктелу үстінде🌀:", reply_markup=get_classes_markup())


    elif call.data == "books_google":
        bot.send_message(
            call.message.chat.id,
            "📚 Оқулықтар Google Disk сілтемесі:\n\n"
            "https://drive.google.com/drive/folders/13wELpxz1axITUpKVy5WOfa482GIsxwxa"
        )


    # Меню "Нұсқа талдаулар"
    elif call.data == "btn1":
        bot.edit_message_text(
            "Мұғалімді таңдаңыз:",
            call.message.chat.id,
            call.message.message_id,
            reply_markup=get_teachers_markup()
        )

    # Кнопки преподавателей
    elif call.data in ["teacher1","teacher2","teacher3","teacher4","teacher5","teacher6", "teacher7"]:
        link_text = teacher_links[call.data]
        bot.send_message(call.message.chat.id, link_text)
        bot.send_message(call.message.chat.id, "Мұғалімді таңдаңыз:", reply_markup=get_teachers_markup())

    # Кнопка "Биология бойынша специфика"
    elif call.data == "btn4":
        file_path = './biolist.pdf'
        try:
            with open(file_path, 'rb') as f:
                bot.send_document(call.message.chat.id, f)
        except FileNotFoundError:
            bot.send_message(call.message.chat.id, f"Файл {file_path} не найден!")
        bot.edit_message_text(
            "Таңдауды жалғастырыңыз😄:",
            call.message.chat.id,
            call.message.message_id,
            reply_markup=get_start_markup()
        )

    elif call.data == "btn2":
        bot.send_message(
            call.message.chat.id,
            "📁 Чек-листтер сілтемесі:\n\nhttps://drive.google.com/drive/folders/1XDAXnI1E8yh0o8DT6feHCzOJSajxYrnS?usp=drive_link"
    )


    elif call.data == "btn5":
        bot.edit_message_text(
            "📱 JUZ40 әлеуметтік желілері\n\n"
            "Төмендегі батырмалар арқылы біздің ресми парақшаларға өте аласыз👇",
            call.message.chat.id,
            call.message.message_id,
            reply_markup=get_juz40_markup()
        )

    elif call.data == "aura":
        bot.send_message(call.message.chat.id, "Аура файлдары жүктелуде ✨")
        threading.Thread(
            target=send_aura_files,
            args=(call.message.chat.id,)
        ).start()



    # Кнопка "Кері қайту"
    elif call.data == "back":
        bot.edit_message_text(
            "Өзіңізге керек бөлімді таңдаңыз:",
            call.message.chat.id,
            call.message.message_id,
            reply_markup=get_start_markup()
        )

bot.polling(none_stop=True)


