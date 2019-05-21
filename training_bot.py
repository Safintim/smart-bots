import os
import json
from dialoflow_tools import list_intents, create_intent
from dotenv import load_dotenv


def is_intent(intent):
    return not isinstance(intent, str)


def read_training_file(training_file):
    with open(training_file) as json_file:
        return json.load(json_file)


def train_bot(training_phrases_parts, project_id):
    existing_intents = list_intents(project_id)
    for display_name, questions_and_answers in training_phrases_parts.items():
        if display_name not in existing_intents:
            training_phrases_parts = questions_and_answers['questions']
            message_texts = questions_and_answers['answer']
            yield create_intent(project_id, display_name, training_phrases_parts, message_texts)
        yield display_name


def main():
    load_dotenv()

    training_phrases_parts = read_training_file('questions.json')
    for intent in train_bot(training_phrases_parts, os.getenv('PROJECT_ID')):
        if is_intent(intent):
            print('Intent created: {}'.format(intent.display_name))
        else:
            print('{} is exist'.format(intent))


if __name__ == '__main__':
    main()


    # def form_intent(training_phrases_parts):
    #     return ((display_name, questions_and_answers['questions'], questions_and_answers['answer'])
    #             for display_name, questions_and_answers in training_phrases_parts.items())



    # project_id = os.getenv("PROJECT_ID")
    # training_phrases_parts = read_training_file('questions.json')
    # existing_intents = list_intents(project_id)
    # for display_name, questions, answer in form_intent(training_phrases_parts):
    #     if display_name in existing_intents:
    #         print(f'{display_name} is exist')
    #     else:
    #         response = create_intent(project_id, display_name, questions, answer)
    #         print(f'{"-" * 3} Intent created: {response.display_name}')
