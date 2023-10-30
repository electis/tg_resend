from aiogram import Bot, F, Router
from aiogram.types import Message
from aiogram.enums import ChatType, ContentType

from config import config, logger
from services import check_boss, log_message

router = Router(name=__name__)


@router.message(F.chat.type == ChatType.PRIVATE)
async def private(message: Message, bot: Bot):
    log_message(message, chat=False)
    if await check_boss(message):
        # bot.get_chat_member(chat_id, bot_id)
        await message.send_copy(config.CHAT_ID)
    else:
        await message.answer("You are not the boss 🤷‍♂️")
        # await message.answer("Добавьте бота в группу и назначьте администратором")


@router.message(F.chat.type.in_({ChatType.GROUP, ChatType.SUPERGROUP, ChatType.CHANNEL}))
async def group(message: Message):
    if message.content_type == ContentType.NEW_CHAT_MEMBERS and message.model_extra.get('new_chat_member', {}).get('id') == message.bot.id:
        logger.warning(f"Added to {message.chat.id} by {message.from_user.id}")
    if message.left_chat_member and message.model_extra.get('left_chat_participant', {}).get('id') == message.bot.id:
        logger.warning(f"Removed from {message.chat.id} by {message.from_user.id}")