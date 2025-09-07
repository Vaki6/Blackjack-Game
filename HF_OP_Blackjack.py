import sys
import random

class Jatekos:

    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def calculate_score(self):
        return sum(int(card) for card in self.hand)

    
    def show_hand(self):
        print(f'{self.name} lapjai: ' + ', '.join(self.hand))
        print(f'Pontszám: {self.calculate_score()}')

class Blackjack:
    def __init__(self):
        self.player_name =input('Kérlek add meg a neved!  ').strip() or 'Játékos'
        
    def play(self):
        print(f'Szia {self.player_name}! Kezdjük a játékot!')

        jatekos_kez = random.randint(2,11) + random.randint(2,11)
        print(f'A játékos kéz összesen: {jatekos_kez}')


        while jatekos_kez <= 21:
            valasz = input('Kérsz még lapot? (igen/nem): ').strip().lower()
            if valasz == 'igen':
                uj_lap = random.randint(2, 11)
                jatekos_kez += uj_lap
                print(f'Az új lapod {uj_lap}, a kézben összesen: {jatekos_kez}')
            else:
                print(f'Megálltál: a kezedben {jatekos_kez} érték van.')
                break

        if jatekos_kez > 21:
            print(f'Sajnálom {self.player_name}, vesztettél!')
            sys.exit()

        bank_kez = random.randint(2,11) + random.randint(2,11)
        print(f'A bank kezében összesen {bank_kez} érték van')

        while bank_kez < 17:
            uj_lap = random.randint(2, 11)
            bank_kez += uj_lap
            print(f'A bank uj lapja {uj_lap}, kezében összesen {bank_kez} érték van!')

        if bank_kez > 21:
            print(f'A {self.player_name} nyert!')
        elif bank_kez > jatekos_kez:
            print('A Bank nyert')
        elif bank_kez == jatekos_kez:
            print('Döntetlen! A Bank nyert!' )
        else:
            print(f'Gratulálunk {self.player_name} nyertél')

if __name__ == '__main__':
    
    game = Blackjack()
    game.play()




