# Input a sentence from the user
sentence = input("Enter a sentence: ").strip()

# Remove extra spaces (leading, trailing, and multiple spaces between words)
cleaned_sentence = " ".join(sentence.split())

# (a) Count the number of words in the cleaned sentence
word_count = len(cleaned_sentence.split())
print("Number of words in the sentence:", word_count)

# (b) Count the frequency of each character in the cleaned sentence
char_frequency = {}
for char in cleaned_sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
print("Character Frequency:", char_frequency)

# (c) Find the most frequent character(s)
max_frequency = max(char_frequency.values())
most_frequent_chars = [char for char, freq in char_frequency.items() if freq == max_frequency]

print("Most Frequent Character(s):", most_frequent_chars)
print("Frequency:", max_frequency)
