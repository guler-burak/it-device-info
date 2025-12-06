import wmi

def get_pc_brand_model():
    """
    This function returns the device's brand and model information.
    """
    c = wmi.WMI()
    system_info = c.Win32_ComputerSystem()[0]

    brand = system_info.Manufacturer
    model = system_info.Model

    print(f"Marka: {brand}")
    print(f"Model: {model}")

get_pc_brand_model()

if __name__ == "__main__":
    print("Welcome to the Device Info App\n")
    print("1 - Show Device Brand and Model\n")

    choice = input("Press 1 to continue: ")

    if choice == "1":
        brand, model = get_pc_brand_model()
        print("\nDevice Brand and Model:\n")
        print(f"Brand : {brand}")
        print(f"Model : {model}")
    else:
        print("\nInvalid choice. Please run the program again.")

    print("\nPress Enter to exit...")
    input()