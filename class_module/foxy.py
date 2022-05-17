import requests

class Foxy():
  def __init__(self):
    self.url= "https://randomfox.ca/floof/"
    self.get = requests.get(self.url)
    self.response = self.get.json()
  def get(self):
    self.get = requests.get(self.url)
    self.response = self.get.json()
    return self.response
  def __str__(self):
    return self.response["image"]
