""" Script is about:
Efficiency cheat-sheet for Python list data structure. More details at
https://wiki.python.org/moin/TimeComplexity."""

"""
Summary
# O(1)
    - .append('man')
    - .index('car')
    - .pop()
    - list[4]
# O(n)
    - .pop('car')
    - .insert(3, 'car')
    - .reverse()
    - del operator (e.g. del list[2])
    - contains (e.g. 'man' in list)
    - iteration (e.g. for e in list)
NOTE: K means, depending on the other elements size.
# O(k)
    - slice (e.g. list[:number])
    - NOTE: getting the slice is O(k) deleting that slice is O(n)
    - concatenate (e.g. list + list_2)
# O(n log n)
    - .sort()
# O(nk)
    - list * list_2
"""

# .append('value'): Add element to the tail, O(1).
el = ['car', 'hat', 'man']
el.append('key')  # return ==> ['car', 'hat', 'man', 'key']
assert len(el) == 4

# .pop(): Remove tail element, O(1).
el = ['car', 'hat', 'man']
el.pop()  # return ==> ['car', 'hat']
assert len(el) == 2

# .index('value'): Returns the index of the first element(repeated or not),
# O(1).
el = ['car', 'ZZ', 'man', 'ZZ']
index = el.index('ZZ')  # return ==> 0
assert index == 1

# .pop(index): Remove element by index, O(n).
el = ['car', 'hat', 'man']
el.pop(0)  # return ==> ['hat', 'man']
assert len(el) == 2

# .remove('value'): Remove element by value, O(n).
el = ['car', 'hat', 'man']
el.remove('car')  # return ==> ['hat', 'man']
assert len(el) == 2

# .insert('value'): Insert at index, O(n).
el = ['car', 'hat', 'man']
el.insert(1, 'woman')  # return ==> ['car', 'woman', 'hat', 'man']
assert len(el) == 4

# .extend(list, set, tuple, iterator): Add collection of elements to the end of
# the list, O(k), K means depending on the size of the iterator size.
el = ['car', 'hat', 'man']
el_2 = ['c', 'h', 'm']
el.extend(el_2)  # return ==> ['car', 'hat', 'man', 'c', 'h', 'm']
assert len(el) == 6


# list.copy(): Returns a copy of the specified list, O(n).
el = ['car', 'hat', 'man']
el_2 = el.copy()
assert el == el_2
# It is a shallow copy
assert id(el) != id(el_2)

# list.sort(): O(n log n).
el = ['car', 'sat', 'hat', 'man']
el.sort()

# list.count():  Returns the number of elements with the specified value, O(n).
el = ['car', 'ZZ', 'man', 'ZZ']
count = el.count('ZZ')  # return ==> 0
assert count == 2

# list.reverse():  O(n).
el = ['car', 'man', 'ZZ']
el.reverse()
assert el == ['ZZ', 'man', 'car']

len(el)  # O(1)
max(el)  # O(n)
min(el)  # O(n)
'car' in el  # O(n)

el = ['car', 'man', 'ZZ']
el_2 = [1, 2, 3]
# Here K means depending on the slice size.
el[0: 1]  # O(K)
del el[0: 1]  # O(n)
# Here K means depending on the other list size want to concatenate.
el + el_2  # O(K)
