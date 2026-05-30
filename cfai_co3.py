from dataclasses import dataclass

@dataclass
class Sector:
    name: str
    demand: int
    allocated: int = 0

available_power = int(
    input("Available Power: ")
)

n = int(
    input("Number of Sectors: ")
)

sectors = []

for i in range(n):

    name = input("Sector Name: ")
    demand = int(
        input("Demand: ")
    )

    sectors.append(
        Sector(name, demand)
    )

remaining = available_power

for sector in sectors:

    if sector.demand <= remaining:

        sector.allocated = sector.demand

        remaining -= sector.demand

    else:

        sector.allocated = remaining

        print(
            "Constraint Failed for",
            sector.name
        )

        remaining = 0

for sector in sectors:

    print(
        sector.name,
        "Allocated:",
        sector.allocated
    )