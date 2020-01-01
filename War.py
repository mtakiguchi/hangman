from random import shuffle


class Card:
    suits = ["スペード♠", "ハート♥", "ダイヤ♦", "クラブ♣"]

    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "J(11)", "Q(12)", "K(13)", "A(1)"]

    def __init__(self, v, s):
        """スート（マーク）も値も整数値です"""
        self.value = v
        self.suit = s
    
    def __lt__(self, c2) :
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False
    
    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False
    
    def __repr__(self):
        v = self.suits[self.suit] + "の" + self.values[self.value]
        return v

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2,15):
            for j in range(4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name

class Game:
    def __init__(self):
        name1 = input("プレーヤー1の名前-> ")
        name2 = input("プレーヤー2の名前-> ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner, len_card):
        w = "このラウンドは{}が勝ちました。残りカード: {}枚"
        w = w.format(winner, len_card)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = "{} は {}、{} は {} を引きました"
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print("戦争を始めます！")
        print("カードが2枚になるまで続けます。")
        print("数字のの強さ順は{}です。".format(" < ".join([lis for lis in Card.values if lis is not None])))
        print("マークの強さ順は{}です。".format(" < ".join(Card.suits)))
        while len(cards) >= 2:
            m = "q で終了、それ以外のキーでPlay:"
            response = input(m)
            if response == 'q':
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name, len(cards))
            else:
                self.p2.wins += 1
                self.wins(self.p2.name, len(cards))
        
        win = self.winner(self.p1, self.p2)
        result = "ゲーム終了、{}は{}勝、{}は{}勝。{} の勝利です！"
        result = result.format(self.p1.name,self.p1.wins,self.p2.name,self.p2.wins,win)
        print(result)

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "引き分け！"

game = Game()
game.play_game()