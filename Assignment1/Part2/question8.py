import random
class guessing_number:
    def __init__(self):
        self.heart = 5
        self.level= 1
        self.tries = 0
        self.max_num = self.level * 10
        self.random_number = random.randint(1, self.max_num)

    def display_level(self):
        print(f'Level: {self.level}')
        print(f'You have to guess between (1 To {self.max_num})')
        print()

    def display_life(self):
        for i in range(0, self.heart):
            print('❤️', end = ' ')
        print()

    def random_number_generator(self):
        self.max_num = self.level * 10
        self.random_number = random.randint(1, self.max_num)
            
    def game_over(self):
        if self.heart <= 0:
            print('You Lose! Better Luck next time.')
            return True
        else:
            return False
        
    def next_level(self, guessed_number):
        if guessed_number == self.random_number:
            print(f'Congrulation! You won on {self.tries} Tries.')
            self.level += 1
            self.heart = 5
            self.tries = 0
            self.random_number_generator()
            print('\n________________________________________________________________________________________________')
            self.display_level()
            self.display_life()
            return True
        else:
            return False
    def hint(self, guessed_number):
        if guessed_number < self.random_number:
            print('Try guessing Bigger number.')
        else:
            print('Try guesssing Small number.')
    

        
    def play(self):
        self.display_level()
        self.display_life()
        while True:
            try:
                guess = int(input('Your guess: '))
                self.tries += 1
                self.heart -= 1
                if self.next_level(guess):
                    random
                    continue

                if self.game_over():
                    break

                self.hint(guess)

                print()
                self.display_life()

            except ValueError:
                print('Error! You can only enter number.')

            except Exception as e:
                print(f'Error! {e}')

if __name__ == "__main__":
    run = guessing_number()
    run.play()
    


                 
                

