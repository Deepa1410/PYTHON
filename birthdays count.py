from datetime import datetime


birthday_str = "2005-03-29"
birthday = datetime.strptime(birthday_str, "%Y-%m-%d")


today = datetime.today()


days_alive = (today - birthday).days

print(f"You have been alive for {days_alive} days.")
