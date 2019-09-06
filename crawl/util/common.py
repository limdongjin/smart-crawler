from typing import List


def to_texts(_) -> List[str]:
    return list(map(lambda _: _.text, _))
