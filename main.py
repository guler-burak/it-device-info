import wmi
import psutil
import socket
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

def get_ip_address():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    return hostname, IPAddr

def get_mac_address():
    c = wmi.WMI()
    for interface in c.Win32_NetworkAdapterConfiguration(IPEnabled=1):
        adapter_name = interface.Description
        mac = interface.MACAddress
        return adapter_name, mac


if __name__ == "__main__":
    print("Welcome to the Device Info App\n")
    print("1 - Show Device Brand and Model")
    print("2 - Show Device Serial Number")
    print("3 - Show Last Reboot Time")
    print("4 - Show IP Address\n")

    choice = input("Press 1, 2, 3, 4 or 5 to continue:")

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

    elif choice == "4":
        hostname, ip = get_ip_address()
        print("\nHostname:", hostname)
        print("IP Address:", ip)
    
    elif choice == "5":
        name, mac = get_mac_address()
        print("\nAdapter Name:", name)
        print("MAC Address:", mac)


    else:
        print("\nInvalid choice")

    input("\nPress Enter to exit...")
