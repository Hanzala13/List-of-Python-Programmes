def find_uncommon_words(str1, str2):
    # Split strings into words
    words1 = str1.split()
    words2 = str2.split()
    
    # Use dictionaries to count word frequency
    word_count = {}
    
    for word in words1 + words2:
        word_count[word] = word_count.get(word, 0) + 1
    
    # Filter out common words (words appearing more than once)
    uncommon_words = [word for word, count in word_count.items() if count == 1]
    
    return uncommon_words

# Sample strings
string1 = "The sun rises in the east"
string2 = "The moon shines in the west"

# Output uncommon words
print("Uncommon words:", find_uncommon_words(string1, string2))
