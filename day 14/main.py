from art import logo, vs
from game import data
import random
import os

# Format the account data into printable format: e.g. data is stored as a list: ['angelina_jolie', '10', 'M'] account_holder = " ".join(data) print(f"Compare A: {account_holder}")

def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

# Display art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

# Make the game repeatable.
while game_should_continue:
    # Generate a random account from the game data.
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_a = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # Ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if user is correct.
    # Get follower count of each account.
    account_a_follower_count = account_a["follower_count"]
    account_b_follower_count = account_b["follower_count"]
    is_correct = check_answer(
        guess, account_a_follower_count, account_b_follower_count)

    # Give user feedback on their guess.
    # Score keeping.
    os.system("cls")
    print(logo)
    
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")
