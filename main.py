import random


# Available choices
CHOICES = ["snake", "water", "gun"]


def get_computer_choice():
    """Generate a random choice for the computer."""
    return random.choice(CHOICES)


def get_user_choice():
    """Get and validate the user's choice."""

    while True:
        user_choice = input(
            "\nEnter your choice (snake/water/gun): "
        ).lower().strip()

        if user_choice in CHOICES:
            return user_choice

        print("❌ Invalid choice! Please choose snake, water, or gun.")


def determine_winner(user, computer):
    """Determine the winner of a round."""

    if user == computer:
        return "draw"

    if (
        (user == "snake" and computer == "water")
        or
        (user == "water" and computer == "gun")
        or
        (user == "gun" and computer == "snake")
    ):
        return "user"

    return "computer"


def display_choice(choice):
    """Return an emoji for each choice."""

    emojis = {
        "snake": "🐍",
        "water": "💧",
        "gun": "🔫"
    }

    return emojis[choice]


def play_game():
    """Run the Snake Water Gun game."""

    user_score = 0
    computer_score = 0
    draws = 0

    print("\n" + "=" * 40)
    print("       🐍 SNAKE WATER GUN GAME")
    print("=" * 40)

    print("\nGame Rules:")
    print("🐍 Snake beats 💧 Water")
    print("💧 Water beats 🔫 Gun")
    print("🔫 Gun beats 🐍 Snake")

    while True:

        # Get choices
        user = get_user_choice()
        computer = get_computer_choice()

        # Display choices
        print("\n" + "-" * 40)
        print(
            f"You chose:      {display_choice(user)} {user.title()}"
        )
        print(
            f"Computer chose: {display_choice(computer)} {computer.title()}"
        )
        print("-" * 40)

        # Determine winner
        result = determine_winner(user, computer)

        if result == "draw":
            draws += 1
            print("🤝 It's a Draw!")

        elif result == "user":
            user_score += 1
            print("🎉 You Win!")

        else:
            computer_score += 1
            print("💻 Computer Wins!")

        # Display score
        print("\n📊 SCORE")
        print(f"You:      {user_score}")
        print(f"Computer: {computer_score}")
        print(f"Draws:    {draws}")

        # Play again
        play_again = input(
            "\nDo you want to play again? (yes/no): "
        ).lower().strip()

        if play_again not in ["yes", "y"]:
            break

    # Final result
    print("\n" + "=" * 40)
    print("             FINAL RESULT")
    print("=" * 40)

    print(f"You:      {user_score}")
    print(f"Computer: {computer_score}")
    print(f"Draws:    {draws}")

    if user_score > computer_score:
        print("\n🏆 Congratulations! You are the winner!")

    elif computer_score > user_score:
        print("\n💻 Computer wins this game!")

    else:
        print("\n🤝 The game ended in a draw!")

    print("\nThanks for playing! 👋")


# Start the game
if __name__ == "__main__":
    play_game()