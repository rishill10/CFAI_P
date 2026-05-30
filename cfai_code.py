from dataclasses import dataclass

# ==========================================
# SMART GRID LOAD DECISION AGENT
# ==========================================

@dataclass
class Sector:
    name: str
    demand: int
    priority: int
    allocated: int = 0


class SmartGridAgent:

    def __init__(self, available_power):
        self.available_power = available_power
        self.trace = []

    def allocate_power(self, sectors):

        # Sort by PRIORITY (highest first)
        sectors.sort(
            key=lambda s: s.priority,
            reverse=True
        )

        remaining = self.available_power

        self.trace.append(
            f"Initial Available Power = {remaining} kW"
        )

        for sector in sectors:

            if remaining <= 0:
                sector.allocated = 0
                self.trace.append(
                    f"No power left for {sector.name}"
                )
                continue

            # Constraint:
            # Allocation cannot exceed remaining power

            if sector.demand <= remaining:

                sector.allocated = sector.demand
                remaining -= sector.demand

                self.trace.append(
                    f"{sector.name} allocated "
                    f"{sector.allocated} kW"
                )

            else:

                sector.allocated = remaining

                self.trace.append(
                    f"Constraint Activated for "
                    f"{sector.name}"
                )

                self.trace.append(
                    f"{sector.name} receives only "
                    f"{remaining} kW"
                )

                remaining = 0

        return sectors, remaining


# ==========================================
# INPUT
# ==========================================

print("\n========== SMART GRID LOAD DECISION AGENT ==========\n")

available_power = int(
    input("Enter Available Power (kW): ")
)

n = int(
    input("Enter Number of Sectors: ")
)

sectors = []

for i in range(n):

    print(f"\nSector {i+1}")

    name = input("Name: ")
    demand = int(input("Power Demand (kW): "))
    priority = int(
        input("Priority (1-5): ")
    )

    sectors.append(
        Sector(name, demand, priority)
    )

# ==========================================
# AGENT DECISION
# ==========================================

agent = SmartGridAgent(available_power)

result, remaining = agent.allocate_power(sectors)

# ==========================================
# OUTPUT
# ==========================================

print("\n========== FINAL ALLOCATION ==========\n")

for sector in result:

    print(
        f"{sector.name:15}"
        f" Demand={sector.demand:5}"
        f"  Allocated={sector.allocated:5}"
    )

print("\nRemaining Power =", remaining, "kW")

# ==========================================
# TRACE LOG
# ==========================================

print("\n========== REASONING TRACE ==========\n")

for step_no, step in enumerate(agent.trace, start=1):
    print(f"{step_no}. {step}")

print("\nLoad Balancing Completed Successfully.")