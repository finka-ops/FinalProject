# Main game
import time
from Exam2PetClass import Penguin, Cat, Bat, Fox

#UI Functions

def show_welcome(max_turns):
    print("Welcome to Sysadmin Tamagotchi!")
    print("A tiny server pet has appeared on your terminal, and it’s your job to keep it alive.\n")

    print("Each turn you’ll see its stats:")
    print("- Health = how stable your server pet is")
    print("- Energy = how awake you are as the sysadmin")
    print("- Mood   = how happy the server pet feels\n")

    print("Choose one action per turn to take care of it.")
    print("Time passes every turn, so stats can drop if you ignore them.\n")

    print(f"Goal: keep your server pet running for {max_turns} turns!")
    print("If Health hits 0, your pet crashes and it’s game over!\n")


def get_menu_choice(prompt, options):
    """
    Generic numbered menu. Returns 0-based index.
    """
    while True:
        print(prompt)
        for i, opt in enumerate(options, start=1):
            print(f"{i}) {opt}")
        choice = input(f"Enter 1-{len(options)}: ").strip()
        if choice.isdigit():
            n = int(choice)
            if 1 <= n <= len(options):
                return n - 1
        print("Invalid input. Try again.\n")

def show_ending(pet, win):
    if win:
        print("\nYou kept your server pet alive through all turns! You win!\n")
        for frame in pet.win_art():
            print(frame)
            time.sleep(0.25)
    else:
        print("\nOh no! Your server pet crashed! Game over.\n")
        print(pet.lose_art())


def choose_pet():
    pet_types = [Penguin, Cat, Bat, Fox]
    names = [p.species_name for p in pet_types]
    choice = get_menu_choice("Pick a pet:", names)
    return pet_types[choice]()


def get_action(pet):
    options = ["Feed coffee", "Apply patches", "Restart service", "Ignore alerts"]
    choice = get_menu_choice("Choose an action:", options)

    if choice == 0:
        pet.feed_coffee()
    elif choice == 1:
        pet.apply_patches()
    elif choice == 2:
        pet.restart_service()
    else:
        pet.ignore_alerts()


def main():
    max_turns = 8
    show_welcome(max_turns)

    pet = choose_pet()
    print(f"\nYou chose: {pet.species_name} {pet.face}\n")

    turn = 1
    while turn <= max_turns and pet.health > 0:
        print(f"--- Turn {turn} of {max_turns} ---")

        pet.new_trait_each_turn()
        pet.show_stats()

        get_action(pet)

        pet.time_passes()
        pet.random_event()

        print()
        time.sleep(0.2)
        turn += 1

    won_game = (pet.health > 0) and (turn > max_turns)
    show_ending(pet, win=won_game)


if __name__ == "__main__":
    main()
#show_ending(pet, win=(pet.health > 0))