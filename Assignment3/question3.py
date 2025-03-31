# Get the word to be replaced and the new word from user input
search_word = input('which word do you want to replace: ')
replace_word = input('Enter new word: ')

# Open the file in read text mode and read its contents
with open('newfile.txt', 'rt') as file:
    content = file.read()

# Replace all occurrences of the search word with the replace word
content = content.replace(search_word, replace_word)

# Open the file in write text mode and write the modified content back to the file
with open('newfile.txt', 'wt') as file:
    file.write(content)

# Open the file again in read text mode and print the updated contents
with open('newfile.txt', 'rt') as file:
    print(file.read())

