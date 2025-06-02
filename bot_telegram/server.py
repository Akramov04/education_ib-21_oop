import telebot
import random
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import TOKEN
from quotes import quotes

bot = telebot.TeleBot(TOKEN)

user_data = {
    "selected_authors": {},
    "viewed_quotes": {},
    "last_message_id": {}
}


@bot.message_handler(commands=['start'])
def handle_start(message):
    user_id = message.chat.id
    markup = create_main_keyboard(user_id)

    if user_id not in user_data["selected_authors"]:
        user_data["selected_authors"][user_id] = []

    first_quote = get_random_quote(user_id)
    welcome_message = f"Добро пожаловать! Это бот с лучшими цитатами известных людей. Выберите авторов для цитат или оставьте все:\n\n{first_quote}"
    sent_message = bot.send_message(user_id, welcome_message, reply_markup=markup, parse_mode="Markdown")

    user_data["last_message_id"][user_id] = sent_message.message_id


def create_main_keyboard(user_id):
    selected = user_data["selected_authors"].get(user_id, [])
    markup = InlineKeyboardMarkup(row_width=2)

    author_buttons = []
    for author in get_all_authors():
        status = "✅" if author in selected else ""
        author_buttons.append(InlineKeyboardButton(f"{status} {author}", callback_data=f"author_{author}"))

    markup.add(*author_buttons)
    markup.add(
        InlineKeyboardButton("📚 Следующая цитата", callback_data="next"),
        InlineKeyboardButton("⚙️ Настройки", callback_data="settings")
    )
    markup.add(
        InlineKeyboardButton("🔄 Сбросить выбор", callback_data="reset")
    )

    return markup


def get_all_authors():
    return list(set(q["author"] for q in quotes))


def get_random_quote(user_id):
    selected_authors = user_data["selected_authors"].get(user_id, [])
    viewed = user_data["viewed_quotes"].get(user_id, [])

    filtered = []
    for q in quotes:
        if (not selected_authors or q["author"] in selected_authors) and q not in viewed:
            filtered.append(q)

    if not filtered:
        user_data["viewed_quotes"][user_id] = []
        return "Все доступные цитаты просмотрены! Начинаем сначала...\n\n" + random.choice(quotes)["text"]

    quote = random.choice(filtered)
    user_data["viewed_quotes"].setdefault(user_id, []).append(quote)
    return f"_{quote['author']}_\n{quote['text']}"


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    user_id = call.message.chat.id
    data = call.data

    if data == "next":
        quote = get_random_quote(user_id)
        markup = create_main_keyboard(user_id)
        bot.edit_message_text(
            chat_id=user_id,
            message_id=user_data["last_message_id"][user_id],
            text=quote,
            reply_markup=markup,
            parse_mode="Markdown"
        )
    elif data.startswith("author_"):
        author = data.split("_")[1]
        selected = user_data["selected_authors"].get(user_id, [])

        if author in selected:
            selected.remove(author)
        else:
            selected.append(author)

        user_data["selected_authors"][user_id] = selected
        markup = create_main_keyboard(user_id)
        bot.edit_message_reply_markup(user_id, user_data["last_message_id"][user_id], reply_markup=markup)
    elif data == "reset":
        user_data["selected_authors"][user_id] = []
        user_data["viewed_quotes"][user_id] = []
        markup = create_main_keyboard(user_id)
        bot.edit_message_reply_markup(user_id, user_data["last_message_id"][user_id], reply_markup=markup)
        bot.answer_callback_query(call.id, "Выбор авторов сброшен!")
    elif data == "settings":
        show_settings_menu(call.message)
    elif data == "back":
        markup = create_main_keyboard(user_id)
        bot.edit_message_text(
            chat_id=user_id,
            message_id=user_data["last_message_id"][user_id],
            text=get_current_quote_text(user_id),
            reply_markup=markup,
            parse_mode="Markdown"
        )


def get_current_quote_text(user_id):
    if user_data["viewed_quotes"].get(user_id):
        return get_random_quote(user_id)
    return "Добро пожаловать! Выберите авторов для цитат или оставьте все:"


def show_settings_menu(message):
    user_id = message.chat.id
    selected_authors = user_data["selected_authors"].get(user_id, [])
    current_authors = ", ".join(selected_authors) if selected_authors else "Все авторы"

    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("🔙 Вернуться", callback_data="back")
    )

    bot.edit_message_text(
        chat_id=user_id,
        message_id=user_data["last_message_id"][user_id],
        text=f"⚙️ Настройки:\n\nТекущие авторы: {current_authors}",
        reply_markup=markup,
        parse_mode="Markdown"
    )


if __name__ == "__main__":
    print("Бот запущен...")
    bot.infinity_polling()