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
'''
文字盤を表すリスト

Example:
    >>> MOJIBAN[0][0]
    'ア'
    >>> MOJIBAN[0][3]
    'エ'
    >>> MOJIBAN[3][0]
    'タ'
'''

ALL_KATAKANA = ''.join(MOJIBAN)
'''
文字盤に含まれる文字を連結したもの

Example:
    >>> for i in tadanounigram.ALL_KATAKANA:
    ...     print(i)
    ...
    ア
    イ
    ウ
    エ
    オ
    カ
    ⋮
'''

_dir = os.path.dirname(__file__)
_path = os.path.join(_dir, 'lib', 'count_100000sentence.pickle')

with open(_path, 'rb') as f:
    _COUNT = pickle.load(f)

class Position(namedtuple('Position', ['x', 'y'])):
    '''
    文字盤の座標を表すクラス

    Attributes:
        x (int): 列番号
        y (int): 行番号
    Note:
        :py:func:`collections.namedtuple` で生成したクラス
    See Also:
        :py:func:`collections.namedtuple`
    '''
    pass

class Frequency(namedtuple('Frequency',['target', 'total'])):
    '''
    文字の出現度数を表すクラス

    Attributes:
        target (int): 対象文字の出現度数
        total (int): 全文字の出現度数
    Note:
        :py:func:`collections.namedtuple` で生成したクラス
    See Also:
        :py:func:`collections.namedtuple`
    '''
    pass

def mozi2position(mozi):
    '''
    文字から座標を求める関数。
    引数として :data:`tadanounigram.MOJIBAN` や
    :data:`tadanounigram.ALL_KATAKANA` に含まれるものを想定。

    Args:
        mozi (str): カタカナ1文字。
    Returns:
        tadanounigram.Position: 文字盤の座標
    Raises:
        ValueError:
            引数が :data:`tadanounigram.MOJIBAN` や
            :data:`tadanounigram.ALL_KATAKANA` に含まれない文字の場合に発生。
    '''
    for idx, same_cons in enumerate(MOJIBAN):
        if not mozi in same_cons:
            continue
        cons = idx
        vow = same_cons.index(mozi)
        return Position(x=cons, y=vow)
    raise ValueError(f'「{mozi}」は文字盤に存在しません。')

def position2mozi(x, y):
    '''
    座標を引数に取り、文字盤上の文字を返す関数。

    Args:
        x (int): 列番号
        y (int): 行番号
    Returns:
        str: 文字盤上の文字
    Note:
        ``tadanounigram.MOJIBAN[x][y]`` と等価
    See Also:
        :data:`tadanounigram.MOJIBAN`
    '''

    return MOJIBAN[x][y]

def check_existence(mozi):
    '''
    文字を引数に取り、文字盤に存在するかどうかを判定する関数

    Args:
        mozi (str): 文字
    Returns:
        bool: 存在するなら ``True`` ,存在しなければ ``False`` を返す。
    Note:
        ``mozi in tadanounigram.ALL_KATAKANA`` と等価
    See Also:
        :data:`tadanounigram.ALL_KATAKANA`
    '''

    if mozi in ALL_KATAKANA:
        return True
    else:
        return False

def frequency(mozi):
    '''
    文字を引数に取り、出現頻度を返す関数。

    Args:
        mozi (str): 文字
    Returns:
        tadanounigram.Frequency: 出現頻度
    Raises:
        ValueError:
            :func:`tadanounigram.check_existence` が ``False`` だと発生
    See Also:
        :func:`tadanounigram.check_existence`
        :class:`tadanounigram.Frequency`
    '''

    if not check_existence(mozi):
        raise ValueError(f'「{mozi}」は文字盤に存在しません。')
    return Frequency(
        target = _COUNT[mozi],
        total=sum(_COUNT.values())
    )

def probability(mozi):
    '''
    文字を引数に取り、出現確率を返す関数。

    Args:
        mozi (str): 文字
    Returns:
        float: 出現確率
    Raises:
        ValueError:
            :func:`tadanounigram.check_existence` が ``False`` だと発生
    See Also:
        :func:`tadanounigram.check_existence`
        :func:`tadanounigram.frequency`
        :class:`tadanounigram.Frequency`
    '''

    freq = frequency(mozi)
    return freq.target / freq.total
