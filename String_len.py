def find_long_words(words, k):
    return [word for word in words if len(word) > k]

words = input("Enter words: ").split()
k = int(input("Enter K: "))
print("Words greater than length", k, ":", find_long_words(words, k))
