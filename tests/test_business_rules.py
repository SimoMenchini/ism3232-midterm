from business_rules import (
    calculate_room_cost,
    calculate_stay_total,
    format_stay_line,
    get_stay_discount,
    gets_welcome_package,
    largest_stay,
    requires_credit_check,
    total_reserved,
)

# calculate_room_cost


def test_calculate_room_cost():
    assert calculate_room_cost(100.0, 3) == 300.00


def test_calculate_room_cost_single_night():
    assert calculate_room_cost(150.50, 1) == 150.50


# get_stay_discount


def test_get_stay_discount_tier1_below_threshold():
    # 3 nights is below the threshold, no discount
    assert get_stay_discount(3, corporate=False) == 0.0


def test_get_stay_discount_tier1_at_threshold():
    # 4 nights is at the threshold, discount is 6%
    assert get_stay_discount(4, corporate=False) == 0.06


def test_get_stay_discount_tier2_below_threshold():
    # 13 nights is below the second threshold, discount is 6%
    assert get_stay_discount(13, corporate=False) == 0.06


def test_get_stay_discount_corporate_change_the_answer():
    # Under 4 nights, corporate=True, discount is 6%
    standard_discount = get_stay_discount(3, corporate=False)
    corporate_discount = get_stay_discount(3, corporate=True)
    assert standard_discount == 0.0
    assert corporate_discount == 0.06


def test_get_stay_discount_tier2_at_threshold():
    # 14 nights is at the second threshold, discount is 18%
    assert get_stay_discount(14, corporate=False) == 0.18


# calculate_stay_total


def test_calculate_stay_total_corporate_change_answer():
    # Corporate status reduces total cost
    standard_total = calculate_stay_total(200.00, 2, corporate=False)
    corporate_total = calculate_stay_total(200.00, 2, corporate=True)
    assert round(standard_total, 2) != round(corporate_total, 2)


def test_calculate_stay_total_cleaning_fee_at_threshold():
    # Discounted cost is $300.00 + $40
    total = calculate_stay_total(100.00, 3, corporate=False)
    assert round(total, 2) == 340.00


def test_calculate_stay_total_cleaning_fee_above_threshold():
    # Discounted cost is $301.00, no cleaning fee
    total = calculate_stay_total(301.00, 1, corporate=False)
    assert round(total, 2) == 301.00


# requires_credit_check


def test_requires_credit_check_below_threshold():
    # $1999.99 is below the threshold, False
    assert requires_credit_check(1999.99) is False


def test_requires_credit_check_at_threshold():
    # $2000.00 is at the threshold, True
    assert requires_credit_check(2000.00) is True


# gets_welcome_package


def test_gets_welcome_package_nights_at_threshold():
    # 5 nights is at the threshold, True
    assert gets_welcome_package(5, 1200.00) is True


def test_gets_welcome_package_nights_below_threshold():
    # 4 nights is below the threshold, False
    assert gets_welcome_package(4, 1200.00) is False


def test_gets_welcome_package_total_below_threshold():
    # Nights are > 6, total is below the threshold, False
    assert gets_welcome_package(7, 999.99) is False


def test_gets_welcome_package_total_at_threshold():
    # Nights are > 6, total is at the threshold, True
    assert gets_welcome_package(7, 1000.00) is True


# total_reserved


def test_total_reserved_short_list():
    short_stays = [
        {"guest": "Mario", "nightly_rate": 100.00, "nights": 1, "corporate": False},
        {"guest": "Luigi", "nightly_rate": 200.00, "nights": 2, "corporate": False},
    ]
    assert round(total_reserved(short_stays), 2) == 540.00


def test_total_reserved_empty_list():
    assert round(total_reserved([]), 2) == 0.00


# largest_stay


def test_largest_stay_short_list():
    short_stays = [
        {"guest": "Mario", "nightly_rate": 100.00, "nights": 1, "corporate": False},
        {"guest": "Luigi", "nightly_rate": 500.00, "nights": 3, "corporate": False},
    ]
    assert largest_stay(short_stays) == "Luigi"


def test_largest_stay_tie_returns_first():
    # Identical total values, return first guest
    tied_stays = [
        {
            "guest": "Mario First",
            "nightly_rate": 100.00,
            "nights": 3,
            "corporate": False,
        },
        {
            "guest": "Luigi Second",
            "nightly_rate": 100.00,
            "nights": 3,
            "corporate": False,
        },
    ]
    assert largest_stay(tied_stays) == "Mario First"


def test_largest_stay_empty_list():
    assert largest_stay([]) == ""


# format_stay_line


def test_format_stay_line_all_no():
    expected = "Kessler: $260.00 | credit check: no | welcome package: no"
    assert (
        format_stay_line("Kessler", 260.00, credit_check=False, welcome_package=False)
        == expected
    )


def test_format_stay_line_all_yes():
    expected = "Nakata: $2296.00 | credit check: yes | welcome package: yes"
    assert (
        format_stay_line("Nakata", 2296.00, credit_check=True, welcome_package=True)
        == expected
    )
