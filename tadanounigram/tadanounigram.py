import os

import pickle
from collections import namedtuple, Counter

MOJIBAN = [
    'アイウエオ',
    'カキクケコ',
    'サシスセソ',
    'タチツテト',
    'ナニヌネノ',
    'ハヒフヘホ',
    'マミムメモ',
    'ヤユヨ',
    'ラリルレロ',
    'ワヲンー'
]

ALL_KATAKANA = ''.join(MOJIBAN)

_dir = os.path.dirname(__file__)
_path = os.path.join(_dir, 'lib', 'count_100000sentence.pickle')

with open(_path, 'rb') as f:
    _COUNT = pickle.load(f)

class Position(namedtuple('Position', ['x', 'y'])):
    pass

class Frequency(namedtuple('Frequency',['target', 'total'])):
    pass

def mozi2position(mozi):
    for idx, same_cons in enumerate(MOJIBAN):
        if not mozi in same_cons:
            continue
        cons = idx
        vow = same_cons.index(mozi)
        return Position(x=cons, y=vow)
    raise ValueError(f'「{mozi}」は文字盤に存在しません。')

def position2mozi(x, y):
    return MOJIBAN[x][y]

def check_existence(mozi):
    if mozi in ALL_KATAKANA:
        return True
    else:
        return False

def frequency(mozi):
    if not check_existence(mozi):
        raise ValueError(f'「{mozi}」は文字盤に存在しません。')
    return Frequency(
        target = _COUNT[mozi],
        total=sum(_COUNT.values())
    )

def probability(mozi):
    freq = frequency(mozi)
    return freq.target / freq.total
