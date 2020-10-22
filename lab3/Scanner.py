from PIF import PIF
from SymbolTable import SymbolTable
import re


class Scanner:
    def __init__(self, tokenFile):
        self.__tokens = []
        file = open(tokenFile, 'r')
        lines = file.readlines()

        for line in lines:
            self.__tokens.append(line.strip())

        print(self.__tokens)

    def scan(self, filename):
        symbolTableIdentifiers = SymbolTable(37)
        symbolTableConstants = SymbolTable(37)
        pif = PIF()

        file = open(filename, 'r')
        lines = file.readlines()

        regexForIdentifiers =

        if self.__tokens[2] == '+' or self.__tokens[2] == "*" or self.__tokens[2] == ".":
            regexForTokens = '\\' + self.__tokens[2]
        else:
            regexForTokens = self.__tokens[2]

        for j in range(3, len(self.__tokens)):
            if self.__tokens[j] == '+' or self.__tokens[j] == "*" or self.__tokens[j] == ".":
                regexForTokens += "|\\" + self.__tokens[j]
            else:
                regexForTokens += "|" + self.__tokens[j]
        print(regexForTokens)

        count = 0
        for line in lines:
            line = line.strip()
            tokensOnLine = line.strip().split()
            tokens = []
            for token in tokensOnLine:
               tokens = tokens + re.split('(' + regexForTokens +')', token)
            while ('' in tokens):
                tokens.remove('')
            while (None in tokens):
                tokens.remove(None)

            for i in range(0, len(tokens)):
                if tokens[i] in self.__tokens:
                    pif.genPIF(tokens[i], (0, 0))
            print("Line{}: {}".format(count, tokens))
            count += 1

        print(pif.getPIF())
        file.close()


scanner = Scanner('token.in')
scanner.scan('p1.txt')

#prima linie linkul cate github, dupa o diagrama simpla si un regex simplu