from dataclasses import dataclass

@dataclass
class Sector:
    name: str
    demand: int
    priority: int

sectors = []

n = int(input("Enter Number of Sectors: "))

for i in range(n):

    print(f"\nSector {i+1}")

    name = input("Name: ")
    demand = int(input("Demand: "))
    priority = int(input("Priority: "))

    sectors.append(
        Sector(name, demand, priority)
    )

# Greedy Search

sectors.sort(
    key=lambda s: s.priority,
    reverse=True
)

print("\nGreedy Search Result\n")

for sector in sectors:

    print(
        sector.name,
        sector.priority
    )