# business_rules.py
# Author: Simone Menchini

# Rules 2 and 3:
DISCOUNT_MID_MIN_NIGHTS: int = 4
DISCOUNT_LONG_MIN_NIGHTS: int = 14
DISCOUNT_RATE_NONE: float = 0.0
DISCOUNT_RATE_MID: float = 0.06
DISCOUNT_RATE_LONG: float = 0.18
DISCOUNT_RATE_CORPORATE_MIN: float = 0.06

# Rule 4:
CLEANING_FEE_THRESHOLD: float = 300.0
CLEANING_FEE_RATE: float = 40.0

# Rule 5:
CREDIT_CHECK_THRESHOLD: float = 2000.0

# Rule 6:
WELCOME_PACKAGE_MIN_NIGHTS: int = 5
WELCOME_PACKAGE_MIN_TOTAL: float = 1000.0


def calculate_room_cost(nightly_rate: float, nights: int) -> float:
    """Returns the room cost before any discount (rule 1)."""
    return nightly_rate * nights


def get_stay_discount(nights: int, corporate: bool = False) -> float:
    """Returns the discount rate as a decimal, so 6% is 0.06 (rules 2 and 3)."""
    if nights >= DISCOUNT_LONG_MIN_NIGHTS:
        return DISCOUNT_RATE_LONG
    if nights >= DISCOUNT_MID_MIN_NIGHTS:
        return DISCOUNT_RATE_MID
    if corporate:
        return DISCOUNT_RATE_CORPORATE_MIN
    return DISCOUNT_RATE_NONE


def calculate_stay_total(
    nightly_rate: float, nights: int, corporate: bool = False
) -> float:
    """Returns the stay total for one stay: the discounted cost, plus the cleaning fee when it applies (rule 4). It must call your first two functions."""
    base_cost = calculate_room_cost(nightly_rate, nights)
    discount_rate = get_stay_discount(nights, corporate)
    discounted_cost = base_cost * (1.0 - discount_rate)
    cleaning_fee = (
        CLEANING_FEE_RATE if discounted_cost <= CLEANING_FEE_THRESHOLD else 0.0
    )
    return discounted_cost + cleaning_fee


def requires_credit_check(total: float) -> bool:
    """Returns True when the stay total requires a credit check (rule 5), otherwise False."""
    return total >= CREDIT_CHECK_THRESHOLD


def gets_welcome_package(nights: int, total: float) -> bool:
    """Returns True when the stay gets a welcome package (rule 6), otherwise False."""
    return nights >= WELCOME_PACKAGE_MIN_NIGHTS and total >= WELCOME_PACKAGE_MIN_TOTAL


def total_reserved(stays: list) -> float:
    """Returns the sum of the stay totals for every stay in the list. It must use a for loop that calls calculate_stay_total."""
    grand_total = 0.0
    for stay in stays:
        if isinstance(stay, dict):
            rate = float(stay["nightly_rate"])
            nights = int(stay["nights"])
            corporate = bool(stay.get("corporate", False))
        else:
            rate = float(stay[1])
            nights = int(stay[2])
            corporate = bool(stay[3]) if len(stay) > 3 else False

        grand_total += calculate_stay_total(rate, nights, corporate)
    return grand_total


def largest_stay(stays: list) -> str:
    """Returns the guest of the stay with the largest stay total. If two are tied for largest, it returns the one that comes first in the list. An empty list returns an empty string, "". It must use a for loop that calls calculate_stay_total."""
    if not stays:
        return ""

    top_guest: str = ""
    max_total: float = -1.0
    is_first: bool = True

    for stay in stays:
        if isinstance(stay, dict):
            guest = stay["guest"]
            rate = float(stay["nightly_rate"])
            nights = int(stay["nights"])
            corporate = bool(stay.get("corporate", False))
        else:
            guest = str(stay[0])
            rate = float(stay[1])
            nights = int(stay[2])
            corporate = bool(stay[3]) if len(stay) > 3 else False

        stay_total = calculate_stay_total(rate, nights, corporate)
        if is_first or stay_total > max_total:
            max_total = stay_total
            top_guest = guest
            is_first = False

    return top_guest


def format_stay_line(
    guest: str, total: float, credit_check: bool, welcome_package: bool
) -> str:
    """Returns one line of the report, such as Kessler: $260.00 | credit check: no | welcome package: no. Each True/False value is shown as yes or no, and the amount always has two decimal places."""
    credit_str = "yes" if credit_check else "no"
    welcome_str = "yes" if welcome_package else "no"
    return f"{guest}: ${total:.2f} | credit check: {credit_str} | welcome package: {welcome_str}"
