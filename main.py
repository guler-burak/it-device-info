import wmi

def get_pc_brand_model():
    c = wmi.WMI()
    cs = c.Win32_ComputerSystem()[0]
    return cs.Manufacturer, cs.Model

def get_serial_number():
    c = wmi.WMI()
    bios = c.Win32_BIOS()[0]
    return bios.SerialNumber

if __name__ == "__main__":
    print("Welcome to the Device Info App\n")
    print("1 - Show Device Brand and Model")
    print("2 - Show Device Serial Number\n")

    choice = input("Press 1 or 2 to continue: ")

    if choice == "1":
        brand, model = get_pc_brand_model()
        print("\nBrand:", brand)
        print("Model:", model)

    elif choice == "2":
        serial = get_serial_number()
        print("\nSerial Number:", serial)

    else:
        print("\nInvalid choice")

    input("\nPress Enter to exit...")
