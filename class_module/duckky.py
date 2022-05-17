import requests
class Duckky:
  def __init__(self):
    self.url= "https://random-d.uk/api/random"
    self.get=requests.get(self.url)
    self.response= self.get.json()
  def get(self):
    return self.response
  def __str__(self):
    return self.response["url"]
    