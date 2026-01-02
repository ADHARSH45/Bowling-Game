Bowling Game Score Calculator

Problem Statement

This project implements a Python module to calculate the total score of a single ten-pin bowling game based on standard bowling rules.

The input is a string that represents all rolls in a game, and the output is the final score after 10 frames.

Bowling Rules (Summary)

A game has 10 frames

Frames 1–9:

Up to 2 rolls per frame

Maximum 10 pins per frame

Frame 10:

Always at least 2 rolls

A strike or spare gives bonus roll(s)

Maximum 3 rolls in the 10th frame

Scoring

Open frame: sum of pins in the frame

Spare (/): 10 + pins from the next roll

Strike (X): 10 + pins from the next two rolls

Input Format

The game is provided as a single string using the following notation:

| Symbol | Meaning           |
| ------ | ----------------- |
| `0–9`  | Pins knocked down |
| `X`    | Strike            |
| `/`    | Spare             |
| `-`    | Miss (0 pins)     |

Example

9-9-9-9-9-9-9-9-9-9- → 90

XXXXXXXXXXXX → 300

5/5/5/5/5/5/5/5/5/5/5 → 150

Project Structure

bowling-game/
├── bowling.py
├── test_bowling.py
├── README.md
└── ERP_Presentation.pptx

How the Solution Works

The input string is converted into a list of rolls

Frames are scored sequentially

Strike and spare bonuses are calculated using look-ahead rolls

Scoring stops after 10 frames, even if bonus rolls exist

The implementation follows roll-based scoring, which simplifies strike and spare handling.

How to Run
python3 bowling.py


Or from Python:

from bowling import calculate_bowling_score
calculate_bowling_score("X7/9-X-88/-6XXX81")

Running Tests

Tests are written using pytest.

pytest -v


The test suite covers:

Open frames

Spares and strikes

Consecutive strikes

10th frame bonus rules

Mixed real-world scenarios

ERP Presentation

A short ERP presentation (less than 10 slides) is included as required.

Author

Adharsh M V