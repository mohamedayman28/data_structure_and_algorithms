""" Efficiency cheat-sheet for Python dictionary data structure.
More details at https://wiki.python.org/moin/TimeComplexity."""

"""
Summary:
    * Since dictionary is built on the Hash Table concept that provides quick
    set(update value) and get(retrieve value) the efficiency of most operations will
    be in O(1).
    * But in rare cases(and depending on you usage) it may happen to be O(n) exception
    for some.
    * Iterating over a dictionary is O(n), as is copying the dictionary, since
    n(key/value) pairs must be copied.

# O(1)
    - .get(key)
    - .update({key, value})
    - .pop(key) returns value.
    - .popitem() ==> remove last key:value pair.
    - delete key:value pair (e.g. del dic[key])
    - key in dic (e.g. 'a' in {'a': 1, 'b': 2})
# O(n)
    - .copy()
    - iteration (e.g. for i in dic)
"""

# .clear(): Removes all the elements from the dictionary
dic = d = {'a': 10, 'b': 20, 'c': 30}
dic.clear()
assert len(dic) == 0

# ========
# ========


# .get(key): Returns the value for a key if it exists in the dictionary, O(n).
dic = d = {'a': 10, 'b': 20, 'c': 30}
assert dic.get('b') == 20
# Set default value to return, if get(key) not in the dictionary.
dic.get('height', "Default msg: Value doesn't exist")

# ========
# ========

# NOTE: More information about the view object in the important_notes.txt.

# All the three methods return a view object of the dictionary.
dic = d = {'a': 10, 'b': 20, 'c': 30}
dic.items()  # returns dict_items([(2, 'a'), (3, 'b')])

dic = {'a': 10, 'b': 20, 'c': 30}
dic.keys()  # returns dict_keys([2, 3])

dic = {'a': 10, 'b': 20, 'c': 30}
dic.values()  # returns dict_values(['a', 'b'])

# ========
# ========

# .copy(): Returns a copy of the dictionary, O(n).
dic = d = {'a': 10, 'b': 20, 'c': 30}
assert dic.copy().get('b') == 20

# ========
# ========

# .pop(key): Removes a key(and related value) from a dictionary, and returns its
# value.
dic = {'a': 10, 'b': 20, 'c': 30}
assert dic.pop('a') == 10
assert dic == {'b': 20, 'c': 30}
# NOTE: .pop(key) raises a KeyError exception if key is not in dictionary.
try:
    dic.pop('z')
except KeyError:
    "Key doesn't exist"

# ========
# ========

# .popitem(): Removes the last key-value pair added from d and returns it as a Python tuple.
dic = {'a': 10, 'b': 20, 'c': 30}
assert dic.popitem() == ('c', 30)
assert dic == {'a': 10, 'b': 20}
assert type(dic.popitem()) is tuple
# NOTE: .popitem() raises a KeyError exception if dictionary is empty.
try:
    dic.clear()
    dic.popitem()
except KeyError:
    'dictionary is empty'

# ========
# ========

# .update(dict): Creates union between two dictionaries.
dic_1 = {'a': 10, 'b': 20, 'c': 30}
# NOTE: b and c are duplicated keys, thus its values will be updated.
dic_2 = {'b': 'zx', 'd': 400, 'c': 'QW'}
dic_1.update(dic_2)

assert dic_1 == {'a': 10, 'b': 'zx', 'c': 'QW', 'd': 400}
# WE can use a sequence of key-value pairs, similar to when the dict() function
# is used to define a dictionary.
dic_1 = {'a': 10, 'b': 20, 'c': 30}
dic_1.update([('z', 'ZX'), ('c', 'QW')])
assert dic_1 == {'a': 10, 'b': 20, 'c': 'QW', 'z': 'ZX'}

# Or the values to merge can be specified as a list of keyword arguments.
d1 = {'a': 10, 'b': 20, 'c': 30}
d1.update(b='updated', d=400)
assert d1 == {'a': 10, 'b': 'updated', 'c': 30, 'd': 400}
