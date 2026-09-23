# Assignment 03 — CHANGES

**Name:** Theikdi Nyan  **Student ID:** 6705140053

This is the written part of your submission. Explain **what you changed and why**, then record your **prompt log**. Keep before/after snippets to a line or two.

---

## 1 · What I changed

One row per change. Name the OOP concept and say how you checked the behaviour was unchanged.

| # | Code smell in the original | What I changed it to | OOP concept applied | How I verified behaviour was unchanged |
|---|---|---|---|---|
| 1 | Products and order items were stored as tuples and accessed by numeric indexes. | Created `Product` and `OrderItem` classes. `OrderItem` has-a `Product`, and constructors validate important state such as product type and positive integer quantity. | Classes / composition / encapsulation | Reviewed the object relationships and constructor checks, then ran `python Assignment_03.py` after completing the refactor and confirmed `PASS`. |
| 2 | Discount and points logic used repeated `if/elif` checks on the customer tier. | Created a `Customer` base class with `RegularCustomer`, `SilverCustomer`, `GoldCustomer`, and `PlatinumCustomer` subclasses. Each subclass defines its own discount rate and points multiplier. | Inheritance / polymorphism | Checked all tier rules, including the `subtotal == 100` and `subtotal > 100` boundary, and confirmed the final self-test returned `PASS`. |
| 3 | Calculations and receipt printing were mixed together in the same legacy function. | Moved calculations into `Order` methods such as `subtotal()`, `discount()`, `tax()`, `total()`, and `points()`, while `receipt()` builds the receipt text and `refactored_main()` handles printing. | Pure methods / interface vs implementation | Compared the four supplied orders with the legacy behaviour and confirmed their totals and receipt text matched. The supplied self-test also returned `PASS`. |
| 4 | Tax logic depended on checking product categories inside the total calculation, and order data was still represented by legacy tuples. | Each `Product` stores its own tax rate and calculates tax through `tax_for()`. Added `build_products()` and `build_orders(products)` to convert the legacy data into connected OOP objects. | Composition / encapsulation / responsibility separation | Checked that the builders produced `Product`, `Customer`, `OrderItem`, and `Order` objects with the correct relationships, then ran the supplied self-test and got `PASS`. |
| 5 | Business-rule numbers such as discount rates, thresholds, bulk rates, and points multipliers were written directly in logic. | Replaced them with named constants and customer-class attributes such as `DISCOUNT_THRESHOLD`, `BULK_DISCOUNT_RATE`, `LOW_DISCOUNT_RATE`, `HIGH_DISCOUNT_RATE`, and `POINTS_MULTIPLIER`. The refactored section also does not use `global`. | Clean code / encapsulation | Reviewed the refactored section for remaining business-rule literals and ran `python Assignment_03.py`; it printed `PASS - behaviour is unchanged. Your refactor is safe.` |

---

## 2 · Short reflection (4–6 sentences)

The change that improved the code the most was replacing the customer tier `if/elif` chains with a customer class hierarchy. Each customer type now owns its own discount and points rules, so the `Order` class does not need to know which tier it is working with. Separating the calculation methods from receipt printing also made the program easier to read and check because each method has one clear responsibility. Keeping the behaviour identical required me to be careful with the discount boundary at 100, the bulk-discount quantity rule, food tax, points calculation, and the exact receipt formatting. I used the provided self-test throughout the refactor and confirmed the final program still prints `PASS`.

---

## 3 · Prompt log (Level 2 — required)

Record **every** prompt where AI helped. If you wrote a part yourself, say so in one row. AI-shaped code with an empty log does **not** meet the Level-2 policy.

