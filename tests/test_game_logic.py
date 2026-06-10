import pytest

from logic_utils import (
    check_guess,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)


# --- check_guess -----------------------------------------------------------

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


# --- get_range_for_difficulty ----------------------------------------------

@pytest.mark.parametrize("difficulty, expected", [
    ("Easy", (1, 20)),
    ("Normal", (1, 100)),
    ("Hard", (1, 50)),
])
def test_range_for_known_difficulty(difficulty, expected):
    assert get_range_for_difficulty(difficulty) == expected

def test_range_for_unknown_difficulty_defaults_to_normal():
    assert get_range_for_difficulty("Whatever") == (1, 100)


# --- parse_guess: valid input ----------------------------------------------

def test_parse_valid_number():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None

def test_parse_strips_whitespace():
    ok, value, err = parse_guess("  7  ")
    assert ok is True
    assert value == 7


# --- parse_guess: invalid input --------------------------------------------

def test_parse_empty_string():
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None
    assert err == "Enter a guess."

def test_parse_none():
    ok, value, err = parse_guess(None)
    assert ok is False
    assert err == "Enter a guess."

def test_parse_float_rejected():
    ok, value, err = parse_guess("3.5")
    assert ok is False
    assert err == "Enter a whole number."

def test_parse_non_number_rejected():
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert err == "That is not a number."


# --- parse_guess: range validation -----------------------------------------

def test_parse_in_range_accepted():
    ok, value, err = parse_guess("100", low=1, high=100)
    assert ok is True
    assert value == 100

def test_parse_above_range_rejected():
    ok, value, err = parse_guess("101", low=1, high=100)
    assert ok is False
    assert value is None
    assert "Out of range" in err

def test_parse_below_range_rejected():
    ok, value, err = parse_guess("0", low=1, high=100)
    assert ok is False
    assert "Out of range" in err

def test_parse_range_boundaries_inclusive():
    assert parse_guess("1", low=1, high=20)[0] is True
    assert parse_guess("20", low=1, high=20)[0] is True


# --- update_score ----------------------------------------------------------

def test_score_win_first_attempt():
    # First-attempt win earns the full 100 points.
    assert update_score(0, "Win", attempt_number=1) == 100

def test_score_win_has_floor_of_10():
    # Even a late win never earns less than 10 points.
    assert update_score(0, "Win", attempt_number=20) == 10

def test_score_wrong_guess_deducts_5():
    assert update_score(50, "Too High", attempt_number=2) == 45
    assert update_score(50, "Too Low", attempt_number=2) == 45
