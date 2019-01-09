import random



class blackjack():

    def __init__(self):
        list_num=[n for n in range(1,11)]
        list_k=['J','Q','K']
        deck=(list_num+list_k)*4
        self.cards=(deck*6)
        random.shuffle(self.cards)
        random.shuffle(self.cards)
        self.mycard=[]
        self.busted=False
        self.total_points=0
        self.result=0

    def serve_card(self):
        card=self.cards[0]
        self.cards.pop(0)
        self.mycard.append(card)
        print(card,end=" ")
        return card
    
    def first_2_card(self):
        print(50*'-')
        print('New Round')
        self.busted=False
        # self.total_points=0
        self.mycard=[]
        for i in range(2):
            crd=self.serve_card()
    
    def ifBust(self):
        total_points=0
        for crd in self.mycard:
            if crd in ['J','Q','K']:
                crd_point=10
            else:
                crd_point=int(crd)
            total_points+=crd_point
        print('your current points',total_points)
        if total_points>21:
            self.busted=True
            print('Busted')
        elif total_points==21:
            self.busted=True
            self.result=1
            print('Black Jack!!!')
        else:
            self.busted=False
            print('Not Busted')

    def hit(self):
        self.serve_card()
        self.ifBust()

    def run(self):
        
        while True:
            self.first_2_card()
            while not self.busted:
                print(" ")
                hit_or_call = input('Hit(h) or Call(c)')
                if hit_or_call=='h':
                    self.hit()
                else:
                    self.first_2_card()


start_bj=blackjack()
start_bj.run()