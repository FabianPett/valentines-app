import turtle
import pygame
import time

import os
import pygame
import sys

# Determine the path to the music file (works both during development and from the .exe)
if getattr(sys, 'frozen', False):  # If running from the packaged executable
    music_path = os.path.join(sys._MEIPASS, 'love.mp3')
else:
    music_path = 'love.mp3'  # Normal path during development

# Initialize pygame mixer and play music
pygame.mixer.init()
pygame.mixer.music.load(music_path)
pygame.mixer.music.play(-1)

# --- Set up the screen ---
screen = turtle.Screen()
screen.bgcolor("lightpink")  # Soft pastel pink background

# Create a turtle for drawing the heart
heart_t = turtle.Turtle()
heart_t.speed(3)      # Moderate speed so you can see the drawing effect
heart_t.pensize(2)

# Create a separate turtle for writing text
text_t = turtle.Turtle()
text_t.hideturtle()
text_t.penup()

# List of colors to cycle through
colors = ["red", "pink", "purple", "blue", "white"]

def draw_heart(color):
    # Clear any previous heart drawing.
    heart_t.clear()
    heart_t.penup()
    # Position so that the heart is roughly centered.
    heart_t.goto(0, -100)
    heart_t.setheading(0)
    heart_t.left(140)           # Pre-turn for the classic heart shape
    heart_t.pendown()
    heart_t.color(color)
    heart_t.begin_fill()
    heart_t.forward(224)
    heart_t.circle(-112, 200)
    heart_t.left(120)
    heart_t.circle(-112, 200)
    heart_t.forward(224)
    heart_t.end_fill()

def write_text():
    # Clear any previous text.
    text_t.clear()
    # Write a border effect by writing in black (offset) then in white at the correct position.
    # Main message (moved higher to y=80)
    text_t.goto(2, 80)
    text_t.color("black")
    text_t.write("I love you, Molly", align="center", font=("Georgia", 28, "bold"))
    # Signature with a fancier font (Brush Script MT)
    text_t.goto(2, 10)
    text_t.color("black")
    text_t.write("- Fabian", align="center", font=("Brush Script MT", 28, "bold"))
    # Now write the main text in white.
    text_t.goto(0, 80)
    text_t.color("white")
    text_t.write("I love you, Molly", align="center", font=("Georgia", 28, "bold"))
    text_t.goto(0, 10)
    text_t.color("white")
    text_t.write("- Fabian", align="center", font=("Brush Script MT", 28, "bold"))

# Main loop: cycle through colors.
while True:
    for c in colors:
        draw_heart(c)
        # Heart is now fully drawn; then write the text.
        write_text()
        time.sleep(5)  # Keep the heart (and text) visible for 5 seconds.
        # Clear both the heart and text so they disappear before the next cycle.
        heart_t.clear()
        text_t.clear()
