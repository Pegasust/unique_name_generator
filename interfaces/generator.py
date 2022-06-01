"""
A simple framework for a name generator
"""
from typing import List, Set, Counter
from collections import Counter
from constraints import Constraints


class Generator:
    def name(self)->str:
        """
        Name of the generator
        """
        return self.__class__.__name__
    def generator_tags(self)->Set[str]:
        """
        The tags for this generator
        """
        return set()
    def ordered_output(self, input_tags: Set[str], constraints: Constraints)->List[str]:
        raise NotImplementedError(f"ordered_output not supported by generator {self.name()}")
    def unordered_output(self, input_tags: Set[str], constraints: Constraints)->Counter[str]:
        raise NotImplementedError(f"unordered_output not supported by generator {self.name()}")
