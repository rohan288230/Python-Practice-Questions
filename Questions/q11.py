# Q11. Time Converter: Total seconds ko hours, minutes aur 
# seconds mein convert karo using `//` and `%`.
total_seconds = int(input("Enter total seconds : "))
hour = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60
print(f"Hours : {hour} | Minutes : {minutes} | Seconds : {seconds}")