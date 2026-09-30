# Shopping Cart Simulation (CSC1401 Assessment 3)

A command-line Python program simulating a simple shopping cart system.
Users browse a 40-item catalogue, add items to their cart (choosing
membership status, quantity, and shipping method), then view an itemized
summary, total cost, and a version of the cart sorted and merged by
product code.

**Team ID:** 37
**Authors:** Xavier Jackson, Fahed Haidar

## Features
- Displays a formatted two-column product catalogue (40 items, codes 0-39)
- Input validation for product code, quantity, and shipping method
- Membership discount (10% off for members)
- Delivery fee calculation based on quantity (flat $2 + $1.60 per extra item),
  or free Pick-up
- Order summary with itemized records and running total
- Sorted/merged view: combines multiple entries of the same product into
  one line with summed quantity and cost

## How to Run
```bash
python shopping_cart.py
```
Follow the prompts: enter `Yes`/`No` for membership (or `End` to finish
adding items), a product code (0-39), a quantity (1-29), and a shipping
method (`Delivery` or `Pick-up`).

## Files
- `shopping_cart.py` — the program
- `CSC1401_Assessment_3_Code.ipynb` — original Jupyter notebook version (includes a sample run)
- `pseudocode_and_contributions.md` — pseudocode design and team contribution summary

## Design
The program is broken into functions by responsibility:
- `show_catalogue()` — displays the product list
- `is_valid_code()` / `is_valid_quantity()` — input validation
- `add_record()` — handles one full item-adding transaction
- `show_record()` / `total_cost()` — displays the cart and running total
- `sort_records()` — sorts and merges records by product code
