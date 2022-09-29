from hangman_game.algorithm import Game
from hangman_game.status_board import StatusBoard

def char_list(char):
    return ''.join(char)

game = Game()
word = game.words()

letters_count = len(word)

print(f'The word consists of {letters_count} letters.')
print('Guess the letters to reveal the hidden word.')

while game.status_board == StatusBoard.IN_PROGRESS:
    letter = input('Pick a letter.\n')
    process = game.guess_letter(letter)

    print(char_list(process))

    print(f'Remaining tries = {game.remaining_attempts}')
    print(f'Previous letters: {char_list(game.attempts)}')

if game.status_board == StatusBoard.LOST:
    print("You've lost!")
    print(f'The word was: {word}')
else:
    print("Congrats! You've won!")



