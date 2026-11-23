"""Numbers.py - simple statistics functions for a list of numbers."""


def sum_numbers(numbers):
    """Return the sum of all the numbers in the list."""
    total = 0
    for n in numbers:
        total += n
    return total


def mean(numbers):
    """Return the average (mean) of the values in the list."""
    if len(numbers) == 0:
        raise ValueError("Cannot find the mean of an empty list.")
    return sum_numbers(numbers) / len(numbers)


def median_and_mode(numbers):
    """Return a tuple: (median, mode).

    - median: the middle value of the sorted list
              (average of the two middle values if the length is even).
    - mode: the most frequent value. If several values tie,
            a list of all of them is returned.
    """
    if len(numbers) == 0:
        raise ValueError("Cannot find the median or mode of an empty list.")

    # --- Median ---
    ordered = sorted(numbers)
    size = len(ordered)
    middle = size // 2
    if size % 2 == 1:
        median = ordered[middle]
    else:
        median = (ordered[middle - 1] + ordered[middle]) / 2

    # --- Mode ---
    counts = {}
    for n in ordered:
        counts[n] = counts.get(n, 0) + 1
    highest = max(counts.values())
    modes = [value for value, count in counts.items() if count == highest]
    mode = modes[0] if len(modes) == 1 else modes

    return median, mode


if __name__ == "__main__":
    data = [4, 1, 2, 2, 3, 5, 2, 4]
    print("Numbers:", data)
    print("Sum:", sum_numbers(data))
    print("Mean:", mean(data))
    median_value, mode_value = median_and_mode(data)
    print("Median:", median_value)
    print("Mode:", mode_value)