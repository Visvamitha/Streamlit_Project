import streamlit as st
import random

def user_guessing_game():
    st.title("User Guessing Game")

    # Set the range
    min_value = st.number_input("Enter the minimum value:", min_value=1, value=1)
    max_value = st.number_input("Enter the maximum value:", min_value=min_value + 1, value=100)

    # Generate a random number
    random_number = random.randint(min_value, max_value)

    st.write("Guess a number between", min_value, "and", max_value)

    attempts = 0
    while True:
        guess = st.number_input("Enter your guess:")
        attempts += 1

        if guess == random_number:
            st.write("Congratulations! You guessed the number in", attempts, "attempts.")
            break
        elif guess < random_number:
            st.write("Too low. Try again.")
        else:
            st.write("Too high. Try again.")

def machine_guessing_game():
    st.title("Machine Guessing Game")

    min_value = st.number_input("Enter the minimum value:", min_value=1, value=1)
    max_value = st.number_input("Enter the maximum value:", min_value=min_value + 1, value=100)

    st.write("Think of a number between", min_value, "and", max_value)

    attempts = 0
    while True:
        guess = (min_value + max_value) // 2
        st.write("Is your number", guess, "?")

        answer = st.text_input("Enter 'higher', 'lower', or 'correct':")

        attempts += 5

        if answer.lower() == "higher":
            min_value = guess + 1
        elif answer.lower() == "lower":
            max_value = guess - 1
        else:
            st.write("The machine guessed the number in", attempts, "attempts.")
            break

# Main application
st.title("Guessing Game & Portfolio")

# Add your portfolio content here
st.write("This is my portfolio page. Feel free to add your own content.")

# Select the game mode
game_mode = st.selectbox("Select game mode", ["User Guessing", "Machine Guessing"])

if game_mode == "User Guessing":
    user_guessing_game()
else:
    machine_guessing_game()
