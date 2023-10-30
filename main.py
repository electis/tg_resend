import asyncio

from aiogram import Bot, Dispatcher

from config import config, logger
from handlers import router


async def run_bot():
    bot = Bot(token=config.BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logger.warning('Starting bot')
    try:
        asyncio.run(run_bot())
    except (SystemExit, KeyboardInterrupt):
        logger.warning('Bot stopped')
