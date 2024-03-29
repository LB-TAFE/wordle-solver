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
        help_message = """Registered commands:

        help - displays this message

        exit - exits the program

        weigh - weighs the letters in the word bank and saves the weights

        guess <word> <score> - enters a guess and the score given by the game, where - is a wrong letter, ? is a misplaced letter, and a letter is a match. Example: guess paper ??-er

        reset - resets the solver

        possible - displays the current possible solutions

        suggestion - displays the best suggestion based on the current possible solutions

        clear - clears the screen
        """
        print(f"{help_message}\n")
        self.get_best_suggestion()
        print()
        while True:
            command = input("$: ").lower().split(' ')
            match command[0]:
                case "help":
                    print(f"{help_message}\n")
                
                case "exit":
                    print("Bye")
                    break

                case "weigh":
                    print("Working..")
                    self.sync_letter_weights()
                    print("Letters weighed")
                    self.load_letter_weights()
                    print("Letter weights loaded")

                case "guess":
                    if len(command) != 3:
                        if len(command) == 4 and command[3] == "":
                            pass
                        else:
                            print("This command takes 2 arguments: <word>, <score>")
                            continue
                    if (len(command[1]) != 5) or (len(command[2]) != 5):
                        print("<word> and <score> must be 5 characters long")
                        continue
                    self.enter_result(command[1], command[2])
                    self.get_possible_solutions()
                    self.get_best_suggestion()
                    print()

                case "reset":
                    self.__init__()

                case "possible":
                    print(self.word_list, "\n")

                case "suggestion":
                    self.get_best_suggestion()
                    print()

                case "clear":
                    print("\033[H\033[J", end="")

                case "":
                    continue

                case _:
                    print("Invalid command")



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
        
        print(f"Best words: {best_words}\nSuggested word: {random.choice(best_words)}")


    def return_best_suggestion(self):
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
