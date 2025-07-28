from datetime import date, timedelta, datetime

# subclassing the built-in ValueError to create MeetupDayException
class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.

    message: explanation of the error.

    """
    def __init__(self):
        super().__init__("That day does not exist.")


def meetup(year: int, month: int, week: str, day_of_week: str) -> date:
	day = 0
	first_of_month = datetime(year, month, 1)
	match week:
			case "teenth":
					day = find_teenth_day(first_of_month, day_of_week)
			case "last":
					day = find_last_day(first_of_month, day_of_week)
			case _:
					nth_indexes = {"first": 1, "second": 2, "third": 3, "fourth": 4, "fifth": 5}
					day = find_nth_day(first_of_month, nth_indexes[week], day_of_week)

	return date(year, month, day)

def find_day_index(day: str) -> int:
	day_indexes = {"Sunday": 6, "Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5}

	return day_indexes[day]

def find_last_day(current_date: datetime, day: str) -> int:
	target_day = find_day_index(day)
	target_month = current_date.month

	last_day = None

	while(current_date.month == target_month):
		if current_date.weekday() == target_day:
				last_day = current_date.day
			
		current_date += timedelta(days=1)

	return last_day

def find_teenth_day(current_date: datetime, day: str) -> int:
	target_day = find_day_index(day)
	target_month = current_date.month

	while(current_date.month == target_month):
		if current_date.weekday() == target_day and current_date.day >= 13 and current_date.day <= 19:
			return current_date.day
			
		current_date += timedelta(days=1)


def find_nth_day(current_date: datetime, nth: int, day: str) -> int:
	target_day = find_day_index(day)
	target_month = current_date.month
	hit_counter = 1

	while(current_date.month == target_month):
		if current_date.weekday() == target_day:
			if hit_counter == nth:
					return current_date.day
			else:
					hit_counter += 1
		
		current_date += timedelta(days=1)

	raise MeetupDayException()