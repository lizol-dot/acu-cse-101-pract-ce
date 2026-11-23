# ==============================================================================
# ACU CSE 101: Week 02 Guided Workshop - Variables, Expressions and Statements
# Think Python: Chapter 2
#
# Write each part with your instructor / TA. No functions are needed yet.
# ==============================================================================

# ------------------------------------------------------------------------------
# Part 1: Variables & Discount Calculations
# Variables store values that expressions can use to calculate new values.
# A percentage discount reduces the original price; shipping adds to the total.
#
# In-Class Goal:
# Calculate the wholesale cost of 60 books with a cover price of $24.95
# and a 40% discount. Shipping is $3 for the first copy and $0.75 for
# each additional copy. Print the total with two decimal places.
# ------------------------------------------------------------------------------
# TODO: Write Part 1 together in class below:
books = 60
cover_price = 24.95
discount = 0.40
book_cost = cover_price * (1 - discount) * books
shipping = 3 + 0.75 * (books - 1)
total_cost = book_cost + shipping
print(f"Total cost: ${total_cost:.2f}")

# ------------------------------------------------------------------------------
# Part 2: Time Arithmetic with // and %
# Use seconds as a common unit when adding durations.
# Floor division finds complete units; modulo finds the remainder.
#
# In-Class Goal:
# Find the arrival time after leaving at 6:52 AM and running 2 miles
# at 8 minutes 15 seconds per mile and 3 miles at 7 minutes 12 seconds
# per mile. Print the arrival hour and minute in HH:MM format.
# ------------------------------------------------------------------------------
# TODO: Write Part 2 together in class below:
departure = (6*3600)+(52*60)
first_part = 2*((8*60)+15)
sec_part = 3*((7*60)+12)
run_time = first_part+sec_part+departure
hour = run_time//3600
minute = (run_time % 3600)//60
print(f"{hour:02d}:{minute:02d}")

# ------------------------------------------------------------------------------
# Part 3: Centering & Formatting Strings
# String centering adds padding around text to reach a chosen width.
#
# In-Class Goal:
# Center "PYTHON CSE 101" in a 30-character banner using "=" as padding.
# Print the banner.
# ------------------------------------------------------------------------------
# TODO: Write Part 3 together in class below:
banner = "PYTHON CSE 101".center(30, "=")
print(banner)
