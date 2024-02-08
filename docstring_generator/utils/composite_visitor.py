from __future__ import annotations

from abc import ABC, abstractmethod

from visitor import Visitor


class Component(ABC):
    def __init__(self, name: str) -> None:
        super().__init__()
        self._name = name

    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        pass

    @property
    def name(self) -> Component:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        self._parent = parent

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_composite(self) -> bool:
        return False

    @abstractmethod
    def operation(self) -> str:
        pass


class File(Component):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def operation(self) -> str:
        return self.name

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_File(self)


class Folder(Component):
    def __init__(self, name: str, children: list[Component] = []) -> None:
        super().__init__(name=name)
        self._children: list[Component] = children

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        results = []
        for child in self._children:
            results.append(child.operation())
        return f"{self.name}: ({'+'.join(results)})"

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_Folder(self)
        for child in self._children:
            child.accept(visitor)


def main():
    children: list[Component] = [
        Folder(
            name='utils', children=[File(name='classes.py'), File(name='functions.py')]
        ),
        File(name='__main__.py'),
        File(name='config.py'),
        File(name='helpers.py'),
        File(name='templates.py'),
    ]
    root_folder: Folder = Folder(name='docstring_generator', children=children)
    visitor: Visitor = Visitor()
    root_folder.accept(visitor)


if __name__ == '__main__':
    main()
