import os
import json
from dialoflow_tools import list_intents, create_intent
from dotenv import load_dotenv


def training_bot(training_file, project_id):
    with open(training_file) as json_file:
        training_phrases_parts = json.load(json_file)

    existing_intents = list_intents(project_id)
    for display_name, questions_and_answers in training_phrases_parts.items():
        if display_name not in existing_intents:
            training_phrases_parts = questions_and_answers['questions']
            message_texts = questions_and_answers['answer']
            create_intent(project_id, display_name, training_phrases_parts, message_texts)
        else:
            print(display_name, 'is exist')


def main():
    load_dotenv()
    training_bot('questions.json', os.environ['PROJECT_ID'])


if __name__ == '__main__':
    main()
