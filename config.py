import os

class Config(object):
    CSRF_ENABLED = True
    SECRET_KEY = "about time"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_POSTS_PER_PAGE = 20

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True




config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig,
}