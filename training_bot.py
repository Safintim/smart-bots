import os
import json
from dialoflow_tools import list_intents, create_intent
from dotenv import load_dotenv


def read_training_file(training_file):
    with open(training_file) as json_file:
        training_phrases_parts = json.load(json_file)

    return training_phrases_parts


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
        if intent:
            print('Intent created: {}'.format(intent))
        else:
            print(intent, 'is exist')


if __name__ == '__main__':
    main()
