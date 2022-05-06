# ML_Blindness_Detection
ML project. Dataset - [APTOS 2019 Blindness Detection](https://www.kaggle.com/competitions/aptos2019-blindness-detection/data)


##### Что в папке с тг ботом:
###### 1. конфиг с токеном тг бота
###### 2. демо ноутбук, там только функция которая через 5 сек рандомно кидает числа 0 1 2
###### 3. модел_НОВЫЙ, это весь код с папки code обернутый в одну функцию, которая принимает фото глазного дна (тут надо уточнить: я пытался заранить его, но есть ошибка с json форматированием для строк содержащих линуксовые команды типа "! cat file.txt", кажется он их не любит. Поэтому нз как быть.)
###### 4. ТГ БОТ. я там понатыкал комментов, но основной связан с переменной answer которая запускает код с ноутбука и отправляет ему фото ДЗН. просто надо будет там название поменять и в импорте тоже. Пока что он работает только с демо ноутбуком. + он еще делает логирование)





# Install and run with pip
## Installation

```console
git clone https://github.com/Freddsle/ML_Blindness_Detection
cd ./ML_Blindness_Detection/

# Create and activate your virtual environment

# create virtual environment
python3.9 -m venv ./venv

# activate virtual environment
source ./venv/bin/activate

# required by pip to build wheels
pip install wheel==0.37.0 

# Install requirements
pip install -r ./requirements.txt
```

## Run TG bot
```console
python3.9 tg_bot_model/TG_BOT_EYECARE.py 
```

# Install and run with poetry
```console
# install poetry
# for details look for https://python-poetry.org/docs/
sudo apt-get install curl
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3.9 -

# poetry will be accessible in current session
source $HOME/.poetry/env

# prepare project
git clone https://github.com/Freddsle/ML_Blindness_Detection
cd ./ML_Blindness_Detection

poetry env use python3.9
poetry install

# Run
poetry run python tg_bot_model/TG_BOT_EYECARE.py 

```