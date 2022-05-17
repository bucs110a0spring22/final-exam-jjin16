import requests

class Doggo():
  def __init__(self):
    """
    sets up the instance variable for the doggo object 
    arg:self
    return:none
    """
    self.api_url= "https://random.dog/woof.json"
    self.get = requests.get(self.api_url)
    self.response = self.get.json()
  def get(self):
    """
    returns a dictionary containing link of a picture of a dog
    arg:self
    return: dictonary containing a link of a picture of a dog
    """
    return self.response
  def __str__(self):
    """
    returns a string link of a picture of a dog
    arg:self
    return: (str)string representing the link of a picture of a dog
    """
    return self.response["url"]
