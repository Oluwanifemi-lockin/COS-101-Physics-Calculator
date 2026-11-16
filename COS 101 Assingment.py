def physics_calculator():
    while True:
        print("\n" + "=" * 35)
        print("     PHYSICS FORMULA SOLVER")
        print("=" * 35)
        print("1. Momentum (p = m * v)")
        print("2. Work Done (W = F * d)")
        print("3. Power (P = W / t)")
        print("4. Wave Speed (v = f * λ)")
        print("5. Pressure (P = F / A)")
        print("=" * 35)

        choice = input("Enter your choice (1-5): ").strip()

        try:
            if choice == "1":
                m = float(input("Enter mass (m) in kg: "))
                v = float(input("Enter velocity (v) in m/s: "))
                p = m * v
                print(f"--> Momentum (p) = {p:.2f} kg·m/s")

            elif choice == "2":
                F = float(input("Enter applied force (F) in N: "))
                d = float(input("Enter distance (d) in m: "))
                W = F * d
                print(f"--> Work Done (W) = {W:.2f} J")

            elif choice == "3":
                W = float(input("Enter work done (W) in J: "))
                t = float(input("Enter time taken (t) in s: "))
                if t == 0:
                    print("Error: Time cannot be zero.")
                else:
                    P = W / t
                    print(f"--> Power (P) = {P:.2f} W")

            elif choice == "4":
                f = float(input("Enter frequency (f) in Hz: "))
                wavelength = float(input("Enter wavelength (λ) in m: "))
                v = f * wavelength
                print(f"--> Wave Speed (v) = {v:.2f} m/s")

            elif choice == "5":
                F = float(input("Enter perpendicular force (F) in N: "))
                A = float(input("Enter surface area (A) in m²: "))
                if A == 0:
                    print("Error: Surface area cannot be zero.")
                else:
                    P = F / A
                    print(f"--> Pressure (P) = {P:.2f} Pa")

            else:
                print("Invalid choice! Please select a number between 1 and 5.")

        except ValueError:
            print("Invalid input! Please enter numeric values only.")

        # Ask the user if they want to continue
        while True:
            again = (
                input("\nDo you want to continue? (yes/no): ").strip().lower()
            )
            if again in ["yes", "y"]:
                break  # Breaks the inner loop and restarts the main calculator
            elif again in ["no", "n"]:
                print("Exiting calculator. Goodbye!")
                return  # Exits the function completely
            else:
                print("Please type 'yes' or 'no'.")


# Run the program
if __name__ == "__main__":
    physics_calculator()