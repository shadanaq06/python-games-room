
import random


def play_number_guess(num_guess):
    """
    Number Guess game:
    - Roll two dice and sum their values.
    - Compare player's guess to the sum.
    - Award points based on closeness of the guess.
    - Display game details and points earned.
    """
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    result = d1 + d2

    points = 0
    if num_guess == result:
        points = 10
    elif abs(num_guess - result) < 2:
        points = 5
    elif abs(num_guess - result) < 4:
        points = 1

    print(f"Game: Number Guess | Dice Sum: {result} | Your Guess: {num_guess} | Points Earned: {points}")
    return points


def play_mrpsls(player_move):
    """
    Modified Rock Paper Scissors Lizard Spock (MRPSLS):
    - Validate player's move.
    - Randomly select computer's move.
    - Determine winner based on rules.
    - Award points for win (10), tie (5), lose (0).
    - Display moves, outcome, and points.
    """

    moves = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
    player_move = player_move.capitalize()
    if player_move not in moves:
        print(f"Invalid move '{player_move}'. Choose from {moves}.")
        return 0

    computer_move = random.choice(moves)

    win_conditions = {
        'Rock': ['Scissors', 'Spock'],
        'Paper': ['Rock', 'Lizard'],
        'Scissors': ['Paper', 'Lizard'],
        'Lizard': ['Paper', 'Spock'],
        'Spock': ['Rock', 'Scissors']
    }

    if player_move == computer_move:
        points = 5
        outcome = "Tie"
    elif computer_move in win_conditions[player_move]:
        points = 10
        outcome = "Win"
    else:
        points = 0
        outcome = "Lose"

    print(
        f"Game: Modified RPSLS | Your Move: {player_move} | Computer's Move: {computer_move} | Outcome: {outcome} | Points Earned: {points}")
    return points


def play_coin():
    """
    Coin Flip game:
    - Flip a coin and observe first flip.
    - If tails, flip until heads then gain 2 points per heads.
    - If heads, flip until 3 heads appear; gain 1 point per tails.
    - Display each flip and final points.
    """
    flips = ['heads', 'tails']
    points = 0

    first_flip = random.choice(flips)
    print(f"Game: Coin Flip | First Flip: {first_flip}")

    if first_flip == 'tails':
        while True:
            flip = random.choice(flips)
            print(f"Flip: {flip}")
            if flip == 'heads':
                points += 2
            else:
                print("Game Over!")
                break
    else:
        head_count = 1
        while head_count < 3:
            flip = random.choice(flips)
            print(f"Flip: {flip}")
            if flip == 'tails':
                points += 1
            else:
                head_count += 1
        print("Game Over!")

    print(f"Points Earned: {points}")
    return points


def games_room(name):
    """
    Main game room loop:
    - Greet player.
    - Show current points.
    - Ask which game to play or exit.
    - Play selected game and update points.
    """

    total_points = 0
    print(f"Welcome to the Games Room, {name}!")

    while True:
        print(f"\nCurrent Points: {total_points}")
        print("Choose a game to play:")
        print("1: Number Guess")
        print("2: Modified RPSLS")
        print("3: Coin Flip")
        print("4: Exit")

        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            try:
                guess = int(input("Enter your guess (1-12): "))
                if guess < 1 or guess > 12:
                    print("Guess out of range. Please enter a number between 1 and 12.")
                    continue
            except ValueError:
                print("Invalid input. Please enter an integer.")
                continue
            points = play_number_guess(guess)
            total_points += points

        elif choice == 2:
            move = input("Enter your move (Rock, Paper, Scissors, Lizard, Spock): ")
            points = play_mrpsls(move)
            total_points += points

        elif choice == 3:
            points = play_coin()
            total_points += points

        elif choice == 4:
            print(f"Thanks for playing, {name}! Your total score is {total_points} points.")
            break

        else:
            points_lost = random.randint(1, 5)
            total_points -= points_lost
            print(f"Invalid choice. You lost {points_lost} points. Try again.")

    return total_points


def main():
    """
    Entry point:
    - Prompt for player name.
    - Start the games room.
    - Display final score.
    """
    player_name = input("Enter your name: ")
    final_score = games_room(player_name)
    print(f"Final Score: {final_score}")


if __name__ == "__main__":
    main()
