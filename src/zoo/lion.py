
# lion.py

from .animal import Animal


class Lion(Animal):
    def __init__(self, name="Asad"):
        super().__init__(name, species="Lion")

    def sound(self):
        return "roars"

    def action(self):
        return "rules the jungle."