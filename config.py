class BaseConfig(object):
	"""docstring for BaseConfig"""
	DEBUG = False
	SECRET_KEY = 'saviourgidi'
	SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/stms'
	SECURITY_REGISTERABLE = True
	#SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@192.168.1.6/stms'


class DevelopmentConfig(BaseConfig):
	DEBUG = True

class ProductionConfig(BaseConfig):
	DEBUG = True