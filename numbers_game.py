class NumbersGame:
    def __init__(self):
        self.data = []
        # Initially: hypothesis space
        self.version_space = {'Power2': [1,2,4,8,16,32,64],
                            'Power4': [1,4,16,64],
                            'Even': [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100],
                            'Prime': [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97],
                            }
        # Keeping all original concepts, so they can be accessed after their deletion
        self.hypothesis_space = dict(self.version_space)

    def feed(self, x):
        self.data.append(x)
        for k, hypo in list(self.version_space.items()):
            if x not in hypo:
                del self.version_space[k]

    # Occam's Razor. Helper function.
    def razor(self, concept):
        return (1 / len(self.version_space[concept])) ** len(self.data)

    # Given a hypothesis, returns the probability that its true
    def hypothesis_probability(self, concept):
        if concept not in self.version_space:
            return 0
        sum = 0
        for hypo in self.version_space:
            sum += self.razor(hypo)
        return self.razor(concept) / sum

    # Prints the probability of each hypothesis (including)
    def print_probabilities(self):
        for k, hypo in self.hypothesis_space.items():
            print("{0} probability = {1}".format(k, self.hypothesis_probability(k)))


if (__name__ == '__main__'):
    game = NumbersGame()
    game.feed(16)
    game.print_probabilities()
    game.feed(4)
    game.print_probabilities()
    game.feed(64)
    game.print_probabilities()
