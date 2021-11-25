class Player:
    def __init__(self):
        self.choice = None

class Computer(Player):
    def __init__(self):
        super().__init__()

    def make_choice(self, otherplayer, choices):
        for i in choices:
            self.choice = i
            if check_win(self, otherplayer) == self:
                return self.choice
            else:
                self.choice = None
                continue


def check_win(player, otherplayer):
    if (player.choice == 'r' and otherplayer.choice == 's') or (player.choice == 's' and otherplayer.choice == 'p') or (player.choice == 'p' and otherplayer.choice == 'r'):
        winner = player
    else:
        winner = otherplayer

    return winner

def main():
    choices = ['r', 'p', 's']
    player = Player()
    ai = Computer()

    player.choice = input("Pick your choice! ")
    if player.choice in choices:
        choices.remove(player.choice)
        ai.choice = ai.make_choice(player, choices)
        print(f"Computer chose {ai.choice}")

        if check_win(player, ai) == player:
            print("you win!")
            main()
        else:
            print("you lost!")
            main()

if __name__ == "__main__":
    main()


