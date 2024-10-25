# prompts
current_time_prompt = "Enter the current time (in 24-hour format, 0-23): "
hours_to_wait_prompt = "Enter the number of hours to wait for the alarm: "

# asking user for input for current time
current_time = int(input(current_time_prompt))

# asking user for the alarm
hours_to_wait = int(input(hours_to_wait_prompt))

# calculation
alarm_time = (current_time + hours_to_wait) % 24


print(f"The time when the alarm will go off is: {alarm_time}:00")
