#!/usr/bin/env python3
"""
Generates using a memory-less interpreter and outputs 
unordered strings
"""

import interfaces.generator as generator
from typing import Set

class Linear(generator.Generator):
    def generator_tags(self)->Set[str]:
        return {"linear", "memoryless", "unordered"}
    