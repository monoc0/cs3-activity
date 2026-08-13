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
      1. Input Supply Type
            1. If Supply Type exists in set "name":
                  1. Input positive supplyAddNum (int)
                  2. Confirm
                  3. Add supplyAddNum to "amount" in index of "name"
            1. Else:
                  1. Loop back to input supply type
6. If: Buy
      1. Initiate loop:
            1. Input Supply Type
                  1. If Supply Type exists in set "name":
                        1. If amount in index of "name" < 1:
                              1. Loop back to supply type input, print "No Supply"
                        1. If amount in index of "name" !< 1:
                              1. Add price to supplyMinusNum
                              1. Add bought in index of "name" by 1
                              1. Loop Back to Input
            1. Else:
                  1. Confirm
                  1. Add supplyMinusNum to income
                  1. Subtract amount in index of "name" to bought in index of "name"
1. If: Exit
      1. Print income
      1. Reprint Supply Check
      1. Terminate Program, no longer looping
11. Loop back to choose mode
