"""
A dummy generator that always output ["dummy"]
This is helpful for testing for the factory
"""

from collections import Counter
from typing import Set
from unique_name_generator.interfaces.generator import Generator
from unique_name_generator.interfaces.constraints import Constraints


class Dummy(Generator):
    def generator_tags(self) -> Set[str]:
        return {"memoryless", "unordered"}

    def unordered_output(self, input_tags: Set[str], contraints: Constraints)\
            -> Counter[str]:
        return Counter({'dummy': 1})
