# AUTOGENERATED! DO NOT EDIT! File to edit: 00_core.ipynb (unless otherwise specified).

__all__ = ['number_sum']

# Cell
def number_sum(text):

    for line in text:
        y = re.findall("[0-9]+", text)

    sums = 0
    for list in y:
        number = int(list)
        sums = sums + number
    print('The total is:', sums)