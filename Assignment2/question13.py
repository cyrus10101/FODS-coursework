# Function to convert a word into a set of unique letters
def convert(word):
    lst = []
    for i in word:
        lst.append(i)
    return set(lst)


# Function to find common letters between two input words
def word_intersection():
    # Get input words from user
    word1 = input("Enter your first word: ")
    word2 = input("Enter you second word: ")
    
    # Convert words to sets of unique letters
    word1_set = convert(word1)
    word2_set = convert(word2)
    
    # Find common letters using set intersection
    common_letters = word1_set & word2_set
    print(f"Common Letters of two words are: {common_letters}")
    
# Call the main function to start the program
word_intersection()