| Section | C# - Name | Date |
| ------- | ------- | ------- |
| 9 - Arayat | #05 - Marion Dominic L. Caleon | 08/13 |

USED WORKSHEET: *****Smart School Canteen Queue*****

# Step 1
*The PSHS canteen’s process is slow.*

# Step 2
0. Some students take too long to decide what to order.
1. The cashier has to manually calculate totals and give change.
2. There is no system to track which food items are running out.

# Step 3
| Sub-Problem | CT Skill | Solution |
| ------- | ------- | ------- |
| Some students take too long to decide what to order. | Breaking Down Complexity | By breaking down choices into simpler forms—number of orders, lists of food, available budget—may speed up the decision. |
| The cashier has to manually calculate totals and give change. | Efficiency | We can make a built-in calculator to speed thing up. |
| There is no system to track which food items are running out. | Foundation for Algorithms | We first need to need to make a structure deigned to track food items to make a fully functioning system. |

# Step 4
0. Initiate App
1. Initiate Variables: supply (set: name (set: strings), amount (set: int), price (set:float), bought (set:int)), supplyAddNum, supplyMinusNum, income
2. Choose Mode: Supply Check, Supply Add, Buying (Supply Subtract), Exit
3. If: Supply Check
   0. Print Supply Type and Supply Amount through iterator loop
1. If: Supply Add
        2. Input Supply Type
            3. If Supply Type exists in set "name":
                4. Input positive supplyAddNum (int)
                5. Confirm
                6. Add supplyAddNum to "amount" in index of "name"
            7. Else:
                8. Loop back to input supply type
6. If: Buy
      7. Initiate loop:
            2. Input Supply Type
                  3. If Supply Type exists in set "name":
                        4. If amount in index of "name" < 1:
                              5. Loop back to supply type input, print "No Supply"
                        6. If amount in index of "name" !< 1:
                              7. Add price to supplyMinusNum
                              8. Add bought in index of "name" by 1
                              9. Loop Back to Input
            7. Else:
                  8. Confirm
                  9. Add supplyMinusNum to income
                  10. Subtract amount in index of "name" to bought in index of "name"
11. If: Exit
      12. Print income
      13. Reprint Supply Check
      14. Terminate Program, no longer looping
11. Loop back to choose mode
