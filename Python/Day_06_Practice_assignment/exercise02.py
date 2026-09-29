class Vehicle:
    def __init__(self, make, model, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_capacity = float(fuel_capacity)

    def calculate_range(self, fuel_efficiency):
        """Calculate range (km) = fuel_capacity * fuel_efficiency."""
        return self.fuel_capacity * float(fuel_efficiency)

    def get_description(self):
        return f"Vehicle: {self.make} {self.model}"


class DeliveryTruck(Vehicle):
    def __init__(self, make, model, fuel_capacity, cargo_load):
        super().__init__(make, model, fuel_capacity)
        self.cargo_load = float(cargo_load)

    def calculate_range(self, fuel_efficiency):
        """Adjusted range reduces efficiency by 10% per metric ton of cargo_load."""
        base_range = super().calculate_range(fuel_efficiency)
        adjusted_range = base_range * (1.0 - 0.1 * self.cargo_load)
        return adjusted_range

    def get_description(self):
        return f"Truck: {self.make} {self.model} carrying {self.cargo_load} tons"


# Example Walkthrough
if __name__ == "__main__":
    truck = DeliveryTruck("Volvo", "FH16", 300.0, cargo_load=2.0)

    # Base range calculations without load adjustment would be 300 * 5 = 1500 km.
    # 2.0 tons load reduces range by 20% (10% * 2) -> 1500 * 0.8 = 1200 km.
    print(truck.calculate_range(5.0))  # Output: 1200.0
    print(truck.get_description())     # Output: Truck: Volvo FH16 carrying 2.0 tons
