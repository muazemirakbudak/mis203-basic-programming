# Lab 03 - Order Approval System

## Test Table (Boundary Cases for 500 TRY Threshold)

| Test Case | Order Amount (TRY) | Stock | Quantity | Member? | Expected Outcome |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Below 500** | 499.99 | 100 | 5 | Yes | Approved, No discount. Final: 499.99 TRY |
| **Exactly 500** | 500.00 | 100 | 5 | Yes | Approved, 10% discount. Final: 450.00 TRY |
| **Above 500** | 500.01 | 100 | 5 | Yes | Approved, 10% discount. Final: 450.009 TRY |

## Test & Change Note

* **Ran Test:** Checked `requested_quantity = 0` with `available_stock = 10`.
* **Change Made:** Initially, the code only checked `requested_quantity > available_stock`. After testing with zero and negative numbers, I added `requested_quantity <= 0` check to prevent invalid quantity requests from processing.
