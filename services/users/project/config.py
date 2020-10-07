class BaseConfig:
   """ Base Configuration """
   TESTING=False
   SQLALCHEMY_TRACK_MODIFICATIONS = False
   
class DevelopmentConfig(BaseConfig):
    """ Development Configuration"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

class TestingConfig(BaseConfig):
    """  Testing configuration"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL')

class ProductionConfiguration(BaseConfig):
    """ Production Configuration""" 
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    
    
    