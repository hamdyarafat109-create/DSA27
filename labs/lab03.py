"""Lab 03 — Data structures, classes and generators.

Lab manual: docs/labs/lab03-data-structures-classes.md
Tests:      tests/test_lab03.py

    pytest tests/test_lab03.py -v

This lab is the bridge into the course proper. From Week 4 on, every data
structure you build is a class like `Bag` below: some private state, a small
set of methods, and a contract written in the docstring.
"""

# -- lists, sets, dictionaries ----------------------------------------------


def unique_in_order(values):
    """The values with duplicates removed, keeping the FIRST occurrence of each.

    unique_in_order([3, 1, 3, 2, 1])  -> [3, 1, 2]
    unique_in_order("banana")         -> ["b", "a", "n"]

    Must be O(n): keep a set of what you have already seen.
    """
    seen = set()
    result = []
    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result


def word_frequencies(text):
    """Count how often each word appears.

    Words are separated by whitespace, compared in lower case, and have any
    of the characters  . , ; : ! ?  removed from both ends.
    Words that become empty after stripping are ignored.

    word_frequencies("The cat. the HAT!")  -> {"the": 2, "cat": 1, "hat": 1}
    word_frequencies("")                   -> {}
    """
    counts = {}
    for raw_word in text.split():
        word = raw_word.strip(".,;:!?").lower()
        if word:
            counts[word] = counts.get(word, 0) + 1
    return counts


def top_k(frequencies, k):
    """The k most frequent words, as a list of (word, count) tuples.

    Highest count first; ties broken alphabetically by word.
    If there are fewer than k words, return them all.

    top_k({"b": 2, "a": 2, "c": 5}, 2)  -> [("c", 5), ("a", 2)]

    Hint: `sorted` with a `key` that returns a tuple.
    """
    if k <= 0:
        return []
    return sorted(frequencies.items(), key=lambda pair: (-pair[1], pair[0]))[:k]


def transpose(matrix):
    """Swap rows and columns of a rectangular list of lists.

    transpose([[1, 2, 3],
               [4, 5, 6]])   -> [[1, 4], [2, 5], [3, 6]]
    transpose([])            -> []

    Write it as a nested list comprehension.
    """
    if not matrix:
        return []
    return [[row[column] for row in matrix] for column in range(len(matrix[0]))]


def invert(mapping):
    """Swap keys and values. Several keys may share a value, so collect them.

    Each list of keys is sorted.

    invert({"a": 1, "b": 2, "c": 1})  -> {1: ["a", "c"], 2: ["b"]}
    """
    result = {}
    for key, value in mapping.items():
        result.setdefault(value, []).append(key)
    for keys in result.values():
        keys.sort()
    return result


def common_elements(first, second):
    """The distinct elements that appear in both sequences, sorted.

    common_elements([3, 1, 2, 3], [3, 4, 1])  -> [1, 3]
    """
    return sorted(set(first) & set(second))


def group_by_length(words):
    """A dict from word length to the words of that length, in input order.

    group_by_length(["hi", "sun", "to", "sky"])
        -> {2: ["hi", "to"], 3: ["sun", "sky"]}
    """
    groups = {}
    for word in words:
        groups.setdefault(len(word), []).append(word)
    return groups


# -- a class: the Bag ADT ---------------------------------------------------


class Bag:
    """A bag (multiset): like a set, but it remembers how many of each item.

    b = Bag(["a", "b", "a"])
    len(b)          -> 3          total items, counting repeats
    b.count("a")    -> 2
    b.count("z")    -> 0
    "b" in b        -> True
    b.add("z")
    b.remove("a")   # removes ONE "a"
    b.distinct()    -> 3          number of different items
    sorted(b)       -> ["a", "b", "z"]    iterating yields each item
                                           as many times as it occurs
    Bag("aab") == Bag("aba")  -> True
    repr(Bag())     -> "Bag([])"

    Store the counts in a dict inside the object. Every method except
    iteration, `==` and `repr` must be O(1).
    """

    def __init__(self, items=()):
        self._counts = {}
        self._total = 0
        for item in items:
            self.add(item)

    def add(self, item):
        """Put one more `item` in the bag."""
        self._counts[item] = self._counts.get(item, 0) + 1
        self._total += 1

    def remove(self, item):
        """Take one `item` out. Raise KeyError if there is none."""
        if item not in self._counts:
            raise KeyError(item)
        self._counts[item] -= 1
        self._total -= 1
        if self._counts[item] == 0:
            del self._counts[item]

    def count(self, item):
        """How many of `item` are in the bag (0 if none)."""
        return self._counts.get(item, 0)

    def distinct(self):
        """How many different items are in the bag."""
        return len(self._counts)

    def __len__(self):
        return self._total

    def __contains__(self, item):
        return item in self._counts

    def __iter__(self):
        for item, count in self._counts.items():
            for _ in range(count):
                yield item

    def __eq__(self, other):
        if not isinstance(other, Bag):
            return NotImplemented
        return self._counts == other._counts

    def __repr__(self):
        """ "Bag([...])" listing every item, repeats included, in sorted order."""
        return f"Bag({sorted(self)!r})"


# -- generators -------------------------------------------------------------


def countdown(n):
    """Yield n, n-1, ..., 1. Nothing at all if n < 1.

    list(countdown(3)) -> [3, 2, 1]

    This must be a generator: use `yield`, not a list.
    """
    for value in range(n, 0, -1):
        yield value


def chunks(values, size):
    """Yield consecutive slices of `values`, each of length `size`.

    The last chunk may be shorter. Raise ValueError if size < 1.

    list(chunks([1, 2, 3, 4, 5], 2)) -> [[1, 2], [3, 4], [5]]
    """
    if size < 1:
        raise ValueError("size must be at least 1")
    for start in range(0, len(values), size):
        yield values[start:start + size]
