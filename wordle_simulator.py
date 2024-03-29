import random
from string import ascii_lowercase

class WordleSimulator:

    def __init__(self, solver, guesses):
        self.solver = solver
        self.word = self.generate_random_word_data()
        self.guesses_left = guesses

    def play(self):
        while True:
            guess = self.solver.get_best_suggestion()
            if guess == self.word:
                return True
            self.guesses_left -= 1
            if self.guesses_left == 0:
                return False
            score = self.score_guess(guess)
            self.solver.enter_result(guess, score)
            self.solver.get_possible_solutions()


    def score_guess(self, guess) -> list:
        """
        """
        response_word = ['' for i in range(len(self.word))]

        if guess == self.word:
            return list('2'*5)

        letter_counts = {}
        for letter in ascii_lowercase:
            letter_counts[letter] = 0

        for letter in self.word:
            letter_counts[letter] += 1

        for index, letter in enumerate(guess):
            if self.word[index] == letter:
                response_word[index] = letter
                letter_counts[letter] -= 1

        for index, letter in enumerate(guess):
            if self.word[index] == letter:
                continue
            if (letter in self.word) and (letter_counts[letter] > 0):
                response_word[index] = '?'
                letter_counts[letter] -= 1
            else:
                response_word[index] = '-'

        return response_word

    
    def generate_random_word_data(self) -> dict:
        """
        Generates a randomly chosen word from the word bank.
        """
        with open("target_words.txt") as file:
            words = file.readlines()

            
        word = random.choice(words).strip('\n') 
        return word