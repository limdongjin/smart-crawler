from typing import List, Iterable
from functools import reduce


def flatten(its: Iterable):
    if not its:
        return []

    return reduce(lambda it, _next: it + _next, its)


def to_texts(its: Iterable) -> Iterable[str]:
    return list(map(lambda it: it.text, its))


def to_strings(its: Iterable) -> Iterable[str]:
    return list(map(lambda it: str(it), its))


def is_str(_):
    return type(_) is str


def is_not_none(_):
    return _ is not None


def to_strips(its: Iterable) -> List:
    return list(map(lambda it: it.strip(), filter(is_str, its)))


def merge_dict(a: dict, b: dict) -> dict:
    return dict(a, **b)


def is_not_equal_empty_list(_):
    return _ != []


def merge_list_dict(l1: List[dict], l2: List[dict]) -> List[dict]:
    return list(map(merge_dict, l1, l2))


def is_all_elements_type(its: Iterable, target_type):
    return all(isinstance(it, target_type) for it in its)
