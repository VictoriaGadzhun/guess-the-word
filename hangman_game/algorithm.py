import random
from typing import Iterable

from hangman_game.invalid_operation_errors import InvalidOperationError as IOE
from hangman_game.status_board import StatusBoard


class Game:


    def __init__(self, mistakes: int = 8):
        if mistakes < 7 or mistakes > 10:
            raise ValueError('Number of mistakes can be from 5 to 10')

        self.__mistakes = mistakes
        self.__counter = 0
        self.__attempts = []
        self.__open_letters = []
        self.__status_board = StatusBoard.NOT_STARTED
        self.__word = ''

    def words(self) -> str:

        guess_word = []
        with open('data/WordsStockRus.txt', encoding="utf-8") as file:
            for line in file:
                guess_word.append(line.strip('\n'))

        rand_index = random.randint(0, len(guess_word) - 1)

        self.__word = guess_word[rand_index]

        self.__open_letters = [False for _ in self.__word]
        self.__status_board = StatusBoard.IN_PROGRESS

        return self.__word

    def guess_letter(self, letter: str) -> Iterable[str]:
        if self.counter == self.mistakes:
            raise IOE(f'Exceeded the maximum number of misses out of a possible {self.mistakes}.')

        if self.status_board != StatusBoard.IN_PROGRESS:
            raise IOE(f'Wrong status of game: {self.status_board}.')

        open_any = False
        result: list[str] = []

        for i, c in enumerate(self.__word):
            current_letter = self.__word[i]
            if current_letter == letter:
                self.__open_letters[i] = True
                open_any = True

            if self.__open_letters[i]:
                result.append(current_letter)
            else:
                result.append('-')

        if not open_any:
            self.counter += 1


        self.__attempts.append(letter)


        if self.__winning():
            self.__status_board = StatusBoard.WON
        elif self.counter == self.mistakes:
            self.__status_board = StatusBoard.LOST

        return result

    def __winning(self):
        for cur in self.__open_letters:
            if not cur:
                return False

        return True

    @property
    def status_board(self) -> StatusBoard:
        return self.__status_board

    @property
    def m_word(self) -> str:
        return self.__word

    @property
    def mistakes(self) -> int:
        return self.__mistakes

    @property
    def counter(self) -> int:
        return self.__counter

    @property
    def attempts(self) -> Iterable[str]:
        return sorted(self.__attempts)

    @property
    def remaining_attempts(self) -> int:
        return self.mistakes - self.counter

    @counter.setter
    def counter(self, value):
        self.__counter = value
