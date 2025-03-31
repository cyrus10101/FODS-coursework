import shutil

try:
    shutil.copy('myfile.txt', 'newfile.txt')
    print('File copied succesfully...')
    
except FileNotFoundError:
    print('Error! File not found.')

except Exception as e:
    print(f'Error! {e}')