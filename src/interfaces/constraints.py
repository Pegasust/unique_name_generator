from dataclasses import dataclass
from typing import List
from collections import Counter
import random

@dataclass
class Constraints:
    min_length: int = 5
    max_length: int = 32
    min_symbols: int = 1
    max_symbols: int = 10

    def satisfies_ordered(self, ordered_output: List[str], join_str: str = "")->bool:
        symbols_count = len(ordered_output)
        output_length = len(join_str.join(ordered_output))
        return self.min_symbols <= symbols_count and symbols_count <= self.max_symbols and\
            self.min_length <= output_length and output_length <= self.max_length
    
    def satisfies_unordered(self, unordered_output: Counter[str], join_str: str = "")->bool:
        ordered_output = unordered_output.elements()
        random.shuffle(ordered_output)
        return self.satisfies_ordered(ordered_output, join_str)


