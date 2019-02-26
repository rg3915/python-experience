readme.md



$ mypy example01.py 
example01.py:2: error: Incompatible return value type (got "str", expected "int")

$ mypy example01.py 
example01.py:4: error: Argument 1 to "add" has incompatible type "str"; expected "int"
example01.py:4: error: Argument 2 to "add" has incompatible type "str"; expected "int"

Define o type hints, annotation

Análise estática das anotações de tipo

Checador de tipo estático experiência





PEP 576

PEP 484

PEP 257


from collections import namedtuple


nt = namedtuple('User', 'nome idade')

nt(1, 1)

# 3.6 e 3.7


from typing import NamedTuple # 3.6 é lento
# 3.7 ficou mais rapido


class User(NamedTuple):
    nome: str
    idade: int

User(1, 1)


l: list = [1, 2, 3]

from typing import List


l: List[str] = [1, 2, 3]

from typing import Dict

d: Dict[str, int] = {'Eduardo': 7, True: 'str'}

from typing import Tuple

t: Tuple[int, str, int, List[int]] = (0, '1', 0, ['2'])

from typing import Sequence, Set

s_l: Sequence = [1, 2, 3]
s_t: Sequence = (1, 2, 3)
s_s: Sequence = {1, 2, 3}
s_s: Set[int] = {1, 2, 3}

from typing import Text

tx: Text = 'abcd'

from typing import Callable, Union

def xpto(func: Callable, n: Union[int, float, complex]) -> Dict[str, int]:
    return {'Eduardo': 7, 'True': 0}

xpto(lambda x: x, 1.0 + 10j)
