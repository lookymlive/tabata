# Importing the libraries
import tkinter as tk
import pygame

# Initialize pygame and load the sounds
pygame.init()
pygame.mixer.init()
start_sound = pygame.mixer.Sound("start.wav")
end_sound = pygame.mixer.Sound("end.wav")

# Create a list of pilates exercises
exercises = ["Hundred", "Roll up", "One leg circle", "Rolling like a ball", "Single leg stretch", "Double leg stretch", "Criss cross", "Spine stretch forward", "Open leg rocker", "Corkscrew"]

# Define global variables
work_time = 20 # Work time in seconds
rest_time = 10 # Rest time in seconds
rounds = 8 # Number of rounds
state = "Work" # Current state (Work or Rest)
counter = work_time # Time counter
index = 0 # Index of the current exercise

# Create the main window
window = tk.Tk()
window.title("Tabata App for Pilates Training")
window.geometry("400x300")

# Create the widgets
time_label = tk.Label(window, text=str(counter), font=("Arial", 50))
rounds_label = tk.Label(window, text="Round " + str(index + 1) + " of " + str(rounds), font=("Arial", 20))
label_exercise = tk.Label(window, text=exercises[index], font=("Arial", 20))

# Place the widgets in the window
time_label.pack(pady=20)
rounds_label.pack()
label_exercise.pack(pady=20)

# Define the function that updates the timer
def update():
    global state, counter, index

    # If counter reaches zero
    if counter == 0:
        # Change the state
        if state == "Work":
            state = "Rest"
            counter = rest_time
            end_sound.play()
        else:
            state = "Work"
            counter = work_time
            index += 1
            start_sound.play()

        # Update the labels
        time_label.config(text=str(counter))
        rounds_label.config(text="Round " + str(index + 1) + " of " + str(rounds))
        label_exercise.config(text=exercises[index % len(exercises)])

        # Check if the user has completed all rounds
        if index == rounds:
            # Play a sound to indicate the end of the workout
            pygame.mixer.Sound("finish.wav").play()
            # Exit the program
            window.quit()

    # If the counter does not reach zero
    else:
        # Decrease the counter by one
        counter -= 1

        # Update the time label
        time_label.config(text=str(counter))

    # Call the update function again after one second
    window.after(1000, update)

# Call the update function for the first time
update()

# Start window's main loop
window.mainloop()
