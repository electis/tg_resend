from config import config, logger


def log_message(message, chat=True):
    text = "Message:\n"
    if chat:
        text += f"{message.chat.title} ({message.chat.id})\n"
    if message.from_user:
        text += f"{message.from_user.full_name} ({message.from_user.id}) {message.from_user.username}\n"
    text += f"{message.text}"
    logger.info(text)


async def check_boss(message):
    if str(message.from_user.id) == config.BOSS_ID:
        return True
