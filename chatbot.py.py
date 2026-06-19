
def chatbot():
  print("chatbot: i am your chatbot")
  print("chatbot: enter 'Goodbye' to exit:\n")
  while True:
      User_input= input("User:  ")
      if User_input =="hello":
         print("chatbot:hi!")
      elif  User_input =="what is your name":
           print("chatbot: i am chatbot")
      elif  User_input =="how are you":
           print("chatbot: i am good! thanks for asking ")
      elif  User_input =="bye":
           print("chatbot: Goodbye! ")
           break
      else:
          print("chatbot: sorry! I didn't get your point.")
chatbot()