from bowling import calculate_bowling_score




def test_all_open_frames():
    # No strikes, no spares
    assert calculate_bowling_score("9-9-9-9-9-9-9-9-9-9-") == 90


def test_perfect_game():
    # 12 strikes = perfect game
    assert calculate_bowling_score("XXXXXXXXXXXX") == 300


def test_all_spares():
    # Every frame is a spare with first roll = 5
    assert calculate_bowling_score("5/5/5/5/5/5/5/5/5/5/5") == 150


def test_single_strike():
    # One strike followed by open frames
    assert calculate_bowling_score("X34XX---------------") == 54


def test_single_spare():
    # One spare followed by open frames
    assert calculate_bowling_score("7/34----------------") == 20


def test_strike_followed_by_spare():
    # Strike bonus should include both rolls of spare
    assert calculate_bowling_score("X5/----------------") == 30


def test_spare_followed_by_strike():
    # Spare bonus should include strike
    assert calculate_bowling_score("5/X----------------") == 30


def test_consecutive_strikes():
    # Multiple strikes in a row
    assert calculate_bowling_score("XXX----------------") == 60


def test_tenth_frame_spare():
    # Spare in the 10th frame with bonus roll
    assert calculate_bowling_score("9-9-9-9-9-9-9-9-9-5/7") == 98


def test_tenth_frame_strike():
    # Strike in the 10th frame with two bonus rolls
    assert calculate_bowling_score("9-9-9-9-9-9-9-9-9-X72") == 100


def test_mixed_real_game():
    # Classic real-world example used in bowling problems
    assert calculate_bowling_score("X7/9-X-88/-6XXX81") == 167
