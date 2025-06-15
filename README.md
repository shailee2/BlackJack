# Blackjack Game

Welcome to **Blackjack**, a Python-based console game where you can play against the house!

This project implements a simplified version of Blackjack, letting a player place bets, draw cards, and try to beat the house by getting as close as possible to 21 without busting.

---
## Project Structure
- `deck.py` Deck and Card classes
- `player.py` Player and House classes
- `game.py` Game logic (start_game function)
- `main.py` Entry point to run the game
- `README.md` Project description
  
---

## How to Run

1. **Clone the repository:**<br>
   ```
   bash
   git clone https://github.com/shailee2/BlackJack.git
   cd BlackJack
2. **Run the game:** <br>
`python main.py`<br>
You’ll need Python 3 installed.

## Game Features
- Shuffle and deal cards
- Place bets and track winnings
- Hit or stay decisions
- House (dealer) follows standard rules (hits until 17 or higher)
- Blackjack detection (automatic win)
- Handles Aces as 1 or 11 intelligently

## Files Explained
- `deck.py`	Defines the card deck and card value logic
- `player.py`	Defines player and house behavior and hand logic
- `game.py`	Runs a full game loop and manages the round flow
- `main.py`	Simple entry point to launch the game

## Future Improvements
- Add multiplayer support
- Add graphical interface (e.g., using Tkinter or Pygame)
- Add more betting options (split, double down)
- Save game history or stats

## Author
Shailee Patel <br>
Email: shaileepatel05@gmail.com <br>
LinkedIn: linkedin.com/in/shailee-patel-04481b285<br>
GitHub: github.com/shailee2
