import requests
class Duckky:
  def __init__(self):
    """
    sets up instance variable for the duckky object
    arg:self
    return:none
    """
    self.url= "https://random-d.uk/api/random"
    self.get=requests.get(self.url)
    self.response= self.get.json()
  def get(self):
    """
    returns a dictionary containing link of a picture of duck
    arg:self
    return: dictionary containing link of a picture of duck
    """
    return self.response
  def __str__(self):
    """
    returns a string link of a picture of duck
    arg:self
    return: (str)link of a picture of duck
    """
    return self.response["url"]
    