class Config:
  """
  General configuration parent class
  """
  MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'

class ProdConfig(Config):
  """
  production configuration child class

  Args:
    Config: The parent configuration with General configuration settings
  """
  pass

class DevConfig(Config):
  """
  Development configuration child clasS

  Args:
    Config:The parent configuration class with General configuration settings
  """

  DEBUG = True