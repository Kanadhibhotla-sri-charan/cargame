user_input = ""
started = False

while True:
  user_input = input("Type your command: ").lower()
  if user_input == "start":
    if started:
     print("Car is already Started!!")
    else:
      started = True
      print("Car started..")
  elif user_input == "help":
    print("""
  start : To start the Car
  stop: To stop the Car
  exit: To quit the game
    """)
  elif user_input == "stop":
    if not started:
     print("car is already stopped.")
    else:
      started = False 
      print("Car stopped")
  elif user_input == "exit":
    print("Exitted from the game")
    break
  else:
    print("sorry!! I didn't understand that")






 







 
