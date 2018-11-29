import os


class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you_will_not_guess'
    DEBUG = True
