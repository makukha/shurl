import random
import string
from collections.abc import Container


CHARS = string.ascii_lowercase + string.digits


def new_key(
    length: int,
    distinct_from: Container[str] | None = None,
) -> str:
    """
    Generate new key, optionally distinct from other values.
    """
    while True:
        key = ''.join(random.choice(CHARS) for _ in range(length))
        if distinct_from is None or key not in distinct_from:
            break
    return key
