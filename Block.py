import time
import pygetwindow as gw
import datetime

# Title of the YouTube browser window
youtube_window_title = "YouTube - Google Chrome"  # Adjust the title for your browser

# Initialize a variable to track the total time spent on YouTube
total_time_spent = 0

# Write today's date to a variable
day = datetime.date.today()

# Set the time interval for checking (in seconds)
check_interval = 60  # 1 minute

# localhost ip number
ip = "127.0.0.1"

# Path to hosts file
hosts = r"C:\Windows\System32\drivers\etc\hosts"

# List of blocked websites
sites = [
    "www.facebook.com",
    "www.youtube.com"
]

while True:
    browser_open = False
    for window in gw.getAllTitles():
        print(f"Window Title: {window}")
        if youtube_window_title.lower() in window.lower():
            browser_open = True
            break

    if browser_open:
        total_time_spent += 1  # Add 1 minute to the total time

    # Print the total time spent on YouTube
    print(f"Total time spent on YouTube: {total_time_spent} minutes")

    # If date changes, time resets
    if day != datetime.date.today():
        today = datetime.date.today()
        total_time_spent = 0

    if total_time_spent >= 120:
    # Reading hosts file
        with open(hosts, "r+") as file:
            content = file.read()
            for website in sites:
                # if site is note in sites, add it
                if not website in content:
                    with open(hosts, "a") as writefile:
                        writefile.write(ip + " " + website + "\n")
    else:
        # If limit was not reached, delete the sites from hosts file
        with open(hosts, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in sites):
                    file.write(line)
            file.truncate()

    # Wait for the specified interval before checking again
    time.sleep(check_interval)
