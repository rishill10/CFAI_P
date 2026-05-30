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

def overload_probability(demand):

    return demand / 100

n = int(input("Number of Sectors: "))

sectors = []

for i in range(n):

    print(f"\nSector {i+1}")

    name = input("Name: ")
    demand = int(input("Demand: "))
    priority = int(input("Priority: "))

    sectors.append(
        Sector(
            name,
            demand,
            priority
        )
    )

# Search

sectors.sort(
    key=lambda s: s.priority,
    reverse=True
)

for sector in sectors:

    util = utility(sector)

    prob = overload_probability(
        sector.demand
    )

    if prob > 0.7:

        decision = "High Risk"

    elif util > 150:

        decision = "Allocate First"

    else:

        decision = "Normal Allocation"

    print(
        sector.name,
        "| Utility =", util,
        "| Risk =", round(prob, 2),
        "| Decision =", decision
    )