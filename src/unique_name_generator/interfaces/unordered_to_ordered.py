from collections import Counter
from typing import List
import random

def to_ordered(unordered: Counter[str], randomize=True)->List[str]:
    """
    Adapts unordered output to ordered output
    :param randomize whether to shuffle the output
    :param unordered the unordered output we want to order
    :return ordered output under the form of list of strings
    """
    ordered = list(unordered.elements())
    if randomize:
        random.shuffle(ordered)

    return ordered