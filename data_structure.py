"""data_structure.py

Concise examples of common Python data structures and their typical operations.

Run this file to see short demonstrations and simple assertions that validate
behavior. It's intended as a quick reference for lists, tuples, sets, dicts,
namedtuples/dataclasses, deque, Counter, and defaultdict.
"""

from collections import namedtuple, deque, Counter, defaultdict
from dataclasses import dataclass
from typing import Any, Dict, Iterable, List, Set, Tuple
import sys


def demo_list() -> None:
    """Lists: ordered, mutable, allow duplicates."""
    print("--- list demo ---")
    a: List[int] = [1, 2, 3]
    print("initial:", a)
    a.append(4)
    print("after append:", a)
    a.insert(1, 10)
    print("after insert at index 1:", a)
    assert a[1] == 10
    popped = a.pop()  # 4
    print("popped:", popped, "result:", a)
    a.extend([7, 8])
    print("after extend:", a)


def demo_tuple() -> None:
    """Tuples: ordered, immutable. Good for fixed collections."""
    print("--- tuple demo ---")
    t: Tuple[int, ...] = (1, 2, 3)
    print("tuple:", t)
    try:
        t[0] = 10  # type: ignore
    except TypeError as e:
        print("immutable (TypeError):", e)


def demo_set() -> None:
    """Sets: unordered, unique elements."""
    print("--- set demo ---")
    s: Set[int] = {1, 2, 3}
    s.add(2)  # no effect, 2 already present
    s.add(4)
    print("set contents:", s)
    assert 2 in s
    s.discard(10)  # no error if missing
    print("after discard(10):", s)


def demo_dict() -> None:
    """Dictionaries: key->value mappings."""
    print("--- dict demo ---")
    d: Dict[str, int] = {"a": 1, "b": 2}
    print("initial dict:", d)
    d["c"] = 3
    print("after add:", d)
    val = d.get("z", "not found")
    print('d.get("z", "not found") ->', val)
    keys = list(d.keys())
    values = list(d.values())
    print("keys:", keys, "values:", values)


def demo_namedtuple_and_dataclass() -> None:
    """Show small structured-record alternatives."""
    print("--- namedtuple & dataclass demo ---")
    Point = namedtuple("Point", ["x", "y"])
    p = Point(1, 2)
    print("namedtuple point:", p, "x=", p.x)

    @dataclass(frozen=True)
    class P:
        x: int
        y: int

    p2 = P(3, 4)
    print("dataclass point (frozen):", p2)


def demo_deque_counter_defaultdict() -> None:
    """Other useful collections: deque, Counter, defaultdict."""
    print("--- deque / Counter / defaultdict demo ---")
    dq = deque([1, 2, 3])
    dq.appendleft(0)
    print("deque after appendleft:", dq)
    dq.pop()
    print("deque after pop:", dq)

    words = ["apple", "banana", "apple", "cherry"]
    c = Counter(words)
    print("counter:", c)
    assert c["apple"] == 2

    dd = defaultdict(list)
    dd["a"].append(1)
    dd["b"].extend([2, 3])
    print("defaultdict:", dict(dd))


def demo_mutability_and_copying() -> None:
    """Small notes about copying and references."""
    print("--- mutability & copying demo ---")
    original = [1, 2, 3]
    alias = original
    alias.append(4)
    print("original after alias.append:", original)
    assert original is alias

    shallow = original.copy()
    shallow.append(5)
    print("original after shallow.append:", original)
    print("shallow:", shallow)
    assert shallow is not original


def run_quick_asserts() -> None:
    """Extra programmatic checks that will raise if behavior is unexpected."""
    # list slicing creates a new list
    a = [1, 2, 3]
    b = a[:]
    assert a == b and a is not b

    # tuple immutability
    t = (1, 2)
    try:
        t[0] = 0  # should raise
    except TypeError:
        pass
    else:
        raise AssertionError("tuple should be immutable")


def main() -> None:
    print("Data Structures quick reference\n")
    demo_list()
    demo_tuple()
    demo_set()
    demo_dict()
    demo_namedtuple_and_dataclass()
    demo_deque_counter_defaultdict()
    demo_mutability_and_copying()
    run_quick_asserts()
    print("\nAll demos completed successfully.")


if __name__ == "__main__":
    main()
    sys.exit(0)