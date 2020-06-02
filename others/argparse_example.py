import argparse


def calc_double(value):
    result = int(value) * 2
    return result


def calc_square(value):
    result = int(value) ** 2
    return result


parser = argparse.ArgumentParser(description='Argparse test examples.')
parser.add_argument(
    '-n',
    '-number',
    type=int,
    default=0,
    help='Type a number.'
)
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

print(vars(args))
