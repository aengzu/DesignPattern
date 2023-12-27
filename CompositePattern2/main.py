from base import AnimalGroup, Cat, Dog

cat_group = AnimalGroup()
cat_group.add(Cat())
cat_group.add(Cat())
cat_group.add(Cat())

dog_group = AnimalGroup()
dog_group.add(Dog())
dog_group.add(Dog())

zoo = AnimalGroup()
zoo.add(cat_group)
zoo.add(dog_group)

zoo.speak()