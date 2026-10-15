# 🛒 Shopping Cart Simulation

**Course:** CSC1401 — Assessment 3  
**Team ID:** 37  
**Authors:** Xavier Jackson, Fahed Haidar — IT/Data Science Student

## Project Overview

A command-line Python shopping cart application developed as part of CSC1401 Assessment 3.

The program simulates a complete shopping experience where users can browse a 40-item product catalogue, add products to a cart, select membership and shipping options, and receive an itemised order summary.

The project demonstrates practical Python programming skills including:

- Functions and modular program design
- Input validation
- Lists and data structures
- Conditional logic
- Loops and user interaction
- Sorting and data processing
- Calculations and formatted output
- Jupyter Notebook development

## Key Features

- Displays a formatted two-column product catalogue containing 40 products
- Validates product codes, quantities, membership status and shipping method
- Applies a 10% membership discount
- Calculates delivery fees based on quantity
- Provides free Pick-up as an alternative shipping method
- Generates an itemised order summary and running total
- Sorts and merges duplicate product entries by product code

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
