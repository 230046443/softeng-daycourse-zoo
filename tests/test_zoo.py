from zoo.elephant import Elephant
from zoo.kangaroo import Kangaroo
from zoo.lion import Lion


def test_elephant():
    assert Elephant().describe() == "Ellie the Elephant says toots and remembers everything!"


def test_kangaroo():
    assert Kangaroo().describe() == "Roo the Kangaroo says thumps and hops around happily."


def test_lion():
    assert Lion().describe() == "Asad the Lion says roars and rules the jungle."
