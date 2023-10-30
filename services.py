from config import config, logger


def log_message(message, chat=True):
    text = ""
    if chat:
        text += f"{message.chat.id}, {message.chat.title}\n"
    text += f"{message.from_user.id}, {message.from_user.username}, {message.from_user.full_name}\n"
    text += f"{message.text}"
    logger.info(text)


async def check_boss(message):
    if str(message.from_user.id) == config.BOSS_ID:
        return True
