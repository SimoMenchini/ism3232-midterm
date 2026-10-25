# main.py

from business_rules import (
    calculate_stay_total,
    format_stay_line,
    gets_welcome_package,
    largest_stay,
    requires_credit_check,
    total_reserved,
)

stays = [
    {"guest": "Kessler", "nightly_rate": 110.00, "nights": 2, "corporate": False},
    {"guest": "Lindqvist", "nightly_rate": 150.00, "nights": 2, "corporate": True},
    {"guest": "Moreno", "nightly_rate": 125.00, "nights": 6, "corporate": False},
    {"guest": "Nakata", "nightly_rate": 140.00, "nights": 20, "corporate": False},
    {"guest": "Osei", "nightly_rate": 95.00, "nights": 15, "corporate": True},
    {"guest": "Petrov", "nightly_rate": 200.00, "nights": 5, "corporate": False},
    {"guest": "Quinn", "nightly_rate": 180.00, "nights": 6, "corporate": False},
    {"guest": "Rahman", "nightly_rate": 260.00, "nights": 10, "corporate": True},
]


def main() -> None:
    """Generates the stay report and summary statistics."""
    print("Seabreeze Inn - Stay Report")

    stay_count = 0
    credit_check_count = 0
    welcome_package_count = 0

    for stay in stays:
        total = calculate_stay_total(
            stay["nightly_rate"], stay["nights"], stay["corporate"]
        )
        has_credit_check = requires_credit_check(total)
        has_welcome_package = gets_welcome_package(stay["nights"], total)

        print(
            format_stay_line(
                stay["guest"], total, has_credit_check, has_welcome_package
            )
        )

        stay_count += 1
        if has_credit_check:
            credit_check_count += 1
        if has_welcome_package:
            welcome_package_count += 1

    grand_total = total_reserved(stays)
    top_guest = largest_stay(stays)
    average_total = grand_total / stay_count if stay_count > 0 else 0.0

    print(f"Stays: {stay_count}")
    print(f"Total reserved: ${grand_total:.2f}")
    print(f"Average stay total: ${average_total:.2f}")
    print(f"Largest stay total: {top_guest}")
    print(f"Credit checks required: {credit_check_count}")
    print(f"Welcome packages: {welcome_package_count}")


if __name__ == "__main__":
    main()
