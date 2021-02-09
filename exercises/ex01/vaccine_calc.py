"""A vaccination calculator."""

__author__ = "730315718"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...

population: int = int(input("Population: "))


doses_admin: int = int(input("Doses administered: "))
doses_day: int = int(input("Doses per day: "))
target: int = int(input("Target percent vaccinated: "))


target_vac: float = float(target / 100)
to_be_vac: float = float(population * target_vac)
individual: int = round(doses_admin / 2)
pop_left: int = int(to_be_vac - individual)
daily_vac: float = float(pop_left / doses_day)

today: datetime = datetime.today()

days: int = round(daily_vac * 2)


future: datetime = today + timedelta(days)

print("We will reach " + str(target) + "% vaccination in " + str(days) + " days.")
print("Which falls on " + str(future.strftime("%B %d, %Y.")))