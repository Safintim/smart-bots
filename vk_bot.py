import random
import os
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from dotenv import load_dotenv
from dialoflow_tools import get_response_from_dialogflow


class VkBot:
    def __init__(self, token, project_id):
        self.token = token
        self.project_id = project_id

    def echo(self, event, api):
        response = get_response_from_dialogflow(self.project_id, event.user_id, event.text)
        if response.query_result.intent.display_name != 'Default Fallback Intent':
            api.messages.send(
                user_id=event.user_id,
                message=response.query_result.fulfillment_text,
                random_id=random.randint(1, 1000)
            )

    def start_bot(self):
        vk_session = vk_api.VkApi(token=self.token)

        api = vk_session.get_api()

        longpoll = VkLongPoll(vk_session)
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                self.echo(event, api)


def main():
    load_dotenv()
    VkBot(os.getenv('VK_BOT'), os.getenv('PROJECT_ID')).start_bot()


if __name__ == '__main__':
    main()
