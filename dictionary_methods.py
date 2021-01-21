""" Efficiency cheat-sheet for Python dictionary data structure.
More details at https://wiki.python.org/moin/TimeComplexity."""

""" Technical Note: The .items(), .keys(), and .values() methods actually return
something called a view object. A dictionary view object is more or less like a
window on the keys and values. For practical purposes, you can think of these
methods as returning lists of the dictionary’s keys and values."""

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


# .get(key): Returns the value for a key if it exists in the dictionary.
dic = d = {'a': 10, 'b': 20, 'c': 30}
assert dic.get('b') == 20
# Set default value to return, if get(key) not in the dictionary.
dic.get('height', "Value doesn't exist")

# .items(): Returns a list of key-value pairs in a dictionary.
dic = d = {'a': 10, 'b': 20, 'c': 30}
dic.items()  # returns dict_items([(2, 'a'), (3, 'b')])

# .keys(): Returns a list of keys in a dictionary.
dic = {'a': 10, 'b': 20, 'c': 30}
dic.keys()  # returns dict_keys([2, 3])

# .values(): Returns a list of values in a dictionary.
dic = {'a': 10, 'b': 20, 'c': 30}
dic.values()  # returns dict_values(['a', 'b'])

# .copy(): Returns a copy of the dictionary.
dic = d = {'a': 10, 'b': 20, 'c': 30}
assert dic.copy().get('b') == 20

# .pop(key): Returns a copy of the dictionary.
dic = {'a': 10, 'b': 20, 'c': 30}
assert dic.pop('a') == 10
# NOTE: .pop(key) raises a KeyError exception if key is not in dictionary
try:
    dic.pop('z')
except KeyError:
    "Key doesn't exist"

# .popitem(key): Removes the last key-value pair added from d and returns it as a tuple.
dic = {'a': 10, 'b': 20, 'c': 30}
assert dic.popitem() == ('c', 30)
# NOTE: .popitem() raises a KeyError exception if dictionary is empty.
try:
    dic.clear()
    dic.popitem()
except KeyError:
    'dictionary is empty'

# .update(dict): Creates union between two dictionaries.
dic_1 = {'a': 10, 'b': 20, 'c': 30}
dic_2 = {'b': 200, 'd': 400}
dic_1.update(dic_2)
# print(dic_1) returns {'a': 10, 'b': 200, 'c': 30, 'd': 400}
