from deuces.deuces.card import Card
from deuces.deuces.evaluator import Evaluator
from deuces.deuces.lookup import LookupTable
from itertools import combinations

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
    for i in range(1,10):
        ret[i] = 0
    total_games = 0
    for i in public_situations:
        board = list(i)
        score = evaluator.evaluate(board, hand)
        rank = evaluator.get_rank_class(score)
        ret[rank] += 1
        total_games += 1

    for k,v in ret.items():
        pr = "{0}: {1} times, {2}%".format(evaluator.class_to_string(k), v, v/total_games*100.0)
        print(pr)

main()
