# smart-bot

## Описание
Два бота (один для группы вконтакте, другой для телеграмма) обученные с помощью
 [DialogFlow](https://dialogflow.com/).
 
Умеют отвечать на вопросы типа:
* Приветствия
* Устройство к нам работу - "Хочу работать у вас", "Как устроиться к вам?" и т.д.
* Забыл пароль - "Восстановить пароль", "Проблемы со входом" и т.д.
* Удаление аккаунта - "Хочу удалить аккаунт", "Как удалить данные обо мне" и т.д.
* Вопросы по банну - "Хочу купить разбан", "Меня забанили" и т.д.
* Вопросы от действующих партнёров - "Контракт уже в силе?", "Задерживаемся на совещание" и т.д.

## DialogFlow
DialogFlow - позволяет создавать разговорные интерфейсы поверх ваших продуктов и услуг,
 предоставляя мощный механизм обработки и понимания естественного языка.

## Пример ботов
вввв

## Требования

Для запуска скрипта требуется:

*Python 3.6*


## Как установить:

1. Установить Python3:

(Windows):[python.org/downloads](https://www.python.org/downloads/windows/)

(Debian):
```sh
sudo apt-get install python3
sudo apt-get install python3-pip
```
2. Установить зависимости и скачать сам проект:

```sh
https://github.com/Safintim/smart-bots.git
pip3 install -r requirements.txt
```
3. [Зарегистрироваться](https://dialogflow.com/docs/getting-started/create-account)
 и [создать проект на dialogflow](https://dialogflow.com/docs/getting-started/first-agent)
4. [Получить ключ-файл](https://dialogflow.com/docs/reference/v2-auth-setup)
5. Персональные настройки:

Скрипт берет настройки из .env файла, где указаны токен телеграм-бота, токен вк-бота, 
токен чат-логгер-бота, номер проекта на dialogflow, ключ dialogflow, номер чата. Создайте файл .env вида:
 
```sh
TELEGRAM_BOT=your_token
LOGGER_BOT=your_token
VK_BOT=your_token
GOOGLE_APPLICATION_CREDENTIALS=your_key_file
CHAT_ID=your_chat_id
PROJECT_ID=your_project_id
```
6. Для обучения бота нужно создать создать json файл с фразами вида:
```json
{
    "display_name1": {
        "questions": [
            "text_questions",
            "text_questions",
            "..."
        ],
        "answer": "answer"
    },
    "display_name2": {
        "questions2": [
            "text_questions",
            "text_questions",
            "..."
        ],
        "answer2": "answer"
    }
}
```

## Как использовать:

Запустить обучение бота:
```sh
python3 training_bot.py
```

Запустить телеграм бота:
```sh
python3 telegram_bot.py
```

Найти ботов в телеграме **_@smart_flow_bot_**, **_@devmanlogging_bot_**

Запустить вк бота:
```sh
python3 vk_bot.py
```

Найти группу [Умный бот](https://vk.com/club182299966) 



## Heroku:
* [Телеграм бот]()
* [Вконтакте бот]()


## Комментарии:
Есть возможность не использовать логгер-бота или использовать своего, для этого нужно написать свой обработчик логов.
И если понадобится написать своего бота.

Пример:
```python
class LogsHandler(logging.Handler):

    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    def emit(self, record):
        log_entry = self.format(record)
        self.bot.send_report(log_entry)
```

## Пример сообщения :
![Alt Text]()
![Alt Text]()