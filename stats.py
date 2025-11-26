def get_num_words(text):
    words = text.split()
    return len(words)


def get_char_counts(text):
    text = text.lower()
    counts = {}

    for char in text:
        if char not in counts:
            counts[char] = 0
        counts[char] += 1

    return counts


def sort_char_counts(char_counts):
    result = []

    for char, num in char_counts.items():
        if char.isalpha():  # only alphabetical characters
            result.append({"char": char, "num": num})

    # Sort from greatest to least
    result.sort(key=lambda d: d["num"], reverse=True)

    return result