| # | My prompt to the AI | What it suggested (summary) | Accept / reject / edited | How I checked it |
|---|---|---|---|---|
| 1 | "check the activities/week_05/Assignment_03.py and Changes.md under Friday Morning class course. brief me what I have to do” | Summarized the assignment requirements: refactor only the provided solution section, use OOP classes and constructor validation, replace tier if/elif logic with customer subclasses, separate calculations from receipt printing, replace magic numbers with named constants, remove the leftover global, run the self-test until PASS, and complete CHANGES.md. | **Accepted** — used the summary as a checklist before starting the refactor. | I reviewed each part as I implemented it, used Codex for focused checks, and verified the final program with the supplied self-test. |
| 2 | “Review only my `Product` and `OrderItem` classes in `Assignment_03.py`. Check whether the constructor validation, composition, and methods satisfy the assignment requirements.” | Confirmed the composition and methods were suitable. It pointed out that `quantity = 1.5` would still pass and suggested requiring a positive integer. It also mentioned optional stronger checks for names and prices. | **Partially accepted** — added integer validation for quantity and kept the positive-quantity check. I did not add the optional extra validation because it was not required. | Re-read the constructor logic and later confirmed the completed assignment still passed the supplied self-test. |
| 3 | “now I just wrote the customer class and subclasses, review/check those” | Confirmed that the subclasses replaced the tier `if/elif` chains and that the discount and points rules were correct, including the 100 versus over-100 boundary. It also suggested moving `tier = "none"` to `RegularCustomer`, naming tier business values, and restoring the missing `Product` type check in `OrderItem`. | **Edited / partially accepted** — moved the regular tier label to `RegularCustomer`, restored the `Product` type check, and later named the tier discount rates and points multipliers. I did not add the optional whitespace-only name check. | Used the focused tier checks, including the 100 boundary and points multipliers, and later confirmed the complete program returned `PASS`. |
| 4 | “review order class, check the composition is correct or not and calculation methods too” | Confirmed that `Order` correctly has-a `Customer` and has-many `OrderItem` objects and that the calculation methods return values without printing. It found that validating `items` before converting to a list could consume a generator, and noted that a bare `Customer` should not be accepted. | **Accepted / edited** — converted `items` to a list before validation and added a check that rejects the base `Customer` class while allowing concrete subclasses. | Codex compared all four supplied orders with the legacy behaviour and checked an additional subtotal-100 case. The final self-test also returned `PASS`. |
| 5 | “Review my `build_products()`, `build_order(products)` and `refactored main()`. are those satisfy the assigned tasks?” | Confirmed that the builder functions correctly convert the legacy data into connected OOP objects and that `refactored_main()` prints receipts and the grand total. It ran the supplied self-test successfully. It also noted that `CHANGES.md` was still incomplete and that tier rates and points multipliers were still numeric literals. | **Accepted** — kept the builder/main implementation, completed `CHANGES.md`, and followed up on the remaining numeric literals. | Codex ran the supplied self-test and reported `PASS`; I also ran `python Assignment_03.py` on the final file and confirmed the same result. |
| 6 | “You said the tier rates and points multipliers are still numeric literals. Which values should I change into named constants for cleaner code? Please only review that part.” | Suggested naming the tier-specific discount values and points multipliers as class attributes such as `LOW_DISCOUNT_RATE`, `HIGH_DISCOUNT_RATE`, and `POINTS_MULTIPLIER`. It also confirmed that `DISCOUNT_THRESHOLD` and `POINTS_DIVISOR` were already named. | **Accepted** — replaced the remaining tier-specific numeric literals with named class attributes on each customer subclass. | Ran `python Assignment_03.py` on the final version and confirmed `PASS - behaviour is unchanged. Your refactor is safe.` |

**Ownership statement.** *By submitting, I confirm I understand and can explain every line of code I submitted, and that this prompt log reflects my actual AI use.*

---

## 4 · Before-you-submit checklist

- [x] `python Assignment_03.py` prints **PASS**.
- [x] No tuples / parallel lists left in the refactored design — products, orders, and items are objects.
- [x] No `if tier == ...` chains — tiers are a class family.
- [x] Calculation methods **return** values and do not `print`; printing is separate.
- [x] Constructors validate state; no leftover `global`; magic numbers are named.
- [x] The change table and reflection above are filled in.
- [x] The prompt log is complete and the ownership statement is included.
