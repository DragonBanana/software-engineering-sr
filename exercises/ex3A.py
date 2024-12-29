from typing import List
from functools import reduce

class Element:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def get_name(self):
        return self.name

    def get_size(self):
        return self.size


class Group:
    def __init__(self, members: List[Element]):
        self.members = members

    def get_members(self):
        return self.members


def print_type(group: Group):
    members = group.get_members()
    if members:
        average_size = reduce(lambda acc, el: acc + el.get_size(), members, 0) / len(members)
        print(average_size)


def names_in_groups(groups: List[Group]) -> List[str]:
    return list(
        map(
            lambda el: el.get_name(),
            filter(
                lambda el: el.get_size() > 10,
                reduce(
                    lambda acc, group: acc + group.get_members(),
                    groups,
                    [],
                ),
            ),
        )
    )


# Example Usage
if __name__ == "__main__":
    # Create sample data
    e1 = Element("Element1", 15)
    e2 = Element("Element2", 5)
    e3 = Element("Element3", 25)
    g1 = Group([e1, e2])
    g2 = Group([e3])

    print("Average size of Group 1:")
    print_type(g1)  # Should print: 10.0

    print("\nNames of elements with size > 10:")
    print(names_in_groups([g1, g2]))  # Should print: ['Element1', 'Element3']
