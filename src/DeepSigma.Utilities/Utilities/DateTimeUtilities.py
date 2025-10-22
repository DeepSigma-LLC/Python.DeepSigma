from datetime import datetime, timedelta
import calendar


def get_quarter(selected_date: datetime) -> int:
    """
            Gets quarter as int from a datetime.
            :param selected_date:
            :return:
            """
    return int((selected_date.month - 1) // 3 + 1)

def get_prior_day(selected_date: datetime = datetime.now()) -> datetime.date:
    """
            Computes and returns prior date.
            :param selected_date: Optional: If no date is passed, then the selected date will default to today's date.
            :return:
            """
    prior_day = selected_date - timedelta(days=1)
    return prior_day

def get_end_of_month(selected_date: datetime = datetime.now(), months_to_add: int = 0) -> datetime.date:
    """
            Gets date at the end of the month for a given datetime with the ability to add or subtract months.
            :param selected_date:
            :param months_to_add:
            :return:
            """
    new_month, new_year = __add_months_to_new_month_and_year(selected_date, months_to_add)
    num_days_in_month = calendar.monthrange(new_year, new_month)[1]
    return selected_date.replace(day=num_days_in_month, month=new_month, year=new_year)

def get_end_of_year(selected_date: datetime = datetime.now(), years_to_add: int = 0) -> datetime.date:
    """
            Gets the date at the end of year given a date and number of years to add/subtract.
            :param selected_date:
            :param years_to_add:
            :return:
            """
    new_month = 12
    num_days_in_month = 31
    new_year = selected_date.year + years_to_add
    return selected_date.replace(day=num_days_in_month, month=new_month, year=new_year)

def date_to_string_iso(selected_date: datetime) -> str:
    """
            Converts date to string of iso format.
            :param selected_date:
            :return:
            """
    return selected_date.isoformat()

def date_to_string(selected_date: datetime, default_format_str: str = '%m-%d-%Y') -> str:
    """
            Converts datetime to string of designated format.
            :param selected_date:
            :param default_format_str:
            :return:
            """
    return selected_date.strftime(default_format_str)

def convert_str_to_datetime(selected_date: str, default_format_str: str = "%m/%d/%Y") -> datetime:
    """
            Converts string to datetime
            :param selected_date:
            :param default_format_str:
            :return:
            """
    return datetime.strptime(selected_date, default_format_str)

def __add_months_to_new_month_and_year(selected_date: datetime, months_to_add: int):
    """
            Takes a date and adds months to the date.
            :param selected_date:
            :param months_to_add:
            :return: Function returns the new date month and year. (month, year)
            """
    total_months = selected_date.year * 12 + selected_date.month - 1  # Converts current date to total months
    new_total_months = total_months + months_to_add
    new_year = new_total_months // 12  # Gets new year
    new_month = new_total_months % 12 + 1  # Gets new month (1-12 range)
    return new_month, new_year
