# used with as file because it automatically closes file after getting out of block.
with open('myfile.txt', 'rt') as file:
    text = file.read()
    text = text.split()

    # Move cursor back to starting point
    file.seek(0)
    
    # counts line using generator experession
    lines_num = sum(1 for line in file)
    
word_count = len(text)
# calculates length of every words and sums it using generator expression
char_count = sum(len(word) for word in text)

# Displaying output
print(f'Number of line: {lines_num}')
print(f'Total words: {word_count}')
print(f'Total character: {char_count}')

