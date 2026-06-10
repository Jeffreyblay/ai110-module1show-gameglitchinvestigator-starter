def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    ranges = {
        "Easy": (1, 20),
        "Normal": (1, 100),
        "Hard": (1, 50),
    }
    return ranges.get(difficulty, (1, 100))


def parse_guess(raw: str, low: int | None = None, high: int | None = None):
    """
    Parse user input into an int guess.

    If low and high are provided, the guess must fall within that inclusive
    range; out-of-range numbers are rejected with a clear message.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    text = raw.strip()
    if text == "":
        return False, None, "Enter a guess."

    try:
        value = int(text)
    except ValueError:
        # Reject floats and non-numeric input with clear messages.
        try:
            float(text)
            return False, None, "Enter a whole number."
        except ValueError:
            return False, None, "That is not a number."

    # Reject guesses outside the allowed range for the difficulty.
    if low is not None and high is not None and not (low <= value <= high):
        return False, None, f"⛔ Out of range! Enter a number between {low} and {high}."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return the outcome string.

    Returns one of: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win"
    if guess > secret:
        return "Too High"
    return "Too Low"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        # Fewer attempts -> more points, with a floor of 10.
        points = max(10, 100 - 10 * (attempt_number - 1))
        return current_score + points

    if outcome in ("Too High", "Too Low"):
        return current_score - 5

    return current_score
