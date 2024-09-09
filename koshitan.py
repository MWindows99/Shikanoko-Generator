import random
from collections import defaultdict

class MarkovChain:
    def __init__(self):
        self.model = defaultdict(lambda: defaultdict(int))

    def doTraining(self, data):
        for i in range(len(data) - 1):
            currentState = data[i]
            nextState = data[i + 1]
            self.model[currentState][nextState] += 1

    def nextCharacter(self, currentState):
        nextStates = self.model[currentState]
        total = sum(nextStates.values())
        randomVal = random.uniform(0, total)
        cumulative = 0
        for state, count in nextStates.items():
            cumulative += count
            if randomVal <= cumulative:
                return state
        return None

    def generateString(self, start, length):
        result = [start]
        currentState = start
        for _ in range(length - 1):
            nextStates = self.nextCharacter(currentState)
            if not nextStates:
                break
            result.append(nextStates)
            currentState = nextStates
        return "".join(result)

    def generateUntilMatch(self, match, start, length):
        counts = 0
        while True:
            generatedString = self.generateString(start, length)
            counts += 1
            yield counts, generatedString
            if generatedString == match:
                break

data = "しかのこのこのここしたんたん"
mc = MarkovChain()
mc.doTraining(data)

generatedText = mc.generateUntilMatch(match=data, start=data[0], length=len(data))

for count, text in generatedText:
    print(count, text)
