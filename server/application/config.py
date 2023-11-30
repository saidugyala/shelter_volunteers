"""
Configuration settings for the application are handled in this module
"""
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Base configuration"""


class ProductionConfig(Config):
    """Production configuration"""


class DevelopmentConfig(Config):
    """Development configuration"""
    #BYPASS_LOGIN = True
    DEV_USER = 'developer@slu.edu'
    DEV_TOKEN = '1234567890-developer-token'

class TestingConfig(Config):
    """Testing configuration"""

    TESTING = True
