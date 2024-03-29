from main import WordleSolver
from wordle_simulator import WordleSimulator
import time

successes = 0
fails = 0
exceptions = 0
exception_words = []
failed_words = []
guesses_used = []
guesses_allowed = 6
test_count = 100000

start = time.perf_counter()
for i in range(test_count):
    solver = WordleSolver()
    simulator = WordleSimulator(solver, guesses_allowed)
    try:
        result = simulator.play()
        if result[0]:
            successes += 1
            guesses_used.append(guesses_allowed - result[1])
            continue
        fails += 1
        if simulator.word not in failed_words:
            failed_words.append(simulator.word)
            guesses_used.append(guesses_allowed - result[1])
    except:
        exception_words.append(simulator.word)
        exceptions += 1

end = time.perf_counter()
avg_guesses = sum(guesses_used) / len(guesses_used)
print(f"Exceptions: {exceptions}\nException Words: {exception_words}\n\nSuccesses: {successes}\nFails: {fails}\nFailed Words: {failed_words}\nSuccess rate: {successes / test_count * 100}%\nAverage guesses used: {avg_guesses}\n\nTests Run: {test_count}\nGuesses allowed: {guesses_allowed}\n\nTime taken: {end - start} seconds\nAverage Time taken: {(end - start) / test_count} seconds")
# LATEST TEST RESULTS
# Exceptions: 0
# Exception Words: []
#
# Successes: 98520
# Fails: 1480
# Failed Words: ['waste', 'skulk', 'brave', 'wooer', 'frown', 'tatty', 'taste', 'rarer', 'frank', 'jolly', 'hatch', 'shave', 'rover', 'wound', 'found', 'odder', 'waver', 'zesty', 'shake', 'graze', 'rower', 'grave', 'fever', 'catch', 'tight', 'crock', 'jaunt', 'bobby', 'conic', 'fixer', 'freed', 'chili', 'droll', 'wreak', 'piper', 'fifty', 'river', 'boxer', 'taunt', 'power', 'joker', 'roger', 'witty', 'fatty', 'watch', 'gauge', 'finer']
# Success rate: 98.52%
# Average guesses used: 2.7536092201243823
#
# Tests Run: 100000
# Guesses allowed: 6
#
# Time taken: 388.97960090002744 seconds
# Average Time taken: 0.0038897960090002745 seconds