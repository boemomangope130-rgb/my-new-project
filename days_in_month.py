def is_leap(year: int) -> bool:
    """Return True if the given year is a Gregorian leap year.

    Leap year rules:
    - Divisible by 4 => leap year
    - Except years divisible by 100 => not a leap year
    - Except years divisible by 400 => leap year again
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def days_in_month(month: int, year: int) -> int:
    """Return the number of days in the given month for the given year.

    Args:
        month: Month number in range 1..12
        year: Four-digit year (Gregorian calendar)

    Raises:
        ValueError: If month is outside the 1..12 range
    """
    if month < 1 or month > 12:
        raise ValueError("Month must be in 1..12")

    if month == 2:
        return 29 if is_leap(year) else 28

    if month in (4, 6, 9, 11):
        return 30

    return 31


if __name__ == "__main__":
    try:
        month_str = input("Enter month (1-12): ").strip()
        year_str = input("Enter year: ").strip()
        month = int(month_str)
        year = int(year_str)
        print(f"Month = {month}")
        print(f"Year = {year}")
        print(f"Days = {days_in_month(month, year)}")
    except ValueError as e:
        print(f"Error: {e}")
