# Pseudocode & Team Contribution Summary

**CSC1401 Assignment III — Team ID: 37**

## Meeting Attendance & Code Contribution

| Participant | Meetings Attended | Meeting Times | Lines Contributed (final version) | No. of Lines |
|---|---|---|---|---|
| Xavier Jackson | 4 | 15/04/26 11am-12pm, 28/04/26 11:30am-3pm | 16-24, 27-38, 40-51, 53-100, 102-110, 112-132, 135-158, 160-172 | 100 |
| Fahed Haidar | 4 | 30/4/26 3:30pm-5:30pm, 1/5/26 4pm-4:45pm | 16-24, 27-38, 40-51, 53-100, 102-110, 112-132, 135-158, 160-172 | 40 |

## Pseudocode

### Main Program
**Goal:** Let user browse products and their prices, exit loop if user inputs "end"

```
Start Program
    Initialise product_list and price_list
    Initialise empty shopping_record list
    Display catalogue of products (codes, names, prices)
    Repeat
        Call add_record
        IF user enters "End"
            EXIT loop
        End If
    Until "End" is entered
    IF shopping_record is empty
        Display "You have not selected any items to buy,"
        Display "There are no records to show"
    Else
        Display all shopping records
        Display total cost
        Display sorted records
    End If
End Program
```

### Add Record
**Goal:** Let the user choose their membership status, product code, quantity, and shipping method, then calculate total cost based on these choices.

```
function add_record
    ask user for membership (Yes / No / End)
    if input = "End"
        return "End"
    end if
    if membership invalid
        display error
        return to start of function
    end if
    ask user for product code (0-39)
    validate using is_valid_code
    if invalid
        display error
        return to start of function
    ask user for quantity (1-29)
    validate using is_valid_quantity
    if invalid
        display error
        return to start of function
    ask user for shipping method (Delivery / Pick-up)
    if invalid
        display error
        return to start of function
    end if
    calculate shipping fee
    calculate subtotal = price x quantity + shipping
    if member = Yes
        apply 10% discount
    end if
    calculate total cost
    add record to shopping_record list
    display "Record added"
end function
```

### Show Record
**Goal:** Display each record stored

```
function show_record
    display each record showing: Membership, Code, Product, Price, Quantity, Shipping method, Shipping fee, Cost
```

### Total Cost
**Goal:** Calculate the total cost of all records and display it

```
function total_cost
    set total = 0
    for each record in shopping_record
        add cost to total
    end for
    display total cost
```

### Sort Record
**Goal:** Sort all the records and present the necessary information to the user

```
function sort_record
    display: Code, Product, Price, Quantity, Cost
    sort records by product code (0-39)
    if same product code exists
        merge quantities and costs
    end if
    display sorted records
```
