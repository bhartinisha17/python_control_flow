def print_greeting():
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")


def check_letter():
    letter = input("Enter a letter: ")

    if len(letter) == 1 and letter.isalpha():
        if letter.lower() in "aeiou":
            print(f"The letter {letter} is a vowel.")
        else:
            print(f"The letter {letter} is a consonant.")
    else:
        print("Invalid input. Please enter a single alphabet letter.")


def check_voting_eligibility():
    try:
        age = int(input("Please enter your age: "))
        if age < 0:
            print("Invalid age.")
            return

        if age >= 18:
            print("You are eligible to vote.")
        else:
            print("You are not eligible to vote yet.")
    except ValueError:
        print("Invalid input.")


def calculate_dog_years():
    try:
        age = int(input("Input a dog's age: "))
        if age < 0:
            print("Invalid age.")
            return

        if age <= 2:
            dog_years = age * 10
        else:
            dog_years = 20 + (age - 2) * 7

        print(f"The dog's age in dog years is {dog_years}.")
    except ValueError:
        print("Invalid input.")


def weather_advice():
    cold = input("Is it cold? (yes/no): ").lower()
    raining = input("Is it raining? (yes/no): ").lower()

    if cold not in ["yes", "no"] or raining not in ["yes", "no"]:
        print("Invalid input.")
        return

    if cold == "yes" and raining == "yes":
        print("Wear a waterproof coat.")
    elif cold == "yes" and raining == "no":
        print("Wear a warm coat.")
    elif cold == "no" and raining == "yes":
        print("Carry an umbrella.")
    else:
        print("Wear light clothing.")


def determine_season():
    month = input("Enter month (Jan-Dec): ").capitalize()

    try:
        day = int(input("Enter day: "))
    except ValueError:
        print("Invalid day.")
        return

    if (month == "Dec" and day >= 21) or (month in ["Jan", "Feb"]) or (month == "Mar" and day <= 19):
        season = "Winter"
    elif (month == "Mar" and day >= 20) or (month in ["Apr", "May"]) or (month == "Jun" and day <= 20):
        season = "Spring"
    elif (month == "Jun" and day >= 21) or (month in ["Jul", "Aug"]) or (month == "Sep" and day <= 21):
        season = "Summer"
    else:
        season = "Fall"

    print(f"{month} {day} is in {season}.")


def guess_number():
    target = 42

    for attempt in range(1, 6):
        try:
            guess = int(input("Guess number (1-100): "))
        except ValueError:
            print("Invalid input.")
            continue

        if guess < 1 or guess > 100:
            print("Out of range.")
            continue

        if guess == target:
            print("Congratulations, you guessed correctly!")
            return

        if attempt == 5:
            print("Last chance!")

        if guess < target:
            print("Too low.")
        else:
            print("Too high.")

    print("Sorry, you failed to guess the number.")


# -------- MENU --------
def main():
    while True:
        print("\n--- MENU ---")
        print("1. Greeting")
        print("2. Vowel or Consonant")
        print("3. Voting Eligibility")
        print("4. Dog Years")
        print("5. Weather Advice")
        print("6. Determine Season")
        print("7. Guess Number Game")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print_greeting()
        elif choice == "2":
            check_letter()
        elif choice == "3":
            check_voting_eligibility()
        elif choice == "4":
            calculate_dog_years()
        elif choice == "5":
            weather_advice()
        elif choice == "6":
            determine_season()
        elif choice == "7":
            guess_number()
        elif choice == "0":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")


# Run program
main()