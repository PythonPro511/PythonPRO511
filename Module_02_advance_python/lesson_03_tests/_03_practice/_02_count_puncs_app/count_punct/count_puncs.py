def count_punct_marks(string: str) -> int:
    total_count = 0
    for sym in ",.::'!?":
        total_count += string.count(sym)
    return total_count
