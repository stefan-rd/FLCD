from Transition import Transition

class FA:
    def __init__(self, fileName):
        self.__states = []
        self.__alphabet = []
        self.__transitions = []
        self.__finalStates = []
        self.__initialState = None
        self.initialiseFromFile(fileName)

    def initialiseFromFile(self, fileName):
        with open(fileName, 'r') as file:
            self.__initialState = file.readline().strip()
            self.__states.append(self.__initialState)
            numberOfStates = int(file.readline().strip())
            for i in range(0, numberOfStates):
                stateName = file.readline().strip()
                if stateName != self.__initialState:
                    self.__states.append(stateName)
            numberOfFinalStates = int(file.readline().strip())
            for i in range(0, numberOfFinalStates):
                stateName = file.readline().strip()
                self.__finalStates.append(stateName)
            for finalState in self.__finalStates:
                if finalState not in self.__states:
                    raise Exception("Final state not in state list!")
            if self.__initialState not in self.__states:
                raise Exception("Initial state not in state list!")
            numberOfSymbols = int(file.readline().strip())
            for i in range(0, numberOfSymbols):
                self.__alphabet.append(file.readline().strip())
            numberOfTransitions = int(file.readline().strip())
            for i in range(0, numberOfTransitions):
                transition = file.readline().strip().split(',')
                if len(transition) == 2:
                    transition.append('')
                self.__transitions.append(Transition(transition[0], transition[2], transition[1]))
            for transition in self.__transitions:
                if transition.getEndState() not in self.__states and transition.getEndState() != '':
                    raise Exception("Transition state not in state list!")
                if transition.getStartState() not in self.__states:
                    raise Exception("Transition state not in state list!")
                if transition.getSymbol() not in self.__alphabet:
                    raise Exception("Symbol not in alphabet!")

    def getStates(self):
        return self.__states

    def getAlphabet(self):
        return self.__alphabet

    def getFinalStates(self):
        return self.__finalStates

    def getInitialState(self):
        return self.__initialState

    def getTransitions(self):
        return self.__transitions

    def verifySequence(self, sequence):
        currentState = self.__initialState
        for symbol in sequence:
            print(symbol)







