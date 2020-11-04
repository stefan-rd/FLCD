class PIF:

    def __init__(self):
        self.__list = []
        
    def genPIF(self, token, positionPair):
        self.__list.append((token, positionPair))

    def getPIF(self):
        pif = ""
        for element in self.__list:
            pif = pif + str(element) + "\n"
        return pif