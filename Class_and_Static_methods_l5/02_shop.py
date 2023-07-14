from typing import Dict, Type, TypeVar

T = TypeVar('T', bound='Shop')


class Shop:
    def __init__(self, name: str, type: str, capacity: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items: Dict[str: int] = {}

    @classmethod
    def small_shop(cls: Type[T], name: str, type: str, capacity=10) -> T:
        return cls(name, type, capacity)

    def add_item(self, item_name: str) -> str:
        if self.capacity > sum(self.items.values()):
            if item_name not in self.items:
                self.items[item_name] = 0
            self.items[item_name] += 1
            return f"{item_name} added to the shop"

        return "Not enough capacity in the shop"

    def remove_item(self, item_name: str, amount: int):
        this_product = [p for p in self.items if item_name == p]
        if this_product:
            exact_product = this_product[0]
            if self.items[exact_product] >= amount:
                self.items[exact_product] -= amount
                if self.items[exact_product] == 0:
                    del self.items[exact_product]
                return f"{amount} {item_name} removed from the shop"

        return f"Cannot remove {amount} {item_name}"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"


fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
small_shop = Shop.small_shop("Fashion Boutique", "Clothes")
print(fresh_shop)
print(small_shop)
print(fresh_shop.add_item("Bananas"))
print(fresh_shop.remove_item("Tomatoes", 2))
print(small_shop.add_item("Jeans"))
print(small_shop.add_item("Jeans"))
print(small_shop.remove_item("Jeans", 2))
print(small_shop.items)