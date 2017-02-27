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
    public_situations = tuple(combinations(deck, 5))
    evaluator = Evaluator()
    ret = dict()
    def _calculate_rank(board, hand)->int:
        total = hand + list(board)
        score = evaluator._seven(total)
        rank = evaluator.get_rank_class(score)
        return rank
    calculate_rank = partial(_calculate_rank, hand=hand)

    total_games = len(public_situations)

    ret = collections.Counter(map(calculate_rank, public_situations))
    for i in range(1, 9):
        pr = "{0}: {1} times, {2}%".format(evaluator.class_to_string(i), ret[i], ret[i]/total_games*100.0)
        print(pr)

main()
