# Objetos Pythônicos

[Apresentação][0] do [Luciano Ramalho][1] no [Garoa Hacker Club][2] dia 11/05/16.


### Tamanho com `len()`

```bash
len(s), len(L)
s.__len__(), L.__len__()
```

### Aritmética

```bash
a = 2
b = 3
a * b, a.__mul__(b)
```

```bash
L = [10, 20, 30]
for i in L:
    print(i, end=' ')
```

### Rodando um doctest

Veja o exemplo [vector0.py][3].

```bash
$ python -m doctest vector0.py -v
$ python -m doctest vector0.py -o FAIL_FAST
```

[0]: https://speakerdeck.com/ramalho/objetos-pythonicos-1
[1]: https://github.com/ramalho
[2]: https://garoa.net.br/wiki/P%C3%A1gina_principal
[3]: https://github.com/fluentpython/pythonic-api/blob/master/examples/vector0.py