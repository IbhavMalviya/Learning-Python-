from random import choice, sample

# Define the numbers and letters
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
letters = ['J', 'Q', 'K', 'A', 'M']

# Generate the initial winning ticket
winning_numbers = sample(numbers, 4)
winning_letter = choice(letters)
winning_ticket = [winning_numbers, winning_letter]

# Print the winning ticket
print(f"Your winning numbers are {winning_numbers} and your winning letter is '{winning_letter}'")

# Initialize the iteration counter
i = 0

# Loop until we find a matching ticket
while True:
    # Generate a new random ticket
    new_numbers = sample(numbers, 4)
    new_letter = choice(letters)
    new_ticket = [new_numbers, new_letter]
    
    # Increment the iteration counter
    i += 1
    
    # Check if the new ticket matches the winning ticket
    if new_ticket == winning_ticket:
        print("You win!")
        print(f"The matching ticket is {new_ticket}")
        break

# Print the number of iterations it took to find a match
print(f"The loop ran {i} times to find a matching ticket")
