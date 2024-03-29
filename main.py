from string import ascii_lowercase
import random

class WordleSolver:


    def __init__(self):

        self.WORDBANK_PATH = 'target_words.txt'
        self.WORD_WEIGHT_PATH = 'word_weights.txt'
        self.word_list = self.load_words()
        self.chars_not_in_word = []
        self.characters_with_known_wrong_indexes = {}
        for char in ascii_lowercase:
            self.characters_with_known_wrong_indexes[char] = []
        self.letter_weights = self.load_letter_weights()
        self.word_theory = ['-', '-', '-', '-', '-']
        self.chars_in_word = []


    def main(self):
        print("Syntax: <word> <score> | - for not in word, ? for in wrong place, <char> for in correct place\n")
        while True:
            self.make_suggestion()
            user_input = input(">> ")
            split_input = user_input.split(' ')
            self.enter_result(split_input[0], split_input[1])
            self.get_possible_solutions()
            print(f"Not in word: {self.chars_not_in_word}")
            print(f"Other: {self.characters_with_known_wrong_indexes}")


    def sync_letter_weights(self):
        word_appearences = {}
        for char in ascii_lowercase:
            word_appearences[char] = 0
        with open(self.WORDBANK_PATH) as file:
            all_lines = file.readlines()
        
        for line in all_lines:
            word = line.strip('\n')
            for char in word_appearences:
                if char in word:
                    word_appearences[char] += 1

        for char in word_appearences:
            word_appearences[char] = (word_appearences[char] / len(self.word_list)) * 100

        with open(self.WORD_WEIGHT_PATH, 'w') as file:
            for char in word_appearences:
                file.write(f"{char} {word_appearences[char]}\n")
                

    def load_letter_weights(self):
        letter_weights = {}
        for char in ascii_lowercase:
            letter_weights[char] = 0
        with open(self.WORD_WEIGHT_PATH) as file:
            lines = file.readlines()

        for line in lines:
            processed_text = line.strip('\n').split(' ')
            letter_weights[processed_text[0]] = float(processed_text[1])

        return letter_weights


    def make_suggestion(self):
        ranked_suggestions = {}
        for word in self.word_list:
            ranked_suggestions[word] = 0
            for char in self.letter_weights:
                if char in word:
                    ranked_suggestions[word] += self.letter_weights[char]


        best_score = max(ranked_suggestions.values())
        best_words = []
                    
        for word in self.word_list:
            if ranked_suggestions[word] == best_score:
                best_words.append(word)
        
        print(f"All possible words: {self.word_list}\n")
        print(f"Best words: {best_words}\n")
        print(f"Suggestion: {random.choice(best_words)}")


    def get_best_suggestion(self):
        ranked_suggestions = {}
        for word in self.word_list:
            ranked_suggestions[word] = 0
            for char in self.letter_weights:
                if char in word:
                    ranked_suggestions[word] += self.letter_weights[char]*10
            for char in word:
                ranked_suggestions[word] += self.letter_weights[char]


        best_score = max(ranked_suggestions.values())
        best_words = []
                    
        for word in self.word_list:
            if ranked_suggestions[word] == best_score:
                best_words.append(word)
        
        return random.choice(best_words)
    

    def load_words(self):
        word_list = []
        with open(self.WORDBANK_PATH) as file:
            all_lines = file.readlines()

        for line in all_lines:
            word_list.append(line.strip('\n'))

        return word_list


    def get_possible_solutions(self):
        guess_list = []

        for word in self.word_list:
            for index, char in enumerate(word):
                if char in self.chars_not_in_word:
                    break
                elif index in self.characters_with_known_wrong_indexes[char]:
                    break
                elif self.word_theory[index] == '-':
                    continue
                elif self.word_theory[index] != char:
                    break
            else:
                for char in self.chars_in_word:
                    if char not in word:
                        break
                else:
                    guess_list.append(word)

        self.word_list = guess_list


    def enter_result(self, entered_word, result_given):
        for index, char in enumerate(entered_word):
            if result_given[index] == char:
                self.word_theory[index] = char
                self.chars_in_word.append(char)
            elif result_given[index] == '?':
                self.characters_with_known_wrong_indexes[char].append(index)
                self.chars_in_word.append(char)
            elif char not in self.chars_in_word:
                self.chars_not_in_word.append(char)



if __name__ == '__main__':
    solver = WordleSolver()
    solver.main()
