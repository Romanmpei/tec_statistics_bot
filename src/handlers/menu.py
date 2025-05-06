from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from db import SessionLocal, Statistic


router = Router()

# Команда /menu с основными кнопками
@router.message(Command("menu"))
async def cmd_menu(message: types.Message):
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Показать статистику")],
            [KeyboardButton(text="О боте")]
        ],
        resize_keyboard=True
    )
    await message.answer("Выберите действие:", reply_markup=kb)

@router.message(lambda m: m.text == "Показать статистику")
async def show_categories(message: types.Message):
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="⚡ Электроэнергетика")],
            [KeyboardButton(text="🔥 Теплоснабжение")],
            [KeyboardButton(text="🛢 Нефть"), KeyboardButton(text="💨 Газ")],
            [KeyboardButton(text="🪨 Уголь")],
            [KeyboardButton(text="↩️ Назад в меню")]
        ],
        resize_keyboard=True,
        input_field_placeholder="Выберите направление ТЭК"
    )
    await message.answer("📊 Показатели ТЭК — выберите категорию:", reply_markup=kb)

# Обработка выбора категории → показать inline-кнопки годов
@router.message(lambda m: m.text in [
    "⚡ Электроэнергетика",
    "🔥 Теплоснабжение",
    "🛢 Нефть",
    "💨 Газ",
    "🪨 Уголь",
    "📋 Сводка по ТЭК"
])

async def category_selected(message: types.Message):
    category = message.text
    inline_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="2024", callback_data=f"{category}_2024"),
                InlineKeyboardButton(text="2023", callback_data=f"{category}_2023"),
            ],
            [
                InlineKeyboardButton(text="2022", callback_data=f"{category}_2022"),
                InlineKeyboardButton(text="2021", callback_data=f"{category}_2021"),
            ],
        ]
    )
    await message.answer(f"📅 Выберите год для категории {category}:", reply_markup=inline_kb)

@router.callback_query(lambda c: any(year in c.data for year in ["2021", "2022", "2023", "2024"]))
async def year_selected(callback: types.CallbackQuery):
    raw_data = callback.data
    for year in ["2021", "2022", "2023", "2024"]:
        if year in raw_data:
            selected_year = year
            break
    category = raw_data.replace(f"_{selected_year}", "")

    session = SessionLocal()
    result = session.query(Statistic).filter_by(category=category, year=selected_year).first()
    session.close()

    if result:
        text = f"📊 Данные по {category} за {selected_year} год:\n{result.text}"
    else:
        text = f"ℹ️ Данных по {category} за {selected_year} год пока нет."

    await callback.message.answer(text)
    await callback.answer()



# Ответ на "О боте"
@router.message(lambda m: m.text == "О боте")
async def about_from_menu(message: types.Message):
    await message.answer("Этот бот создан для отображения статистики в сфере ТЭК.\nРазработка: Roman MPEI 🚀")

@router.message(lambda m: m.text == "↩️ Назад в меню")
async def back_to_menu(message: types.Message):
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Показать статистику")],
            [KeyboardButton(text="О боте")]
        ],
        resize_keyboard=True
    )
    await message.answer("↩️ Возврат в главное меню", reply_markup=kb)
