# TextBasedGame.py
# Author: Michael Henderson
# Game: Fragments of Humanity - A text-based adventure game

# Function to display the game instructions
def show_instructions():
    print("Fragments of Humanity - Text Adventure Game")
    print("Your goal: Collect all 6 Soul Fragments to restore humanity.")
    print("Avoid the Husk of Humanity until you're ready to fight.")
    print("Move commands: go South, go North, go East, go West")
    print("Add to Inventory: get 'item name'")
    print("-" * 50)

# Function to show the player's current status
def show_status(current_room, inventory, rooms):
    print(f"\nYou are in the {current_room}")
    print(f"Inventory: {inventory}")
    if "item" in rooms[current_room]:
        item = rooms[current_room]["item"]
        if item not in inventory and item != "Husk of Humanity":
            print(f"You see a {item}")
    print("-" * 50)

# Main function controlling the game loop
def main():
    # Dictionary of rooms with connections and items
    rooms = {
        "Dimensional Nexus": {
            "North": "Crumbling Library",
            "South": "Echoing Caverns",
            "East": "Abyssal Garden",
            "West": "Forgotten Stronghold"
        },
        "Crumbling Library": {
            "East": "Clockwork Wastes",
            "South": "Dimensional Nexus",
            "item": "Memory Fragment"
        },
        "Clockwork Wastes": {
            "West": "Crumbling Library",
            "item": "Creativity Fragment"
        },
        "Forgotten Stronghold": {
            "East": "Dimensional Nexus",
            "item": "Resilience Fragment"
        },
        "Echoing Caverns": {
            "North": "Dimensional Nexus",
            "East": "Mirror Sanctum",
            "item": "Compassion Fragment"
        },
        "Mirror Sanctum": {
            "West": "Echoing Caverns",
            "item": "Unity Fragment"
        },
        "Abyssal Garden": {
            "West": "Dimensional Nexus",
            "North": "Hollow Citadel",
            "item": "Hope Fragment"
        },
        "Hollow Citadel": {
            "South": "Abyssal Garden",
            "item": "Husk of Humanity"
        }
    }

    # Initialize game state
    current_room = "Dimensional Nexus"
    inventory = []
    soul_fragments = [
        "Memory Fragment", "Hope Fragment", "Compassion Fragment",
        "Creativity Fragment", "Unity Fragment", "Resilience Fragment"
    ]

    # Show the initial instructions
    show_instructions()

    # Start gameplay loop
    while True:
        show_status(current_room, inventory, rooms)

        # Get user input
        command = input("Enter your move: ").strip()

        # Validate basic command structure
        if len(command.split()) < 2:
            print("Invalid command format. Try again.")
            continue

        action, *details = command.split()
        action = action.lower()
        target = " ".join(details)

        # Handle movement commands
        if action == "go":
            direction = target.capitalize()
            if direction in rooms[current_room]:
                new_room = rooms[current_room][direction]
                if new_room == "Hollow Citadel":
                    if len(inventory) == 6:
                        print("\nYou enter the Hollow Citadel...")
                        print("The Soul Fragments pulse with light, weaving together in your hands.")
                        print("With a final surge of energy, you restore the essence of humanity.")
                        print(" Congratulations! You have defeated the Husk of Humanity. ")
                        print("Thanks for playing Fragments of Humanity. You brought back the light.")
                    else:
                        print("\nYou step into the Hollow Citadel...")
                        print("Without all the Soul Fragments, the darkness consumes you.")
                        print("The Husk of Humanity stares into your soul—and you vanish into oblivion.")
                        print("GAME OVER.")
                        print("Thanks for playing Fragments of Humanity. Try again to reclaim what was lost.")
                    break
                else:
                    current_room = new_room
            else:
                print("You can’t go that way!")

        # Handle item pickup
        elif action == "get":
            if "item" in rooms[current_room] and rooms[current_room]["item"] == target:
                if target not in inventory:
                    inventory.append(target)
                    print(f"{target} retrieved!")
                else:
                    print(f"You already have the {target}.")
            else:
                print(f"Can’t get {target}!")

        else:
            print("Invalid input! Try again using 'go' or 'get'.")

        # Optional encouragement if player has all items
        if len(inventory) == 6:
            print("\nYou feel a surge of power as all Soul Fragments come together...")
            print("You are now ready to face the Husk of Humanity in the Hollow Citadel.")

# Start the game
if __name__ == "__main__":
    main()