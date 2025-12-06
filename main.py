import wmi
import psutil
from datetime import datetime

def get_pc_brand_model():
    c = wmi.WMI()
    cs = c.Win32_ComputerSystem()[0]
    return cs.Manufacturer, cs.Model

def get_serial_number():
    c = wmi.WMI()
    bios = c.Win32_BIOS()[0]
    return bios.SerialNumber

def last_reboot():
    t = psutil.boot_time()
    dt = datetime.fromtimestamp(t)
    return dt.strftime("%Y-%m-%d %H:%M:%S")


if __name__ == "__main__":
    print("Welcome to the Device Info App\n")
    print("1 - Show Device Brand and Model")
    print("2 - Show Device Serial Number\n")
    print("3 - Show Last Reboot Time\n")
    

    choice = input("Press 1, 2 or 3 to continue: ")

    if choice == "1":
        brand, model = get_pc_brand_model()
        print("\nBrand:", brand)
        print("Model:", model)

    elif choice == "2":
        serial = get_serial_number()
        print("\nSerial Number:", serial)
    
    elif choice == "3":
        reboot = last_reboot()
        print("\nReboot Time:", reboot)

    else:
        print("\nInvalid choice")

    input("\nPress Enter to exit...")
