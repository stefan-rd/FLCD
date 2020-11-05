class Transition:
    def __init__(self, startState, endState, symbol):
        self.__startState = startState
        self.__endState = endState
        self.__symbol = symbol

    def __str__(self):
        return str(self.__startState) + " -> " + self.__symbol + str(self.__endState)

    def getStartState(self):
        return self.__startState

    def getEndState(self):
        return self.__endState

    def getSymbol(self):
        return self.__symbol
