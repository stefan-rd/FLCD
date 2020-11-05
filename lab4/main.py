from FA import FA

def run():
    fileName = "FA.in"
    try:
        fa = FA(fileName)
    except Exception as e:
        print(e)
        return
    menu = "0. Exit\n" \
           "1. Set of states.\n" \
           "2. Alphabet.\n" \
           "3. Transitions.\n" \
           "4. Initial state.\n" \
           "5. Final states.\n"
    while True:
        try:
            print(menu)
            choice = input("Enter option: ")
            if choice == "0":
                return
            elif choice == "1":
                print(fa.getStates())
            elif choice == "2":
                print(fa.getAlphabet())
            elif choice == "3":
                for transition in fa.getTransitions():
                    print(transition)
            elif choice == "4":
                print(fa.getInitialState())
            elif choice == "5":
                print(fa.getFinalStates())
            else:
                continue
        except Exception as e:
            print(e)


run()

