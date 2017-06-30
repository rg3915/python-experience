def dedupe(items, key=None):
    ''' Returns only one item each depending on column. '''
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


itens = [
    ('1', 'foo', 'zaz'),
    ('2', 'foo', 'zaz'),
    ('3', 'bar', 'foo'),
]

res = list(dedupe(itens, key=lambda d: (d[1], d[2])))
print(res)

itens = [
    ('foo', 'zaz'),
    ('foo', 'zaz'),
    ('bar', 'foo'),
    ('bar', 'foo'),
    ('zaz', 'foo'),
]

res = list(dedupe(itens, key=lambda d: d[0]))
print(res)
