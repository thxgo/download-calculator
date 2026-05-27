def get_unit():
    while True:
        unit = input("unit (MB/GB): ").strip().upper()
        if unit in ("MB", "GB"):
            return unit
        print("Error: enter MB or GB.")


def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Error: value must be greater than zero.")
            else:
                return value
        except ValueError:
            print("Error: invalid input, enter a number.")


def download_time(file_size, speed_mbps):
    file_size = file_size * 8 
    total_sec = file_size / speed_mbps

    hours = int(total_sec // 3600)
    minutes = int((total_sec % 3600) // 60)
    seconds = int(total_sec % 60)

    return hours, minutes, seconds


def main():
    print("Download Time Calculator\n")
    
    unit = get_unit()
    file_size = get_float(f'file size ({unit}): ')
    
    if unit == "GB":
        file_size = file_size * 1024

    speed_mbps = get_float('internet speed (Mbps): ')
    hours, minutes, seconds = download_time(file_size, speed_mbps)

    print(f'\ndownload time: {hours}h, {minutes}m, {seconds}s\nspeed: {speed_mbps:.0f} Mbps ({speed_mbps / 8:.2f} MB/s)')


if __name__ == "__main__":
    main()

