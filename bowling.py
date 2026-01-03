from typing import Optional

def calculate_bowling_score(game : str)->int:
    """
    function for calculating the score of  ten-pin bowling game
    
    :param game: A string representing bowling rolls.
    :return: Total score as an Integer
    """

    rolls = [] 
    prev = 0
    # convert input string to rollvalues
    for ch in game:
        if ch == 'X':       #Strike
            rolls.append(10)
            prev = 0
        elif ch == '-':     #Spare
            rolls.append(0)
            prev = 0
        elif ch == '/':     #Open
            rolls.append(10 - prev)
        else:               #digit
            val = int(ch)
            rolls.append(val)
            prev = val

    roll_idx = 0
    total_score = 0
    # calculate score for 10 frames
    for frame in range(10):
        # Strike
        if rolls[roll_idx] == 10:
            total_score += 10 + rolls[roll_idx + 1] + rolls[roll_idx + 2]
            roll_idx += 1

        #Spare
        elif rolls[roll_idx] + rolls[roll_idx + 1] == 10:
            total_score += 10 + rolls[roll_idx + 2]
            roll_idx += 2
        
        #Open
        else:
            total_score += rolls[roll_idx] + rolls[roll_idx + 1]
            roll_idx += 2

    return total_score






print(calculate_bowling_score("9-9-9-9-9-9-9-9-9-9-"))     # 90
print(calculate_bowling_score("XXXXXXXXXXXX"))           # 300
print(calculate_bowling_score("5/5/5/5/5/5/5/5/5/5/5"))   # 150
