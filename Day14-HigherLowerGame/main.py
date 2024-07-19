import random
import os
from game_data import data
from art import logo, vs

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_random_entry(exclude=None):
    """Select and return a random entry from the data, optionally excluding a specific entry."""
    available_entries = [entry for entry in data if entry != exclude]
    return random.choice(available_entries)

def play_game():
    count = 0
    current_entry = get_random_entry()  # Initialize the first entry

    while True:
        clear_screen()
        print(logo)
        
        # Get the new entry for comparison
        new_entry = get_random_entry(exclude=current_entry)
        
        name1, follower1, description1, country1 = (current_entry['name'], current_entry['follower_count'], current_entry['description'], current_entry['country'])
        name2, follower2, description2, country2 = (new_entry['name'], new_entry['follower_count'], new_entry['description'], new_entry['country'])
        
        print(f"Compare A: {name1}, a {description1}, from {country1}")
        print(vs)
        print(f"Against B: {name2}, a {description2}, from {country2}")
        
        x = input("Who has more followers? Type 'A' or 'B': ").strip().upper()
        
        if x == 'A' and follower1 > follower2:
            count += 1
            print(f"You're right! Current score: {count}")
        elif x == 'B' and follower2 > follower1:
            count += 1
            print(f"You're right! Current score: {count}")
            # Update current_entry to the new "A"
            current_entry = new_entry
        else:
            print(f"Sorry, that's wrong! Final score: {count}")
            break

if __name__ == "__main__":
    play_game()
