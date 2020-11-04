class PIF:

    def __init__(self):
        self.__list = []
        
    def genPIF(self, token, positionPair):
        self.__list.append((token, positionPair))

    def getPIF(self):
        return self.__list