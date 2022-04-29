import collections

from numpy import mat
def quick_ratio(s1: str, s2: str) -> float:
    """Return an upper bound on ratio() relatively quickly."""
    length = len(s1) + len(s2)

    if not length:
        return 1.0

    intersect = collections.Counter(s1) & collections.Counter(s2)
    print(intersect)
    matches = sum(intersect.values())
    print(matches)
    return 2.0 * matches / length




from difflib import SequenceMatcher

def similar(a, b):
    a = a.lower()
    b = b.lower()
    return SequenceMatcher(None, a, b).ratio()


print(quick_ratio("King’s College", "Kings College"))
# print(similar("King’s College London", "Kings College"))

{'g': 2, 'l': 2, 'e': 2, 'K': 1, 'i': 1, 'n': 1, 's': 1, ' ': 1, 'C': 1, 'o': 1}