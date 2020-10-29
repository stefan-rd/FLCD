from PIF import PIF
from SymbolTable import SymbolTable
import re


class Scanner:
    def __init__(self, tokenFile):
        self.__reservedWordsAndSeparators = []

        with open(tokenFile, 'r') as file:
            self.__identifierCode = file.readline().strip()
            self.__constantCode = file.readline().strip()
            for line in file:
                self.__reservedWordsAndSeparators.append(line.strip())

        print(self.__reservedWordsAndSeparators)
        print(self.__identifierCode)
        print(self.__constantCode)


    def checkIfIdentifier(self, token):
        regexForIdentifiers = '^[a-zA-Z][a-zA-Z0-9]*'
        if re.fullmatch(regexForIdentifiers, token):
            return True
        else:
            return False

    def checkIfStringConstant(self, token):
        regexForStrings = '^\"[a-zA-Z0-9]*\"'
        if re.fullmatch(regexForStrings, token):
            return True
        else:
            return False

    def checkIfNumberConstant(self, token):
        regexForNumbers = '^(0|-?[1-9][0-9]*)'
        if re.fullmatch(regexForNumbers, token):
            return True
        else:
            return False

    def scan(self, filename):
        symbolTableIdentifiers = SymbolTable(37)
        symbolTableConstants = SymbolTable(37)
        pif = PIF()

        file = open(filename, 'r')
        lines = file.readlines()
        error = []

        count = 0
        for line in lines:
            line = line.strip()
            tokensOnLine = line.strip().split()
            tokens = []
            regexForTokens = "[^a-zA-Z0-9\"]"
            for token in tokensOnLine:
                tokens = tokens + re.split('(' + regexForTokens + ')', token)
            while ('' in tokens):
                tokens.remove('')
            while (None in tokens):
                tokens.remove(None)

            i = 0
            while i < len(tokens):
                j = i + 1
                if (i < len(tokens) - 1):
                    if tokens[i] == "=" and tokens[i + 1] == "=":
                        tokens[i] = "=="
                        j = i + 2
                if (i < len(tokens) - 2):
                    if tokens[i] == "=" and tokens[i + 1] == "/" and tokens[i + 2] == "=":
                        tokens[i] = "=/="
                        j = i + 3
                if (i < len(tokens) - 1):
                    if tokens[i] == "<" and tokens[i + 1] == "=":
                        tokens[i] = "<="
                        j = i + 2
                if (i < len(tokens) - 1):
                    if tokens[i] == ">" and tokens[i + 1] == "=":
                        tokens[i] = ">="
                        j = i + 2
                if tokens[i] in self.__reservedWordsAndSeparators:
                    pif.genPIF(tokens[i], (0, 0))
                else:
                    if self.checkIfIdentifier(tokens[i]):
                        pif.genPIF(self.__identifierCode, symbolTableIdentifiers.position(tokens[i]))
                    else:
                        if self.checkIfNumberConstant(tokens[i]):
                            pif.genPIF(self.__constantCode, symbolTableConstants.position(tokens[i]))
                        else:
                            if self.checkIfStringConstant(tokens[i]):
                                pif.genPIF(self.__constantCode, symbolTableConstants.position(tokens[i]))
                            else:
                                error.append("error on line " + str(count) + " for token " + tokens[i])
                i = j

            print("Line{}: {}".format(count, tokens))
            count += 1

        file.close()

        with open('PIF.out', 'w') as f:
          print('PIF:\n', pif.getPIF(), file=f)

        with open('ST_constants.out', 'w') as f:
          print('ST_constants:\n', str(symbolTableConstants), file=f)

        with open('ST_identifiers.out', 'w') as f:
          print('ST_identifiers:\n', str(symbolTableIdentifiers), file=f)

        if(error == []):
            print("Lexically correct.")
        else:
            print(error)


scanner = Scanner('token.in')
scanner.scan('p1err.txt')
