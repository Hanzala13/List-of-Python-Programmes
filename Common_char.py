def common_unique_characters(strings):
    """
    Returns a set of unique characters that are common across all strings in the list.

    :param strings: List of strings
    :return: Set of characters common to all strings
    """
    if not strings:
        return set()

    # Start with characters from the first string
    common_chars = set(strings[0])

    # Intersect with sets from remaining strings
    for s in strings[1:]:
        common_chars &= set(s)

    return common_chars


# Example usage
if __name__ == "__main__":
    input_strings = ["hello", "world", "hold"]
    result = common_unique_characters(input_strings)
    print("Common unique characters in all strings:", result)
