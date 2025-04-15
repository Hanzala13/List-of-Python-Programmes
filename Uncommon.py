def find_uncommon_words(str1, str2):
    # Split both strings into words
    words1 = str1.split()
    words2 = str2.split()

    # Create frequency dictionaries
    freq = {}

    for word in words1 + words2:
        freq[word] = freq.get(word, 0) + 1

    # Collect words that appear only once
    uncommon = [word for word in freq if freq[word] == 1]

    return uncommon

# Example usage
string1 = "apple banana mango"
string2 = "banana orange apple"

result = find_uncommon_words(string1, string2)
print("Uncommon words:", result)
