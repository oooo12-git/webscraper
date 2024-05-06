class Puppy:

    def __init__(self, name):
        self.name = name
        self.age = 0.1
        self.breed = "Beagle"


ruffus = Puppy("Ruffus")
bibi = Puppy("Bibi")

print(
    ruffus.name,
    bibi.name,
)
