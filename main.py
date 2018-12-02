from json import dumps
from collections import OrderedDict
from GenAlg import GenAlg
from MyGenAlg import MyGenAlg

def main():
    # read data from file
    bag, items = load("2.txt")
    # find solution
    genAlg = GenAlg(bag, items)
    myGenAlg = MyGenAlg(bag, items)
    res1 = genAlg.solve()
    res2 = myGenAlg.solve()
    # form the result
    result = {
        "1": nice(res1, items),
        "2": nice(res2, items)
    }
    # print result in json format
    print(dumps(result, indent=4))

def load(filename):
    """
    Load data from file
    """
    with open(filename, 'r') as file:
        bag = [ float(val) for val in file.readline().split() ]
        items = []
        for line in file:
            items.append([ float(val) for val in line.split() ])
    return (bag, items)

def nice(tpl, data):
    """
    Calculates the necessary values from tuple 0 and 1.
    Weight, volume, value and list of items.
    """
    weight = volume = value = 0
    items = []
    for i in range(len(tpl)):
        if tpl[i]:
            items.append(i)
            weight += data[i][0]
            volume += data[i][1]
            value  += data[i][2]
    return {
        "value":  round(value, 1),
        "weight": round(weight, 1),
        "volume": round(volume, 1),
        "items":  items
    }


if __name__ == '__main__':
    main()