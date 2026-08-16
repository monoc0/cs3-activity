# Annex C
Code Quality Assessment Worksheet

|Section|C#/Name|Date|
|----|----|----|
|9-Arayat|04-Bobila, **05-Caleon**, 06-Gusad|08/16/2026|

## QUESTIONS

1. Efficiency:

    Which algorithm is faster when the list of numbers is very large? Why?

    > *Algorithm 1 is faster because it uses one for loop and one if statement, while algorithm 2 uses twice as many.*

    |Question|PseudoCode 1| PseudoCode 2|
    |------|------|------|
    |Does the algorithm use one loop or two nested loops?|[1]|[2]|
    |Does the algorithm repeat work unnecessarily?|[X]|[✓]|
    |Which algorithm finishes in fewer steps?|[✓]|[X]|

2. Readability:

    Which algorithm is easier to understand at first glance? What makes it clearer?

    > *Algorithm 1, because there are multiple calculations in the same lines and nested loops inside Algorithm 2*

    |Question|PseudoCode 1| PseudoCode 2|
    |------|------|------|
    |Are variable names meaningful (e.g., max vs. bigger)?|[✓]|[✓]|
    |Is the logic simple or complicated?|[C]|[S]|
    |Are there fewer lines of code?|[✓]|[X]|

3. Maintainability:

    If you had to add a new feature (like finding both max and min), which algorithm would be easier to update? Why?

    >*Algorithm 1, because the code is shorter, more straightforward, and easier to  understand.*

    |Question|PseudoCode 1| PseudoCode 2|
    |------|------|------|
    |Is the structure straightforward?|[✓]|[X]|
    |Would adding new steps break the code easily?|[X]|[✓]|
    |Is there less chance of errors when updating?|[✓]|[X]|

4. Testability:

    Which algorithm is easier to test with different inputs? Why?

    > *Algorithm 1, because it doesn't use nested loops, which makes it simpler and easier to fix if an error occurs.*

    |Question|PseudoCode 1| PseudoCode 2|
    |------|------|------|
    |Can you test with small lists easily?|[✓]|[✓]|
    |Does the algorithm have fewer conditions to check?|[✓]|[X]|
    |Is the output predictable and clear?|[✓]|[✓]|

5. Security:

    Imagine the input list comes from a user. What should the algorithm check to avoid errors or misuse?

    > *The algorithm should check if the item is either a numerical value or not*

    |Question|PseudoCode 1| PseudoCode 2|
    |------|------|------|
    |Can you test with small lists easily?|[X]|[X]|
    |Does the algorithm have fewer conditions to check?|[X]|[X]|
    |Is the output predictable and clear?|[X]|[✓]|

6. Final Answer:

    Based on your answers from 1 to 5, which one is the better algorithm that you will use to solve the problem of finding the highest number? Why? Summarize your answer

    > *Algorithm 1, because compared to Algorithm 2, It is shorter, simpler, faster, Straightforward, does not do unnecessary steps, and has less conditions to check*