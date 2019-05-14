import os
import logging
import telegram
from dotenv import load_dotenv


class LogsHandler(logging.Handler):

    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    def emit(self, record):
        log_entry = self.format(record)
        self.bot.send_report(log_entry)


class BotLogger:
    def __init__(self, token, chat_id):
        self.token = token
        self.chat_id = chat_id
        self.bot = telegram.Bot(self.token)

    def send_report(self, msg):
        self.bot.send_message(chat_id=self.chat_id, text=msg)

    @staticmethod
    def create_logger(logs_handler):
        logger = logging.getLogger('Bot Logger')
        handler = logs_handler
        handler.setFormatter(logging.Formatter('%(message)s'))
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        return logger


load_dotenv()
bot_logger = BotLogger(os.getenv('LOGGER_BOT'), os.getenv('CHAT_ID'))
logger = BotLogger.create_logger(LogsHandler(bot_logger))
