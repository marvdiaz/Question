# Marvin Diaz
# programming assignment 5
# The user will think of an integer number at a specific range and the
# programming will guess the number using minimal guesses.

# Initial values for low and high will be asked, to know range
print()
print("Enter two numbers, low then high.")
low = int(input("low = ")) # Low number in the range
high = int(input("high = ")) # High number in the range
print()

# If low is greater than higher, it will ask the user to put inputs in order
while low>high:
   print("Please enter the smaller followed by the larger number.")
   low = int(input("low = ")) # Low number in the range
   high = int(input("high = ")) # High number in the range
   print()

# The range of the number will be listed out
print("Think of a number in the range of "+str(low)+" to "+str(high)+".\n")
guess = 0 # guess will be used to count the number of guesses
L = ['G','g','l','L','e','E'] # These are the acceptable inputs

# This will be the cycles used for the guesses that program makes
while low<=high:
   # The range will be split to guess the right number
   m = (low+high)//2

   # If the low and high are equal it will guess the right number in 0 guesses
   if low == high:
      print("Your number is "+str(m)+". I found it in "+str(guess)+" guesses.\n")
      break

   # It will initially ask the user for an input 
   print("Is your number Less than, Greater than, or Equal to "+str(m)+" ?")
   num = input("Type 'L', 'G' or 'E': ")
   print()

   # The program will ask the user for the correct input, which are any that
   # that are in the list L
   while num not in L:
      num = input("Please type 'L', 'G' or 'E': ")
      print()

   num = num.lower() # The input letter will be lower cased

   # If the number is equal
   if num == 'e':
      guess += 1
      if guess > 1:
         print("I found your number in "+str(guess)+" guesses.\n")
      else:
         print("I found your number in 1 guess.\n")
      break
   # If the number is lower
   elif num == 'l':
      high = m-1
      guess += 1
   # Else if the number is greater
   else:
      low = m+1
      guess += 1
# If the while loop ends and the number was not found, inputs were inconsistent
else:
   print("Your answers have not been consistent.")
