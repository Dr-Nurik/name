import asyncio
import sys
from aiogram import Bot

async def send_broadcast_message(token, message):
    bot = Bot(token=token)
    # Получите список всех chat_id из вашей базы данных
    chat_ids = []  # Замените этот список реальными ID чатов
    for chat_id in chat_ids:
        try:
            await bot.send_message(chat_id, message)
        except Exception as e:
            print(f"Ошибка отправки сообщения: {e}")
    await bot.close()

if __name__ == "__main__":
    # Первый аргумент командной строки - токен бота, второй - сообщение
    asyncio.run(send_broadcast_message(sys.argv[1], sys.argv[2]))
