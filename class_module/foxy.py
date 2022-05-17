import requests

class Foxy():
  def __init__(self):
    """
    sets up the instance variable for the foxy object
    arg:self
    return:none
    """
    self.url= "https://randomfox.ca/floof/"
    self.get = requests.get(self.url)
    self.response = self.get.json()
  def get(self):
    """
    returns the dictionary containing link to the picture of fox
    arg:self
    return: dictionary contianig link to the picture of fox
    """
    return self.response
  def __str__(self):
    """
    returns the string link to the picture of fox 
    arg:self
    return: (str) link to the picture of a fox
    """
    return self.response["image"]
