import psutil

# Display information for each core
print("CPU Usage per core: ")

# Get the percentage load for each core
cpu_percent = psutil.cpu_percent(interval=1, percpu=True)

# Get information about the frequency for all cores
cpu_freq = psutil.cpu_freq()

# Use a single cpu_freq value for all cores
for i, percent in enumerate(cpu_percent, start=1):
    # Display information about the load and frequency for each core
    print(f"Core {i}: {percent}% Frequency: {cpu_freq.current} MHz")

# Important! Note that cpu_freq.current is the overall frequency for all cores, not for a specific core.

# Virtual Memory and Swap
virtual_mem = psutil.virtual_memory()
swap = psutil.swap_memory()

print("\nVirtual Memory: ")
print(f"Total: {virtual_mem.total / (1024 ** 3):.2f} GB")
print(f"Used {virtual_mem.used / (1024 ** 3):.2f} GB")
print(f"Swap Total: {swap.total / (1024 ** 3):.2f} GB")
print(f"Swap Used: {swap.used / (1024 ** 3):.2f} GB")

# Network Information
network = psutil.net_io_counters()
print("\nNetwork Information: ")
print(f"Bytes received: {network.bytes_recv / (1024 ** 2):.2f} MB")
print(f"Bytes sent: {network.bytes_sent / (1024 ** 2):.2f} MB")

# Temperature Information
try:
    temperatures = psutil.sensors_temperatures()
    if temperatures:
        print("\nTemperatures: ")
        for name, entries in temperatures.items():
            for entry in entries:
                print(f"{name}: {entry.current}°C")
    else:
        print("\nTemperature information unavailable")
except AttributeError:
        print("\nTemperature information unavailable")

# Battery information (if it's a laptop)
battery = psutil.sensors_battery()
if battery:
     plugged = "Plugged in" if battery.power_plugged else "Not Plugged in"
     print(f"\nBattery Status: {plugged}, {battery.percent}%")
else:
     print("\nBattery information unavailable") 

# Disk Information
disk = psutil.disk_usage('/')
print("\nDisk Information: ")
print(f"Total Disk Space: {disk.total / (1024 ** 3):.2f} GB")
print(f"Used Disk Space: {disk.used / (1024 ** 3):.2f} GB")
print(f"Free Disk Space: {disk.free / (1024 ** 3):.2f} GB")