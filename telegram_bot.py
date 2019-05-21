import os
from dotenv import load_dotenv
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters
from dialoflow_tools import get_response_from_dialogflow
from logger_bot import logger


class TelegramBot:
    def __init__(self, token, project_id):
        self.token = token
        self.project_id = project_id

    def start(self, bot, update):
        update.message.reply_text('Здравствуйте')

    def echo(self, bot, update):
        response = get_response_from_dialogflow(
            self.project_id,
            update.message.chat_id,
            update.message.text)
        update.message.reply_text(response.query_result.fulfillment_text)

    def error(bot, update, error):
        logger.exception(f'(smart-bots) Телеграм Бот упал\nUpdate {update} caused error')

    def start_bot(self):
        logger.info('(smart-bots) Телеграм Бот запущен')
        updater = Updater(self.token)
        dp = updater.dispatcher
        dp.add_handler(CommandHandler("start", self.start))
        dp.add_handler(MessageHandler(Filters.text, self.echo))
        dp.add_error_handler(self.error)

        updater.start_polling()


def main():
    load_dotenv()
    TelegramBot(os.getenv('TELEGRAM_BOT'), os.getenv('PROJECT_ID')).start_bot()


if __name__ == '__main__':
    main()
