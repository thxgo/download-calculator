def download_time(file_size_mb: float, speed_mbps: float) -> tuple[int, int, int]:
    file_size_mb = file_size_mb * 8 
    total_sec = file_size_mb / speed_mbps 

    hours = int(total_sec // 3600)
    minutes = int((total_sec % 3600) // 60)
    seconds = int(total_sec % 60)

    return hours, minutes, seconds

def main():
    print("Download Time Calculator\nPS: GB -> MB => multiply by 1024")

    file_size_mb = float(input('\nsize file (MB):'))
    speed_mbps = float(input('internet speed (Mbps):'))

    hours, minutes, seconds = download_time(file_size_mb, speed_mbps)
    print(f'\ndownload time: {hours} hour(s), {minutes} minute(s), {seconds} second(s)')

if __name__ == "__main__":
    main()
