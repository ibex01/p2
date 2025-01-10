# Reverse a sentence
def reverse_sentence(sentence):
    return ' '.join(sentence.split()[::-1])

# Count word occurrences in a paragraph
def count_word_occurrences(paragraph):
    word_count = {}
    for word in paragraph.split():
        word = word.strip().lower()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

# Find and replace words in a paragraph
def find_and_replace(paragraph, target, replacement):
    return paragraph.replace(target, replacement)

# Menu-driven functionality
def menu():
    while True:
        print("\nMenu:")
        print("1. Reverse words in a sentence")
        print("2. Count occurrences of each word in a paragraph")
        print("3. Find and replace a word in a paragraph")
        print("4. Exit")
        
        try:
            choice = int(input("Enter your choice (1-4): "))
            if choice == 1:
                sentence = input("Enter a sentence: ")
                print("Reversed Sentence:", reverse_sentence(sentence))
            elif choice == 2:
                paragraph = input("Enter a paragraph: ")
                print("Word Count:", count_word_occurrences(paragraph))
            elif choice == 3:
                paragraph = input("Enter a paragraph: ")
                target = input("Enter the word to replace: ")
                replacement = input("Enter the replacement word: ")
                print("Updated Paragraph:", find_and_replace(paragraph, target, replacement))
            elif choice == 4:
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Run Question 2
menu()
