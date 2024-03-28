from string import ascii_lowercase
import random

class WordleSolver:

    def __init__(self):

        self.WORDBANK_PATH = 'target_words.txt'
        self.word_list = self.load_words()
        self.chars_not_in_word = []
        self.characters_with_known_wrong_indexes = {}
        for char in ascii_lowercase:
            self.characters_with_known_wrong_indexes[char] = []
        self.word_theory = ['-', '-', '-', '-', '-']

    def main(self):
        while True:
            self.make_suggestion()
            user_input = input(">> ")
            split_input = user_input.split(' ')
            self.enter_result(split_input[0], split_input[1])
            self.get_possible_solutions()

    def make_suggestion(self):
        ranked_suggestions = {}
        for word in self.word_list:
            ranked_suggestions[word] = 0

        for word in self.word_list:
            for index, char in enumerate(word):
                if char not in word[:index]:
                    ranked_suggestions[word] += 1

        best_score = max(ranked_suggestions.values())
        best_words = []

        for word in ranked_suggestions:
            if ranked_suggestions[word] == best_score:
                best_words.append(word)

        for word in best_words:
            for char in word:
                if char in 'aeiou':
                    ranked_suggestions[word] += 1

        best_score = max(ranked_suggestions.values())
        best_words = []
        for word in self.word_list:
            if ranked_suggestions[word] == best_score:
                best_words.append(word)

        print(f"All possible words: {self.word_list}\n")
        print(f"Best words: {best_words}\n")
        print(f"Suggestion: {random.choice(best_words)}")



    def load_words(self):
        word_list = []
        with open(self.WORDBANK_PATH) as file:
            all_lines = file.readlines()

        for line in all_lines:
            word_list.append(line.strip('\n'))

        return word_list

    def get_possible_solutions(self):
        list_one = []

        for word in self.word_list:
            for index, char in enumerate(word):
                if char in self.chars_not_in_word:
                    break
                elif index in self.characters_with_known_wrong_indexes[char]:
                    break
                elif char not in self.characters_with_known_wrong_indexes:
                    break
            else:
                list_one.append(word)

        list_two = []
        for word in self.word_list:
            for index, char in enumerate(word):
                if (self.word_theory[index] == '-'):
                    continue
                if (self.word_theory[index] != char):
                    break
            else:
                list_two.append(word)

        final_list = []
        for word in list_one:
            if word in list_two:
                final_list.append(word)

        self.word_list = final_list


    def enter_result(self, entered_word, result_given):
        chars_may_be_in_word = []
        for index, char in enumerate(entered_word):
            if result_given[index] == char:
                self.word_theory[index] = char
                chars_may_be_in_word.append(char)
                continue
            elif result_given[index] == '?':
                self.characters_with_known_wrong_indexes[char].append(index)
                chars_may_be_in_word.append(char)
            elif char in chars_may_be_in_word:
                continue
            elif char not in chars_may_be_in_word:
                self.chars_not_in_word.append(char)



if __name__ == '__main__':
    solver = WordleSolver()
    solver.main()