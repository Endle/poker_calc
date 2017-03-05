from deuces.deuces.card import Card
from deuces.deuces.evaluator import Evaluator
from deuces.deuces.lookup import LookupTable
from itertools import combinations
from functools import partial
import collections

def generate_set():
    suit = "shdc"
    rank = [str(i) for i in range(2,10)] + ['T', 'J', 'Q', 'K', 'A']
    l = (Card.new(b+a) for a in suit for b in rank)
    return l


def main():
    deck_tuple = generate_set()
    deck = set(deck_tuple)
    evaluator = Evaluator()
    ret = dict()
    def _calculate_rank(board, hand)->int:
        total = list(hand) + list(board)
        score = evaluator._seven(total)
        rank = evaluator.get_rank_class(score)
        return rank
    while True:
        print("Print two cards, or Q for quit")
        order = input()
        order = order.strip()
        print(order)
        if order.lower() == 'q':
            break
        try:
            hand = [Card.new(order[:2]), Card.new(order[2:])]
        except (KeyError, IndexError):
            print("Wrong card code")
            continue
        Card.print_pretty_cards(hand)
        deck -= set(hand)
        public_situations = combinations(deck, 5)
        calculate_rank = partial(_calculate_rank, hand=hand)
        ret = collections.Counter(map(calculate_rank, public_situations))
        total_games = sum(ret.values())
        for i in range(1, 10):
            pr = "{0:16s}: {1:6d} times, {2:.2f}%".format(evaluator.class_to_string(i), ret[i], ret[i]/total_games*100.0)
            print(pr)
            deck = set(deck_tuple)
        break
    import sys; sys.exit(0)

main()
