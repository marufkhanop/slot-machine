import game

def test_win_line_1():
    # 1. Set starting balance
    game.BALANCE = 100 
    
    # 2. Run score function (betting $10 on line 1, and winning)
    game.score_logic(1, 10, True, False, False) 
    
    # 3. Check if the math is correct! (100 + 40 = 140)
    assert game.BALANCE == 140


def test_win_line_2():
    game.BALANCE = 100
    # Betting $10 on line 2, and winning on the second line
    game.score_logic(2, 10, False, True, False)
    
    assert game.BALANCE == 130


def test_losing_spin():
    game.BALANCE = 100
    # Getting no lines right (False, False, False)
    game.score_logic(3, 10, False, False, False)
    
    # Balance should not go up
    assert game.BALANCE == 100
