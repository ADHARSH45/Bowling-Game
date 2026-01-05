# Bowling Game Score Calculator

## Problem Statement
This project implements a Python module to calculate the total score of a single ten-pin bowling game based on standard bowling rules.

The input is a string representing all rolls in a game, and the output is the final score after 10 frames.

---

## Bowling Rules (Summary)

- A game consists of 10 frames

### Frames 1–9
- Up to 2 rolls per frame
- Maximum 10 pins per frame

### Frame 10
- Always at least 2 rolls
- A strike or spare grants bonus roll(s)
- Maximum 3 rolls in the 10th frame

---

## Scoring Rules

- **Open frame**: sum of pins in the frame  
- **Spare (`/`)**: 10 + pins from the next roll  
- **Strike (`X`)**: 10 + pins from the next two rolls  

---

## Input Format

The game is provided as a single string using the following notation:

| Symbol | Meaning |
|------|--------|
| `0–9` | Pins knocked down |
| `X` | Strike |
| `/` | Spare |
| `-` | Miss (0 pins) |

### Examples

9-9-9-9-9-9-9-9-9-9- → 90

XXXXXXXXXXXX → 300

5/5/5/5/5/5/5/5/5/5/5 → 150

Project Structure
```basb
bowling-game/
├── bowling.py
├── test_bowling.py
├── README.md
└── ERP_Presentation.pptx
```


---

## How the Solution Works

- The input string is converted into a list of rolls
- Frames are evaluated sequentially
- Strike and spare bonuses are computed using look-ahead rolls
- Scoring stops after 10 frames, even if bonus rolls exist

The solution uses a roll-based approach, which simplifies strike and spare handling.

---

## How to Run

From the project root directory, run:

```bash
python3 bowling.py
Or 
```
```bash
from bowling import calculate_bowling_score
calculate_bowling_score("X7/9-X-88/-6XXX81")
```
### How to Test
Run the test suite using pytest:
```basb
pytest -v
```


