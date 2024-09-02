# Tic-Tac-Toe Game with AI (Minimax Algorithm)

## Overview

This project is a Tic-Tac-Toe game where a single player competes against an AI opponent. The AI uses the Minimax algorithm to play optimally, ensuring a challenging game.

## How to Play

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/shivaMoulodi/tic-tac-toe.git
   ```
   
2. **Navigate to the Project Directory**:
   ```bash
   cd code.py
   ```
   
3. **Run the Game**:
   ```bash
   python tic_tac_toe.py
   ```

4. **Gameplay**:
   - The game starts with the AI making its move.
   - Enter a position (1-9) to place your mark ('o') when prompted.
   - The board positions are numbered as follows:
     ```
     1 | 2 | 3
     4 | 5 | 6
     7 | 8 | 9
     ```
   - Continue playing until there's a win or a draw.

## Game Logic

- The game board is represented as a dictionary.
- The Minimax algorithm allows the AI to make the best possible move each turn, aiming to win or force a draw.
