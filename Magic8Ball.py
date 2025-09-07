#Magic8Ball.py
#Name:
#Date:
#Assignment:

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  #Prompt the user for their question.
Question = input("Enter a Yes or No question: ")

answers = ["No way Jose.", "Only time will tell.", "Without a doubt", "Yes", "Yes, 100% yes.", "It is destined to happen.",
           "That's a great question, :).", "Not a chance", "Try again", "It has been and always will be", "No", 
           "Never goning to happen", "God is still trying to figure that one out", "I would bet the house against it", 
           "My grandma has a better chance of walking right out of her grave", "I've seen the future and it's happen", 
           "60 percent of the time, it'll be 100 percent true", "I believe so", "I'd say so", "Certainly so, right?"]
  #Answer question randomly with one of the options from your earlier list.
length = len(answers)
r=random.random() * length
r=int(r)

response = answers[r]
print(response)

if __name__ == '__main__':
  main()
