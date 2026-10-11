# Name: Diesta, Macy T.
# Date: October 11, 2026
# Course: PROGCON IT261
# File: wk09d02ex03_guess_colors.py
# Description: Guess the colors of the rainbow. The user enters 7 guesses,
#              and the program counts the correct answers and gives a grade.
#              Converted from my Flowgorithm file wk09d02ex03_guess_colors.fprg.


# Flowgorithm: Main
def main():
    # Flowgorithm: String Array rainbowColor[7] and the 7 assignments
    rainbow_color = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    user_guesses = [""] * 7     # Flowgorithm: String Array userGuesses[7]
    correct_count = 0           # Flowgorithm: correctCount = 0

    # Flowgorithm: First loop, i = 0 to 6: ask for each guess
    for i in range(7):
        user_guesses[i] = input("Enter the colors of the rainbow " + str(i + 1) + ": ")

    # Flowgorithm: Second loop, i = 0 to 6: compare each guess with the color
    for i in range(7):
        if user_guesses[i] == rainbow_color[i]:
            correct_count = correct_count + 1

    # Flowgorithm: Show the number of correct answers
    print("You got " + str(correct_count) + " correct answers.")

    # Flowgorithm: Grade decisions
    if correct_count >= 6:
        print("Grade: excellent")
    elif correct_count >= 3:
        print("Grade: average")
    else:
        print("Grade: poor")


if __name__ == "__main__":
    main()
