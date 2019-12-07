import os


DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user='postgres', pw='postgres', url='localhost', db='users_info')


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = DB_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE = 3