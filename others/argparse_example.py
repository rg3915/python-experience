import argparse


def calc_double(value):
    print(int(value) * 2)


def calc_square(value):
    print(int(value) ** 2)


parser = argparse.ArgumentParser(description='Argparse test examples.')
parser.add_argument(
    '-d',
    type=calc_double,
    default=0,
    help='Calculate Double of value.'
)
parser.add_argument(
    '-s',
    type=calc_square,
    default=0,
    help='Calculate Square of value.'
)
args = parser.parse_args()
