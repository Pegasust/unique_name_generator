"""
A simple framework for a name generator
"""
from typing import List, Set, Any, Dict
from collections import Counter
from .constraints import Constraints
from dataclasses import dataclass
from .unordered_to_ordered import to_ordered
from .domain import Domain, Symbol

    
@dataclass
class Generator:
    """
    An interface for implementing a Generator
    Generator implementors should only be concerned to overwrite
    `generator_tags(self)`, `ordered_output(...)`, `unordered_output(...)`
    """
    domain_: Domain = None
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
        try:
            return to_ordered(self.unordered_output(input_tags, constraints))
        except NotImplementedError as ex:
            raise NotImplementedError(f"ordered_output not supported by generator {self.name()}") from ex
        except Exception as ex:
            raise ex

    def unordered_output(self, input_tags: Set[str], constraints: Constraints)->Counter[str]:
        raise NotImplementedError(f"unordered_output not supported by generator {self.name()}")

    def domain(self)->Domain:
        if self.domain_ is None:
            raise AttributeError(f"{self.name()}: Domain not binded")
        return self.domain_

    def bind(self, domain: Domain):
        self.domain_ = domain