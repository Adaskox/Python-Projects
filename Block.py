import time
import pygetwindow as gw

# Title of the YouTube browser window
youtube_window_title = "YouTube - Google Chrome"  # Adjust the title for your browser

# Initialize a variable to track the total time spent on YouTube
total_time_spent = 0

# Write here a code that will reset total time spent every 24h

# Set the time interval for checking (in seconds)
check_interval = 60  # 5 seconds

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

    if total_time_spent >= 120:
        print('stop') # Write here a code, that will block YT after 120min of usage

    # Wait for the specified interval before checking again
    time.sleep(check_interval)
