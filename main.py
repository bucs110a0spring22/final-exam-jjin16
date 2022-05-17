from class_module import doggo, duckky, foxy

def main():
  while True:
    team=input("are u a team dog, team duck, or a team fox person?:")
    if team == "dog" or team=="Dog":
      print("here is a cute picture of a doggo!")
      dog=doggo.Doggo()
      print("click on the link:", dog)
      one_more= input("would you like to see another doggo? y/n:")
      if one_more == "y" or one_more == "Y":
        dog=doggo.Doggo()
        print("click on the link:", dog)
      elif one_more == "n" or one_more == "N":
        break
    elif team == "duck" or team == "Duck":
      print("here is a cute picture of a duck!")
      #cat_fact=catfacts.Catfacts()
      duck=duckky.Duckky()
      print("click on the link:", duck)
    elif team == "fox" or team == "Fox":
      print("here is a cute fox picture!")
      fox= foxy.Foxy()
      print("Click on the link:", fox)
    else: 
      print("Please enter either 'dog', 'duck', or 'fox' Please!")
main()
