# 🇮🇳 India Map Quiz Game

A fun and educational Python project using Turtle graphics to guess Indian states on a blank map!

## 🧠 About the Project

The **India Map Quiz** is a Python-based interactive game where users try to guess all 28 Indian states by name. When a correct guess is entered, the name of the state appears at its correct location on a blank map of India.

It’s a great way to test and improve your geographical knowledge of India in an engaging, visual way.

## 🎮 How to Play

- Run the script.
- A blank map of India will appear.
- A prompt will ask you to guess a state name.
- If correct, the name appears on the map.
- If incorrect, you can try again.
- Type `Exit` anytime to quit the game.
- Upon exiting, a `Missed_states.csv` file is generated containing all the states you didn’t guess.


## 🖼️ Screenshot

![Screenshot 2025-05-03 005625](https://github.com/user-attachments/assets/6df59fb1-5dfd-4419-bb42-4dd9a9cb54e9)


## 📁 Files Included

- `main.py` – Main game logic
- `India_Map.gif` – Blank map of India used as background
- `states.csv` – Data file containing state names and their x, y coordinates
- `Missed_states.csv` – (Auto-generated) List of states you missed during gameplay


## 🖼️ Customization Tip

At the end of the script, there's a commented helper function that you can use to get coordinates of mouse clicks on the map. This allows you to easily adapt the game for other countries, world maps, or regional maps.

## 📦 Requirements

- Python 3.x
- `pandas` module

Install pandas using:

```bash
pip install pandas
