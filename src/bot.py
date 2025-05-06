import asyncio
from aiogram import Bot, Dispatcher
from config.config import BOT_TOKEN
from handlers import routers
from middleware import UserMiddleware


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    
    dp.message.middleware(UserMiddleware())


    for router in routers:
        dp.include_router(router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
