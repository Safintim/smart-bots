import os
from dotenv import load_dotenv
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters
from dialoflow_tools import get_response_from_dialogflow


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

    def start_bot(self):
        updater = Updater(self.token)
        dp = updater.dispatcher
        dp.add_handler(CommandHandler("start", self.start))
        dp.add_handler(MessageHandler(Filters.text, self.echo))

        updater.start_polling()


def main():
    load_dotenv()
    TelegramBot(os.getenv('TELEGRAM_BOT'), os.getenv('PROJECT_ID')).start_bot()


if __name__ == '__main__':
    main()
