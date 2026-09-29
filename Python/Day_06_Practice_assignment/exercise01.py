class SmartThermostat:
    # 1. Class-level Constant Variables
    MIN_TEMP = 10.0
    MAX_TEMP = 35.0

    # 2. Constructor (__init__)
    def __init__(self, appliance_name, initial_temp):
        self.__appliance_name = appliance_name
        
        # Check initial_temp bounds; default to 22.0 if out of range
        if self.MIN_TEMP <= initial_temp <= self.MAX_TEMP:
            self.__target_temp = float(initial_temp)
        else:
            self.__target_temp = 22.0

    # 3. Properties
    @property
    def target_temp(self):
        """Getter for target_temp."""
        return self.__target_temp

    @target_temp.setter
    def target_temp(self, value):
        """Setter for target_temp with range validation."""
        if self.MIN_TEMP <= value <= self.MAX_TEMP:
            self.__target_temp = float(value)
        else:
            raise ValueError(f"Temperature must be between {self.MIN_TEMP} and {self.MAX_TEMP} degrees.")

    @property
    def appliance_name(self):
        """Read-only getter for appliance_name."""
        return self.__appliance_name


# Example Walkthrough
if __name__ == "__main__":
    thermostat = SmartThermostat("Living Room AC", 24.0)
    print(thermostat.appliance_name)  # Output: Living Room AC
    print(thermostat.target_temp)     # Output: 24.0

    thermostat.target_temp = 28.0     # Updates successfully
    print(thermostat.target_temp)     # Output: 28.0

    try:
        thermostat.target_temp = 5.0  # Out of range!
    except ValueError as e:
        print(e)  # Output: Temperature must be between 10.0 and 35.0 degrees.
