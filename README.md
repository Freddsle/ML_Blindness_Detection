# ML_Blindness_Detection
ML project. Dataset - [APTOS 2019 Blindness Detection](https://www.kaggle.com/competitions/aptos2019-blindness-detection/data)


Model training code in `code` folder. Final model for TG bot in `data/model` folder.

For run training code in collab you have to add kaggle API (json file) to colaab folder.

TG bot in `tg_bot_model` model. TG bot contains:
- config with bot token
- file for model loading and prediction
- TG bot (run this file to run bot)


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
