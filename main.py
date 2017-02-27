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
    deck = list(generate_set())
    hand = deck[5:7]
    deck = tuple(deck[:5] + deck[7:])
    public_situations = combinations(deck, 5)
    evaluator = Evaluator()
    ret = dict()
    def _calculate_rank(board, hand)->int:
        total = list(hand) + list(board)
        score = evaluator._seven(total)
        rank = evaluator.get_rank_class(score)
        return rank
    calculate_rank = partial(_calculate_rank, hand=hand)

    ret = collections.Counter(map(calculate_rank, public_situations))

    total_games = sum(ret.values())
    for i in range(1, 10):
        pr = "{0:16s}: {1:6d} times, {2:.2f}%".format(evaluator.class_to_string(i), ret[i], ret[i]/total_games*100.0)
        print(pr)

main()
