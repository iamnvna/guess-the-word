import random

print("Welcome to the word guessing game!")
print("\nInstructions"
      "\n========================================="
      "\nYou have two options to guess a word out"
      "\nof ten word values. The words are Throw;"
      "\nPlay; Think; Santorini; Accra; Friday; "
      "\nMonday; Lagos; London; Sunday.")

weekdays = ['friday', 'monday', 'sunday']
verbs = ['throw', 'play', 'think']
city = ['santorini', 'accra', 'london', 'lagos']

words = ['friday', 'monday', 'sunday', 'throw', 'play',
         'think', 'santorini', 'accra', 'london', 'lagos']

random_word = random.choice(words)
count = 0

if random_word in weekdays:
    print("\nHint: It's a weekday.")
elif random_word in verbs:
    print("\nHint: It's a verb.")
else:
    print("\nHint: It's a city.")
    
def game_over():
    if count >= 2:
        print("\nYou've used all your guesses.")
        print("You lost.")
        quit()

while True:
    user_choice = input("Enter your guess: ").lower()
    if user_choice not in words:
        print("Entered an input from the words provided.")
        continue
    count += 1
    if user_choice == random_word:
        print(f"\nYou won on {count} attempt(s)!")
        quit()
    else:
        game_over()
        continue

# Commentary
'''
Line 1:
     Line 1 imports the random module that is used in the program.

Line 3-9:
      This block of code is a print statement that welcomes users to
      the game and outlines the instructions for the game.

Line 11-16:
      This block of code contains lists that are first grouped according
      to similarities, and later combined into a group. The first three
      lists allow us to give hints to the user whereas the full group
      allows the random.choice() method choose a word from the entire
      group of words available.

Line 18:
      This line of code assigns a random selected word from the words
      list to the random_word variable.

Line 19:
      This line of code assigns 0 to the count variable. This variable is
      used later in the code to tell how many guesses the user has made.

Line 21-26:
      The if/elif/else statement evaluates the random_word variable, and
      prints the line of code that evaluates True (i.e. the hint).

Line 28-32:
      This block of code is a function that evaluate the number of guesses
      the user has made and takes the necessary action.

Line 34-45:
      This block of code first collects the user guess and evaluates it
      against the word list to be sure it belongs in the options. If it
      doesn't, the user is prompted to enter a valid input. If the user
      guess is a valid input, it is evaluated against the random_word
      variable. If the evaluation is True, the program prints 'You won'
      else, it calls the game_over() function to evaluate if the user
      has made exactly two or more guesses. If so, the game quits or the
      user is given another attempt.
'''