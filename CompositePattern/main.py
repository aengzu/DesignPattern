from base import Composite, Leaf

compost1 = Composite("1")
compost1.add(Leaf())
compost1.add(Leaf())

compost0 = Composite("0")
compost0.add(Leaf())
compost0.add(compost1)

compost0.fn()