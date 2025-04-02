import asyncio
import os
import time
from aiogram import Bot, Dispatcher
from dotenv import find_dotenv, load_dotenv
from handlers.user_private import user_router
import aiohttp
load_dotenv(find_dotenv())

bot = Bot(token=os.getenv('TOKEN'))

dp = Dispatcher()


dp.include_router(user_router)

allw_upd=['message','edited_message']







async def main_logic():
    print("Программа работает. Нажми Ctrl+C для прерывания.")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowedupdates=allw_upd)

async def shutdown():
    print("Завершение программы...")
    await bot.delete_webhook(drop_pending_updates=True)
    print("Программа завершена. Спасибо!")

async def main():
    try:
        await main_logic()
    except asyncio.CancelledError:
        print("Получен сигнал отмены, завершаем работу...")
        await shutdown()
    except KeyboardInterrupt:
        print("Получен сигнал прерывания, завершаем работу...")
        await shutdown()
  
asyncio.run(main())