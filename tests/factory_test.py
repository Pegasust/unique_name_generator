import pytest
from collections import Counter
from unique_name_generator.generators.dummy import Dummy
from unique_name_generator.generators.factory import GeneratorType, generate
from unique_name_generator.interfaces.constraints import Constraints
from unique_name_generator.interfaces.domain import Domain


def test_factory_dummy():
    input_tags = set()
    constraints = Constraints()
    domain = Domain()
    expect = Counter(dummy=1)

    obj: Dummy
    obj = generate(GeneratorType.DUMMY, domain)
    assert(obj.domain() == domain)
    assert(obj.unordered_output(input_tags, constraints) == expect)
    assert(obj.ordered_output(input_tags, constraints) == ["dummy"])
