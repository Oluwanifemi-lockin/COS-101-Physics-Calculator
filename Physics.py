def calculate_speed(distance, time):
    """Calculate speed: Speed = Distance / Time."""
    return distance / time


def calculate_force(mass, acceleration):
    """Calculate force: Force = Mass * Acceleration."""
    return mass * acceleration


def calculate_density(mass, volume):
    """Calculate density: Density = Mass / Volume."""
    return mass / volume


def calculate_weight(mass, gravity=9.8):
    """Calculate weight: Weight = Mass * Gravitational acceleration."""
    return mass * gravity


def calculate_kinetic_energy(mass, velocity):
    """Calculate kinetic energy: KE = 1/2 * Mass * Velocity squared."""
    return 0.5 * mass * velocity ** 2


def main():
    print("===== PHYSICS FORMULAS =====")
    print("1. Speed")
    print("2. Force")
    print("3. Density")
    print("4. Weight")
    print("5. Kinetic Energy")

    choice = input("\nChoose a formula (1-5): ")

    if choice == "1":
        distance = float(input("Enter distance (m): "))
        time = float(input("Enter time (s): "))
        if time <= 0:
            print("Time must be greater than zero.")
        else:
            print("Speed:", calculate_speed(distance, time), "m/s")

    elif choice == "2":
        mass = float(input("Enter mass (kg): "))
        acceleration = float(input("Enter acceleration (m/s²): "))
        print("Force:", calculate_force(mass, acceleration), "N")

    elif choice == "3":
        mass = float(input("Enter mass (kg): "))
        volume = float(input("Enter volume (m³): "))
        if volume <= 0:
            print("Volume must be greater than zero.")
        else:
            print("Density:", calculate_density(mass, volume), "kg/m³")

    elif choice == "4":
        mass = float(input("Enter mass (kg): "))
        print("Weight:", calculate_weight(mass), "N")

    elif choice == "5":
        mass = float(input("Enter mass (kg): "))
        velocity = float(input("Enter velocity (m/s): "))
        print("Kinetic Energy:", calculate_kinetic_energy(mass, velocity), "J")

    else:
        print("Invalid choice. Please choose between 1 and 5.")


if __name__ == "__main__":
    main()
