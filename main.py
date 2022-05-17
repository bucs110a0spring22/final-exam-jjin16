from class_module import doggo, duckky, foxy

def main():
  while True:
    """
    takes user input and depending on the input, shows a random picture of either fox, duck, or dog. Then asks user if they want to see another one of choosen animal. If not then ends the program.
    arg:none
    return:none
    """
    team=input("are u a team dog, team duck, or a team fox person?:")
    if team == "dog" or team=="Dog":
      print("here is a cute picture of a doggo!")
      dog=doggo.Doggo()
      print("click on the link:", dog)
      while True:
        one_more= input("would you like to see another doggo? y/n:")
        if one_more == "y" or one_more == "Y":
          dog=doggo.Doggo()
          print("click on the link:", dog)
        elif one_more == "n" or one_more == "N":
          print("okay, have a nice day!")
          quit()
          
        
    elif team == "duck" or team == "Duck":
      print("here is a cute picture of a duck!")
      duck=duckky.Duckky()
      print("click on the link:", duck)
      while True:
        one_more= input("would you like to see another ducky? y/n:")
        if one_more == "y" or one_more == "Y":
          duck=duckky.Duckky()
          print("click on the link:", duck)
        elif one_more == "n" or one_more == "N":
          print("okay, have a nice day!")
          quit()
    elif team == "fox" or team == "Fox":
      print("here is a cute fox picture!")
      fox= foxy.Foxy()
      print("Click on the link:", fox)
      while True:
        one_more= input("would you like to see another foxy? y/n:")
        if one_more == "y" or one_more == "Y":
          fox= foxy.Foxy()
          print("click on the link:", fox)
        elif one_more == "n" or one_more == "N":
          print("okay, have a nice day!")
          quit()
    else: 
      print("Please enter either 'dog', 'duck', or 'fox' Please!")
main()
