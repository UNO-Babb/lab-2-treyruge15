#FutureTime.py
#Name:
#Date:
#Assignment:

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now.hour - 5) % 24
  currentMinute = now.minute


  #TODO:
  #Ask user for hours
  #Ask user for minutes
  print("Future Time Calculator")
  moreMins = int(input("Enter how many minutes will elapse: "))
  moreHours = int(input("Enter how many hours will elapse: "))
  
  futureMins = (currentMinute + moreMins) % 60
  extraHour = (currentMinute + moreMins) // 60
  futureHour = (currentHour + moreHours + extraHour) % 24

  #Calculate the time after the user-supplied time has passed.
  futureTime = ("futureHour + futureMins")

  print("The time will be: ")
  print(f"{futureHour:02}:{futureMins:02}")

  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"


if __name__ == '__main__':
  main()
