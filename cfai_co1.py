from dataclasses import dataclass

@dataclass
class Sector:
    name: str
    demand: int
    priority: int

class SmartGridAgent:

    def decide(self, sector):

        if sector.demand > 50:
            return "High Load"

        return "Normal Load"

sector = Sector(
    "Hospital",
    80,
    5
)

agent = SmartGridAgent()

print("Sector:", sector.name)
print("Demand:", sector.demand)
print("Priority:", sector.priority)
print("Decision:", agent.decide(sector))