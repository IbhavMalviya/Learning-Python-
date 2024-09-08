from random import choice, sample

# List of numbers to choose from
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# List of letters to choose from
letters = ['J', 'Q', 'K', 'A', 'M']

# Randomly select 4 numbers from the list
chosen_numbers = sample(numbers, 4)
# Randomly select one letter from the list
letter = choice(letters)
print(f"Your winning numbers are {chosen_numbers} and your winning letter is '{letter}'")

# Store the chosen numbers and letter in a ticket
my_ticket = [chosen_numbers, letter]

# Iterate over each element in the ticket
for my_ticket in my_ticket:
    # Randomly select another letter
    letter2 = choice(letters)
    # Randomly select another 4 numbers
    chosen_numbers2 = sample(numbers, 4)
    i = 0
    print("You win!")
    print(f"{my_ticket} and another ticket {my_ticket} matches")
    i = i + 1
    print(f"The loop ran {i} times")