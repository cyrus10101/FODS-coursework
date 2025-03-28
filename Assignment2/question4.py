#Function that accepts list of name and return sorted order of list

# Function that converts and return sorted list
def sorted_list(para):
    return sorted(para)

# Loop that runs until no exception are thrown.
while True:
    try:
        names = input("Enter names seperated with spaces: ")
        name_list = names.split()

        # Raise exception if there contain anything other than alphabet.
        if not all(name.isalpha() for name in name_list):
            raise Exception("names can be in alphabet.")
        
        print(f'Sorted Names: {sorted_list(name_list)}')
        break

    except Exception as e:
        print(f"Error! {e}")

