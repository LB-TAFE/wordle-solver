from main import WordleSolver
from wordle_simulator import WordleSimulator

successes = 0
fails = 0
exceptions = 0
exception_words = []
failed_words = []
guesses_allowed = 6
test_count = 100000

for i in range(test_count):
    solver = WordleSolver()
    simulator = WordleSimulator(solver, guesses_allowed)
    try:
        result = simulator.play()
        if result:
            successes += 1
            continue
        fails += 1
        if simulator.word not in failed_words:
            failed_words.append(simulator.word)
    except:
        exception_words.append(simulator.word)
        exceptions += 1

print(f"Exceptions: {exceptions}\nException Words: {exception_words}\n\nSuccesses: {successes}\nFails: {fails}\nFailed Words: {failed_words}\nSuccess rate: {successes / (successes + fails + exceptions) * 100}%\n\nTest count: {test_count}\nGuesses allowed: {guesses_allowed}")
# LATEST TEST RESULTS:
#
# Exceptions: 15
# Exception Words: ['order', 'order', 'order', 'order', 'order', 'order', 'order', 'order', 'order', 'order', 'order', 'order', 'order', 'order', 'order']
#
# Successes: 98804
# Fails: 1181
# Failed Words: ['riper', 'gauge', 'ionic', 'power', 'waver', 'wreak', 'taunt', 'rower', 'grave', 'crook', 'tatty', 'catch', 'rarer', 'jolly', 'crock', 'joker', 'wooer', 'rover', 'waste', 'piper', 'hatch', 'fever', 'fixer', 'brave', 'shake', 'found', 'shave', 'roger', 'witty', 'graze', 'finer', 'taste', 'tight', 'river', 'fatty', 'bobby', 'wound', 'jaunt', 'freed', 'daddy', 'boxer', 'skulk', 'frown', 'frank', 'chili', 'droll', 'drool', 'watch', 'mover', 'skull', 'conic', 'chill', 'odder', 'order']
# Success rate: 98.804%
#
# Test count: 100000
# Guesses allowed: 6