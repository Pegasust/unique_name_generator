#!/usr/bin/env python3
"""
Generates using a memory-less interpreter and outputs 
unordered strings
"""

import unique_name_generator.interfaces.generator as generator
from typing import Set

from unique_name_generator.interfaces.constraints import Constraints
from collections import Counter


class Linear(generator.Generator):
    def generator_tags(self) -> Set[str]:
        return {"linear", "memoryless", "unordered"}

    # def unordered_output(self, input_tags: Set[str], constraints: Constraints)\
    #         -> Counter[str]:
    #     return None
    