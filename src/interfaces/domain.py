
from dataclasses import dataclass
from typing import Any, List, Set, Dict


@dataclass
class Symbol:
    name: str
    keywords: List[str]


@dataclass
class Domain:
    """
    Stores the data used by the generator
    """
    data_tag: List[Any]
    symbols: List[Symbol]

    m_tag_dict: None=None

    def tag_dict(self)->Dict[str, Set[Symbol]]:
        """
        Returns the mapping from tag to the symbols
        """
        if self.m_tag_dict is None:
            tagd: Dict[str, Set[Symbol]]
            tagd = dict()
            for sym in self.symbols:
                for kw in sym.keywords:
                    if kw not in tagd:
                        tagd[kw] = set()
                    tagd[kw].add(sym)
            self.m_tag_dict = tagd
        return self.m_tag_dict    
