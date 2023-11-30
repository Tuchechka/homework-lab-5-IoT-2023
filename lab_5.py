class Flower:
    def __init__(self, name, height, size, *args):
        self.name = name
        self.height = height
        self.size = size
        self.color = args[0]
        self.price = args[1]
        self.quantity = args[2]
        self.delivery_rate = args[3]


class FlowerShop:
    def __init__(self):
        self.inventory = {}

    def add_flower(self, flower):
        """
        Add new flower in the flower shop
        """
        if isinstance(flower, Flower) is True:
            self.inventory[flower] = {"Name": flower.name, "Price": flower.price}
        else:
            raise TypeError

    def remove_flower(self, flower):
        """
        Remove the flower from the flower shop
        """
        del self.inventory[flower]

    def top_price(self):
        """
        Return top price of the flower shop
        """
        return sorted(self.inventory.values(), key=lambda x: x["Price"], reverse=True)


class Bouquet:
    def __init__(self):
        self.inventory = []

    def add_flower(self, flower):
        """
        Add new flower in the bouqut
        """
        if isinstance(flower, Flower) is True:
            self.inventory.append(flower)
        else:
            raise TypeError

    def count_price(self):
        """
        Returns the cost of the bouquet
        """
        result = 0
        for flower in self.inventory:
            result += flower.price * flower.quantity
        return result


def main():
    """
    Creating flowers and calling methods
    """
    rose = Flower("Роза", 35, "Small", "Red", 322, 1, 0.1)
    orchid = Flower("Орхідея", 45, "Big", "White", 140, 51, 0.5)
    basil = Flower("Базилік", 38, "Medium", "Green", 250, 101, 0.7)

    first_shop = FlowerShop()
    first_shop.add_flower(rose)
    first_shop.add_flower(orchid)
    first_shop.add_flower(basil)
    first_shop.remove_flower(rose)
    print(first_shop.top_price())

    bouquet = Bouquet()
    bouquet.add_flower(orchid)
    bouquet.add_flower(basil)
    print(bouquet.count_price())


main()
