# 📘 Sindh Districts Map Quiz – Python Turtle Game

An interactive and educational Python game that challenges players to identify and locate all districts of Sindh, Pakistan on a coordinate-based map. Built using Python Turtle Graphics, Pandas, and CSV data handling, this project visually labels districts on the map as users guess them.

## 🗺️ Overview

This game reads district names & coordinates from a CSV file and plots them on a Turtle Graphics map when the user guesses correctly. It includes score tracking, error handling, visual feedback, and an on-map reveal of missed districts.

## 🚀 Features
**🎮 Interactive Gameplay**

- Type district names to guess them.
- Correct answers appear at their exact map coordinates.
- Full map labeling system using Turtle.

**📊 Data-Driven Logic**

- Loads all district names from Districts.csv
- Uses coordinate data (x, y) for precise placement
- Automatically adjusts if CSV is updated

**🧠 Smart UI & Feedback**

- Scoreboard showing progress
- Instructions displayed on screen
- Messages for incorrect or repeated guesses
- “Show” command reveals all remaining districts
- “Exit” command ends game and marks missed ones in red

**🖼️ Map Integration**

- Uses Sindh_Districts.gif as a visual background
- Falls back to a placeholder if image is missing

## 📁 Project Structure
```bash
📦 Sindh Districts Quiz
├── SindhDistrictsGame.py        # Main game logic
├── Districts.csv                # District names & coordinates
├── Sindh_Districts.gif          # Map image (optional)
└── README.md                    # Project documentation
```

## 🛠️ Technologies Used

- Python
- Turtle Graphics
- Pandas
- CSV Data Processing

## ▶️ How to Run

1. Install dependencies:
```bash
pip install pandas
```
2. Run the game file:
```bash
python SindhDistrictsGame.py
```
3. Enjoy the quiz!

##🎯 Gameplay Instructions

- Type a district name (e.g., Sukkur, Hyderabad, Karachi East)
- Type Show → reveals all unguessed districts
- Type Exit → ends game & displays missed districts
- Correct guesses are labeled in dark blue
- Missed districts appear in red

## 🏆 Win Condition

You win the game when you correctly identify all districts of Sindh.
A celebratory message will be displayed on completion 🎉.
