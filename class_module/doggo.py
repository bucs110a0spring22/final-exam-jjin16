import requests

class Doggo():
  def __init__(self):
    self.api_url= "https://random.dog/woof.json"
    self.get = requests.get(self.api_url)
    self.response = self.get.json()
  def get(self):
    self.get = requests.get(self.api_url)
    self.response = self.get.json()
    return self.response
  def __str__(self):
    return self.response["url"]
