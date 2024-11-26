def gamble(bankroll):
    bankroll += 30
    print(bankroll)

def gamebleagain():
    global bankroll
    bankroll += bankroll

bankroll = 30

def main():
    gamebleagain()
    print(bankroll)
    gamble(bankroll)
    print(bankroll)
    gamebleagain()
    print(bankroll)

if __name__ == "__main__":
    main()


