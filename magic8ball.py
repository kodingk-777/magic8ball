
import random

# Ask the user for a question
question = input("Ask the Magic 8-Ball a yes-or-no question: ")
name = input("What is your name, please? ")

random_number = random.randint(1, 10)
#print(random_number)
if random_number == 1:
    answer = 'Yes - definitely!'
elif random_number == 2:
    answer = 'It is decidedly so.'
elif random_number == 3:
    answer = 'Without a doubt.'
elif random_number == 4:
    answer = 'Reply hazy, try again.'
elif random_number == 5:
    answer = 'Ask again later.'
elif random_number == 6:
    answer = 'Better not tell you now.'
elif random_number == 7:
    answer = 'My sources say no.'
elif random_number == 8:
    answer = 'Outlook not so good.'
elif random_number == 9:
    answer = 'Very doubtful.'
elif random_number == 10:
    answer = f"\nIt remains to be seen if the answer is yes or no to: {question}"
else: 
  answer = 'Error'

# Print the original question and the Magic 8-Ball's response
print(f"\nYou asked: {question}")
print(f"Magic 8-Ball says: {answer}")

question_2 = input(f"Don't you wonder how I know that {name}? ")

# Generate a new random number for the second question
random_number_2 = random.randint(1, 9)

if random_number_2 == 1:
    answer_2 = "I just know things."
elif random_number_2 == 2:
    answer_2 = "The universe whispers it."
elif random_number_2 == 3:
    answer_2 = "Logic and reason guide me."
elif random_number_2 == 4:
    answer_2 = "It is a mystery even to me."
elif random_number_2 == 5:
    answer_2 = "Because I can see the bigger picture."
elif random_number_2 == 6:
    answer_2 = "Experience tells me so."
elif random_number_2 == 7:
    answer_2 = "Some things cannot be explained."
elif random_number_2 == 8:
    answer_2 = "I read between the lines."
elif random_number_2 == 9:
    answer_2 = "Because patterns repeat themselves."
else:
    answer_2 = "Error"

# Print the second question and response
print(f"\nYou asked: {question_2}")
print(f"Magic 8-Ball says: {answer_2}")