from enum import Enum
from unique_name_generator.interfaces.domain import Domain
from unique_name_generator.interfaces.generator import Generator
from unique_name_generator.generators.linear import Linear
from unique_name_generator.generators.dummy import Dummy


class GeneratorType(Enum):
    LINEAR = Linear
    DUMMY = Dummy


def generate(gen_type: GeneratorType, domain: Domain) -> Generator:
    obj_instance: Generator
    obj_instance = gen_type.value()
    obj_instance.bind(domain)
    return obj_instance
