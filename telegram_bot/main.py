import asyncio
import logging

from aiogram import Bot, Dispatcher

from telegram_bot.bot.config import Settings
from telegram_bot.bot.handlers import router


async def main() -> None:
    settings = Settings.from_env()
    bot = Bot(token=settings.bot_token)
    dispatcher = Dispatcher()
    dispatcher.include_router(router)

    logging.info("Бот запускается в режиме long polling")
    try:
        await dispatcher.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Бот остановлен")
