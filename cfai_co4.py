from dataclasses import dataclass

@dataclass
class Sector:
    name: str
    demand: int
    priority: int

def utility(sector):

    return (
        sector.priority *
        sector.demand
    )

n = int(input("Number of Sectors: "))

for i in range(n):

    name = input("Name: ")
    demand = int(input("Demand: "))
    priority = int(input("Priority: "))

    sector = Sector(
        name,
        demand,
        priority
    )

    print(
        "Utility =",
        utility(sector)
    )