from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я бот для отображения статистики ТЭК 🚀")

@router.message(Command("help"))
async def cmd_help(message: types.Message):
    help_text = (
        "Доступные команды:\n"
        "/start — Начать работу\n"
        "/help — Справка\n"
        "/about — О боте\n"
        "/menu — Кнопки\n"
        "/stats — Показать статистику"
    )
    await message.answer(help_text)

@router.message(Command("about"))
async def cmd_about(message: types.Message):
    await message.answer("Этот бот создан для отображения статистики в сфере ТЭК.\nРазработка: Roman MPEI 🚀")
