# MyPy

http://mypy-lang.org/


## Links

https://twitter.com/gvanrossum/status/1095036541179555840

https://www.python.org/dev/peps/pep-0484/

https://www.python.org/dev/peps/pep-0526/


## Exemplos

Exemplo com retorno de string.

```
# example01.py
def add(a: int, b: int) -> int:
    return 'a + b'
```

Rodando o mypy

```
$ mypy example01.py 
example01.py:2: error: Incompatible return value type (got "str", expected "int")
```

Exemplo com string nos parâmetros de entrada.

```
# example02.py
def add(a: int, b: int) -> int:
    return a + b

print(add('40', '2'))
```

Rodando o mypy

```
$ mypy example01.py 
example01.py:4: error: Argument 1 to "add" has incompatible type "str"; expected "int"
example01.py:4: error: Argument 2 to "add" has incompatible type "str"; expected "int"
```

Corrigindo o código:

```
def add(a: int, b: int) -> int:
    return a + b

print(add(40, 2))
```

## Descrição

O mypy ajuda a definir o 'type hints', são anotações.

type hints: Análise estática das anotações de tipo

O mypy é uma experiência de checador de tipo estático.


[PEP 484](https://www.python.org/dev/peps/pep-0484/) type hints

[PEP 257](https://www.python.org/dev/peps/pep-0257/) docstring


## Mais exemplos

```
example03.py
a: int = 10 # type hint

# example03.py:1: error: Variable annotation syntax is only supported in
# Python 3.6 and greater

# py 3.7
```

```
example04.py
from typing import List


def fib(a: int) -> List[int]:
    return (1, 1, 2, 3)  # mude para [1, 1, 2, 3]
```

```
$ mypy example04.py 
example04.py:5: error: Incompatible return value type (got "Tuple[int, int, int, int]", expected "List[int]")
```

```
# example05.py
from typing import Dict


def weekday(day: int) -> Dict[str, str]:
    if day == 1:
        return {'day': 'sunday'}
    else:
        return  # mude para return {}
```

```
$ mypy example05.py
example05.py:8: error: Return value expected
```


```
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
```
