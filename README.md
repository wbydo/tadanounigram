# tadanounigram
simple KATAKANA 1-gram

- Documentation: https://wbydo.github.io/tadanounigram/
- PyPi: https://pypi.org/project/tadanounigram/

## Installation
``%pip install tadanounigram``

## Basic Usage
```python
>>> import tadanounigram as tdn
>>> tdn.probability('ユ')
0.008758420624531816
>>> tdn.probability('ニ')
0.024601601530203743
>>> tdn.probability('ク')
0.03201051211394553
>>> tdn.probability('ラ')
0.011973469235356896
>>> tdn.probability('ム')
0.002282111892800012

>>> tdn.check_existence('グ')
False
```
