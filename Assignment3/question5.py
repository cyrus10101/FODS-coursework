# Imports tabulate from tabulate.
from tabulate import tabulate

# counts words and storing it in dictionary words as keys and total number as values.
def count_same_word(para_set, para_list):
    count_dict = {}
    for word in para_set:
        count_dict[word] = para_list.count(word)
    return count_dict     

# opens file and reads content.
with open('count.txt', 'rt')as file:
    data = file.read()

# Converts string into list.
data_list = data.split()
# Converts list into set.
data_set = set(data_list)
# Counts total words in file content.
total_words = len(data_list)
# stores data returned by count_same_word function.
counted_dict = count_same_word(data_set, data_list)
# Converts dictionary into tuples.
tabular_tuple = tuple((i, j) for i, j in counted_dict.items())

# Displays ouptut.
print(f'\nTotal words in file content: {total_words}')
# Displays words and total words in tabular format.
print(tabulate(tabular_tuple[0:], headers =["Words", "Total"], tablefmt='fancy_grid'))