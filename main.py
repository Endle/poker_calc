import pymontecarlo
from deuces.deuces.card import Card
#from deuces import card

def generate_set():
    suit = "shdc"
    rank = [str(i) for i in range(2,10)] + ['T', 'J', 'Q', 'K', 'A']
    l = (Card.new(b+a) for a in suit for b in rank)
    return list(l)

Card.print_pretty_cards(generate_set()[0:10])
