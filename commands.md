# Terminal Record: Seabreeze Inn



## 1. Building the project

```bash
mkdir ism3232-midterm
cd ism3232-midterm
git init
pyton3 -m venv .venv
source .venv/bin/activate
which python3
pip install pytest ruff
pip freeze > requirements.txt
echo '.venv/' > .gitignore
echo '__pycache__/' >> .gitignore
touch business_rules.py main.py commands.md README.md
mkdir tests
touch tests/__init__.py tests/test_business_rules.py
git remote add origin git@github.com:SimoMenchini/ism3232-midterm.git
git branch -M main
```



## 2. The virtual environment

/home/mench/ism3232/ism3232-midterm/.venv/bin/python3
The virtual environment is active because the path points to the python3 binary inside the local .venv/bin directory 



## 3. The project structure

.
├── README.md
├── __pycache__
│   └── business_rules.cpython-314.pyc
├── business_rules.py
├── commands.md
├── main.py
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py
The .venv folder is on my computer but not in my GitHub repositoty because it is listed in .gitignore



## 4. Every function and test

main.py
26:def main() -> None:

business_rules.py
23:def calculate_room_cost(nightly_rate: float, nights:int) -> float:
27:def get_stay_discount(nights: int, corporate: bool = False) -> float:
37:def calculate_stay_total(nightly_rate: float, nights: int, corporate: bool = False) -> float:
45:def requires_credit_check(total: float) -> bool:
49:def gets_welcome_package(nights: int, total: float) -> bool:
53:def total_reserved(stays: list) -> float:
69:def largest_stay(stays: list) -> str:
98:def format_stay_line(guest: str, total: float, credit_check: bool, welcome_package: bool) -> str:

tests/test_business_rules.py
16:def test_calculate_room_cost():
19:def test_calculate_room_cost_single_night():
26:def test_get_stay_discount_tier1_below_threshold():
30:def test_get_stay_discount_tier1_at_threshold():
34:def test_get_stay_discount_tier2_below_threshold():
38:def test_get_stay_discount_corporate_change_the_answer():
45:def test_get_stay_discount_tier2_at_threshold():
52:def test_calculate_stay_total_corporate_change_answer():
58:def test_calculate_stay_total_cleaning_fee_at_threshold():
63:def test_calculate_stay_total_cleaning_fee_above_threshold():
72:def test_requires_credit_check_below_threshold():
76:def test_requires_credit_check_at_threshold():
84:def test_gets_welcome_package_nights_at_threshold():
88:def test_gets_welcome_package_nights_below_threshold():
92:def test_gets_welcome_package_total_below_threshold():
96:def test_gets_welcome_package_total_at_threshold():
104:def test_total_reserved_short_list():
111:def test_total_reserved_empty_list():
118:def test_largest_stay_short_list():
125:def test_largest_stay_tie_returns_first():
133:def test_largest_stay_empty_list():
140:def test_format_stay_line_all_no():
144:def test_format_stay_line_all_yes():

business_rules.py defines 8 functions, and tests/test_business_rules.py defines 23 tests.



## 5. Which files print

main.py
commands.md

main.py is the only Python file that prints, business_rules.py is not in the list because it strictly returns values without invoking the print () function.



## 6.The commit history

e3e9243 (HEAD -> main, origin/main) ism3232-midterm: README.md, EXTRA Commitment, I did not commit each part separately because it was said in part 7 and by then I had already submitted everything together except for commands.md and README.md
9c620e3 ism3232-midterm: command.md and README.md
3e13879 ism3232-midterm: command.md
4e7573f ism3232-midterm: Seabreeze Inn

There was 4 commitment at that point