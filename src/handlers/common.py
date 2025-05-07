from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
	"Привет! Я бот для отображения статистики ТЭК 🚀\n\n"
        "📊 Могу показать тебе основные данные по направлениям ТЭК России за 2021–2024 гг.\n\n"
        "👉 Нажми кнопку меню или введи команду /menu для начала.\n"
        "Если нужна помощь — используй /help."
    )

@router.message(Command("help"))
async def cmd_help(message: types.Message):
    help_text = (
        "Доступные команды:\n"
        "/start — Начать работу\n"
        "/help — Справка\n"
        "/about — О боте\n"
        "/menu — Кнопки\n"
    )
    await message.answer(help_text)

@router.message(Command("about"))
async def cmd_about(message: types.Message):
    await message.answer(
        "📌 Бот статистика ТЭК создан для всех, кому нужно иметь под рукой основную статистическую информацию" 
        "о ключевых направлениях ТЭК.\n\n"
        "📈 Данные могут быть расширены или можно разработать индивидуальный бот.\n\n"
        "🔒 Бот не собирает персональные данные.\n"
        "📚 Используются только открытые и официальные источники:\n"
        "- отчеты о функционировании ЕЭС России от АО СО ЕЭС.\n"
        "- энергетическая стратегия до 2050 года.\n"
        "- отчет о состоянии теплоэнергетики Минэнерго.\n"
        "- отчеты Росстата.\n"
        "- данные из ЕМИСС.\n"
        "🗃 Публичный репозиторий проекта доступен для всех желающих.\n\n"
        "👨‍💻 Разработчик: Intodex\n"
        "Telegram: @intodex\n"
        "Email: mail@tointodex.ru\n"
        "Website: https://intodex.ru"
     )
