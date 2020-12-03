# Задача 2.
# Закодируйте любую строку по алгоритму Хаффмана.

ABC = 'flyingcircus'

print(ABC)

class Coffee_Tree:

    def __init__(self, left = None, right = None):
        self.left = left
        self.right = right

    def child(self):
        return (self.left, self.right)


def coding(point, left = 1, _str = ''):
    if type(point) is str:
        return {point: _str}
    (_left, _right) = point.child()
    a = dict()
    a.update(coding(_left, 1, _str + '0'))
    a.update(coding(_right, 0, _str + '1'))
    return a


_frequency = {}
for i in ABC:
    if i in _frequency:
        _frequency[i] += 1
    else:
        _frequency[i] = 1
_frequency = sorted(_frequency.items(), key = lambda x: x[1], reverse = True)

crossing = _frequency

while len(crossing) > 1:
    (key_1, val_1) = crossing[-1]
    (key_2, val_2) = crossing[-2]
    crossing = crossing[:-2]
    node = Coffee_Tree(key_1, key_2)
    crossing.append((node, val_1 + val_2))
    crossing = sorted(crossing, key=lambda x: x[1], reverse=True)

zero_one = coding(crossing[0][0])

a = []

for (i, j) in _frequency:
    a.append(zero_one[i])

print("".join([str(i) for i in a]))