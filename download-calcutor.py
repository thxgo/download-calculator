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

def download_time(file_size_mb, speed_mbps):
    file_size_mb = file_size_mb * 8 
    total_sec = file_size_mb / speed_mbps 

    hours = int(total_sec // 3600)
    minutes = int((total_sec % 3600) // 60)
    seconds = int(total_sec % 60)

    return hours, minutes, seconds

def main():
    print("Download Time Calculator\nPS: GB -> MB => multiply by 1024")

    file_size_mb = get_float('\nfile size (MB): ')
    speed_mbps = get_float('internet speed (Mbps): ')

    hours, minutes, seconds = download_time(file_size_mb, speed_mbps)
    print(f'\ndownload time: {hours} hour(s), {minutes} minute(s), {seconds} second(s)')

if __name__ == "__main__":
    main()
