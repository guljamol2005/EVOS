from asyncio import run
from aiogram import Bot, Dispatcher, types, F
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton,FSInputFile


def get_product_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="-", callback_data="decrease"),
            InlineKeyboardButton(text="1", callback_data="quantity"),
            InlineKeyboardButton(text="+", callback_data="increase"),
        ],
        [
            InlineKeyboardButton(text="🛒 Savatga qo'shish", callback_data="add_to_cart")
        ]
    ])


async def Comboplusisit_handler(message: types.Message):

    photo = FSInputFile(r"C:\Users\PC_ACER\Downloads\Telegram Desktop\photo_2025-06-19_18-42-16.jpg")
    caption = "🥙 <b>Combo Plus Isituvchan (Qora choy)</b>\nNarxi: 16 000 so'm"
    await message.answer_photo(photo=photo, caption=caption, reply_markup=get_product_keyboard())


user_main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Menyu")],
        [KeyboardButton(text="Mening buyurtmalarim")],
        [KeyboardButton(text="Savat"), KeyboardButton(text="Aloqa")],
        [KeyboardButton(text="Xabar yuborish"), KeyboardButton(text="Sozlamalar")],
        [KeyboardButton(text="Biz haqimizda")],

    ],
    resize_keyboard=True,
    is_persistent=True
)

user_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Setlar(8)")],
        [KeyboardButton(text="Lavash(9)"), KeyboardButton(text="Shaurma")],
        [KeyboardButton(text="Burger(4)"), KeyboardButton(text="Hot-Dog(8)")],
        [KeyboardButton(text="Ichimliklar(11)")],
        [KeyboardButton(text="Shirinlik va disertlar(4)")],
        [KeyboardButton(text="Garnirlar(10)")],
        [KeyboardButton(text="Orqaga qaytish")],

    ],
    resize_keyboard=True,
    is_persistent=True
)

user_menu_setlar_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Combo Plus Isituvchan(Qora choy)"), KeyboardButton(text="FitCombo")],
        [KeyboardButton(text="Iftar kofte grill mol go'shtidan"), KeyboardButton(text="Donar boks mol go'shtidan")],
        [KeyboardButton(text="Donar boks tovuq go'shtidan"), KeyboardButton(text="COMBO+")],
        [KeyboardButton(text="Iftar strips tovuq go'shtidan"), KeyboardButton(text="Kids COMBO")],
        [KeyboardButton(text="Orqaga qaytish")],

    ],
    resize_keyboard=True,
    is_persistent=True
)
user_menu_lavash_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Mol go'shtidan qalampir lavash"), KeyboardButton(text="Tovuq go'shtidan qalampir lavash")],
        [KeyboardButton(text="Mol go'shtidan pishloqli lavash"), KeyboardButton(text="Tovuq go'shtidan pishloqli lavash")],
        [KeyboardButton(text="FITTER"), KeyboardButton(text="Lavash tovuq go'sht")],
        [KeyboardButton(text="Lavash mol go'sht")],
        [KeyboardButton(text="Orqaga qaytish")],

    ],
    resize_keyboard=True,
    is_persistent=True
)

user_menu_shaurma_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Shaurma qalampir mol go'sht"), KeyboardButton(text="Shaurma tovuq go'sht")],
        [KeyboardButton(text="Shaurma qalampir tovuq go'sht"), KeyboardButton(text="Shaurma mol go'sht")],
        [KeyboardButton(text="Orqaga qaytish")],

    ],
    resize_keyboard=True,
    is_persistent=True
)
user_menu_burger_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Gamburger"), KeyboardButton(text="Double burger")],
        [KeyboardButton(text="Cheese burger"), KeyboardButton(text="Double cheese")],
        [KeyboardButton(text="Orqaga qaytish")],

    ],
    resize_keyboard=True,
    is_persistent=True
)

user_menu_hotdog_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Hot-dog baguette"), KeyboardButton(text="Sub tovuq cheese")],
        [KeyboardButton(text="Sub tovuq"), KeyboardButton(text="Hot-dog baguette double")],
        [KeyboardButton(text="Hot-dog kids"), KeyboardButton(text="Sub go'sht cheese")],
        [KeyboardButton(text="Hot-dog classic"), KeyboardButton(text="Sub go'sht")],
        [KeyboardButton(text="Orqaga qaytish")],

    ],
    resize_keyboard=True,
    is_persistent=True
)

user_menu_ichimliklar_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Sok dena 0,33l"), KeyboardButton(text="Suv 0,5")],
        [KeyboardButton(text="Pepsi 0,5l"), KeyboardButton(text="Pepsi 1,5")],
        [KeyboardButton(text="Quyib beriladigan pepsi"), KeyboardButton(text="Bliss sharbati")],
        [KeyboardButton(text="Americano"), KeyboardButton(text="Latte")],
        [KeyboardButton(text="Ko'k choy"), KeyboardButton(text="Qora choy")],
        [KeyboardButton(text="Limonli ko'k choy")],
        [KeyboardButton(text="Orqaga qaytish")],

    ],
    resize_keyboard=True,
    is_persistent=True
)

user_menu_shirinlik_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Medovik Asalim"), KeyboardButton(text="Chizkeyk")],
        [KeyboardButton(text="Donut karameli"), KeyboardButton(text="Donut mevali")],
        [KeyboardButton(text="Orqaga qaytish")],

    ],
    resize_keyboard=True,
    is_persistent=True
)

