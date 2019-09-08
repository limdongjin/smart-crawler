from typing import List


def to_texts(_) -> List[str]:
    return list(map(lambda _: _.text, _))


def to_strings(its) -> List[str]:
    return list(map(lambda it: str(it), its))


def is_str(_):
    return type(_) is str


def is_not_none(_):
    return _ is not None


def to_strips(its) -> map:
    return list(map(lambda it: it.strip(), filter(is_str, its)))


def merge_dict(a: dict, b: dict) -> dict:
    return dict(a, **b)


def is_not_equal_empty_list(_):
    return _ != []


def merge_list_dict(l1: List[dict], l2: List[dict]) -> List[dict]:
    return list(map(merge_dict, l1, l2))


def is_all_elements_type(its, target_type):
    return all(isinstance(it, target_type) for it in its)


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]