user_menu_garnirlar_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Ketchup"), KeyboardButton(text="Guruch")],
        [KeyboardButton(text="Pro-devevenski"), KeyboardButton(text="Sarimchoqli qayla")],
        [KeyboardButton(text="Chili qaylasi"), KeyboardButton(text="Mayonez")],
        [KeyboardButton(text="Salat"), KeyboardButton(text="Sir qaylasi")],
        [KeyboardButton(text="Tovuq strips"), KeyboardButton(text="Fri")],
        [KeyboardButton(text="Orqaga qaytish")],

    ],
    resize_keyboard=True,
    is_persistent=True
)

welcome_text = (
    "📜 <b>Xush kelibsiz EVOS!</b>\n"
    "🚶 Siz bilan birga qadam-baqadam!\n"
    "🚗 Yetkazib berish xizmati har kuni 9:00 dan 3:00 gacha. Dam olish kuni yo‘q.\n"
    "☎️ Yagona call-markaz: +998 71 203 12 12\n"
    "☎️ Ishonch telefoni: +998 93 512 05 12\n"
    "📩 Buyurtma berish uchun quyidagi tugmani bosing."
)


async def start_handler(message: types.Message):
    await message.answer(text=welcome_text, parse_mode="HTML")

    text = (
        f"\n\nAssalomu alaykum, "
        f"{message.from_user.mention_html(f'{message.from_user.full_name}')}"
    )
    await message.answer(text=text, reply_markup=user_main_keyboard)


async def menu_handler(message: types.Message):
    text = "Tanlang: "
    await message.answer(text=text, reply_markup=user_menu_keyboard)

async def set_handler(message: types.Message):
    if message.text == "Orqaga qaytish":
        await menu_handler(message)
        return

    photo = FSInputFile(r"C:\Users\PC_ACER\Downloads\Telegram Desktop\photo_2025-06-19_16-59-43.jpg")
    await message.answer_photo(photo=photo, reply_markup=user_menu_setlar_keyboard)

async def lavash_handler(message: types.Message):
    if message.text == "Orqaga qaytish":
        await menu_handler(message)
        return

    photo = FSInputFile(r"C:\Users\PC_ACER\Downloads\Telegram Desktop\photo_2025-06-19_17-56-30.jpg")
    await message.answer_photo(photo=photo, reply_markup=user_menu_lavash_keyboard)

async def shaurma_handler(message: types.Message):
    if message.text == "Orqaga qaytish":
        await menu_handler(message)
        return

    photo = FSInputFile(r"C:\Users\PC_ACER\Downloads\Telegram Desktop\photo_2025-06-19_17-59-41.jpg")
    await message.answer_photo(photo=photo, reply_markup=user_menu_shaurma_keyboard)

async def burger_handler(message: types.Message):
    if message.text == "Orqaga qaytish":
        await menu_handler(message)
        return

    photo = FSInputFile(r"C:\Users\PC_ACER\Downloads\Telegram Desktop\photo_2025-06-19_18-02-14.jpg")
    await message.answer_photo(photo=photo, reply_markup=user_menu_burger_keyboard)

async def hotdog_handler(message: types.Message):
    if message.text == "Orqaga qaytish":
        await menu_handler(message)
        return

    photo = FSInputFile(r"C:\Users\PC_ACER\Downloads\Telegram Desktop\photo_2025-06-19_18-05-32.jpg")
    await message.answer_photo(photo=photo, reply_markup=user_menu_hotdog_keyboard)

async def ichimlik_handler(message: types.Message):
    if message.text == "Orqaga qaytish":
        await menu_handler(message)
        return

    photo = FSInputFile(r"C:\Users\PC_ACER\Downloads\Telegram Desktop\photo_2025-06-19_18-07-32.jpg")
    await message.answer_photo(photo=photo, reply_markup=user_menu_ichimliklar_keyboard)

async def shirinlik_handler(message: types.Message):
    if message.text == "Orqaga qaytish":
        await menu_handler(message)
        return

    photo = FSInputFile(r"C:\Users\PC_ACER\Downloads\Telegram Desktop\photo_2025-06-19_18-10-04.jpg")
    await message.answer_photo(photo=photo, reply_markup=user_menu_shirinlik_keyboard)

async def garnir_handler(message: types.Message):
    if message.text == "Orqaga qaytish":
        await menu_handler(message)
        return

    photo = FSInputFile(r"C:\Users\PC_ACER\Downloads\Telegram Desktop\photo_2025-06-19_18-12-40.jpg")
    await message.answer_photo(photo=photo, reply_markup=user_menu_garnirlar_keyboard)


async def main():
    bot = Bot(
        token="7597032032:AAEwOr2GfnQaRqzN76C44O6bzu3g1dtyoHQ",
        default=DefaultBotProperties(parse_mode='HTML')
    )
    dp = Dispatcher()

    dp.message.register(start_handler, Command('start'))
    dp.message.register(menu_handler, F.text == "Menyu")
    dp.message.register(set_handler, F.text.in_(["Setlar(8)", "Orqaga qaytish"]))
    dp.message.register(lavash_handler, F.text.in_(["Lavash(9)", "Orqaga qaytish"]))
    dp.message.register(set_handler, F.text.in_(["Shaurma(4)", "Orqaga qaytish"]))
    dp.message.register(set_handler, F.text.in_(["Burger(4)", "Orqaga qaytish"]))
    dp.message.register(set_handler, F.text.in_(["Hot-Dog(8)", "Orqaga qaytish"]))
    dp.message.register(set_handler, F.text.in_(["Ichimliklar(11)", "Orqaga qaytish"]))
    dp.message.register(set_handler, F.text.in_(["Shirinlik va disertlar(4)", "Orqaga qaytish"]))
    dp.message.register(set_handler, F.text.in_(["Garnirlar(10)", "Orqaga qaytish"]))
    dp.message.register(Comboplusisit_handler, F.text == "Combo Plus Isituvchan(Qora choy)")

    await dp.start_polling(bot)


if __name__ == '__main__':
    run(main())
