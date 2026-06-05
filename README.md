# Topic 06: Loops and Functions

**Week 3 | CIS Intro to Programming**

---

## Overview

This week combines two powerful tools: loops and functions. The starter code gives you a working structure to build from. Your job is to extend it with your own logic.

## Assignment Prompt

Starting from the starter code below, build a program that uses both a loop and at least one function. Your finished program should:

- Define at least one function with a clear, descriptive name
- Call that function at least once
- Use a loop (`for` or `while`) to repeat an action
- Produce output that clearly shows the loop and function working together

## Starter Code

Copy the code below into a file named `solution.py` in your forked repository.

```python
# Topic 06 Collaborative Assignment
# Your Name:
# Date:

# --- STARTER CODE ---
# This function takes a number and returns its square.
def square(n):
    return n * n

# This loop calls the function for numbers 1 through 5.
for i in range(1, 6):
    result = square(i)
    print(i, "squared is", result)

# --- YOUR EXTENSION BELOW THIS LINE ---
# Ideas: Write a second function, change the range,
# change what the function does, or add a while loop
# that lets the user keep entering numbers until they type "quit".
```

## Peer Review Prompt

When reviewing a classmate's code this week, consider:

- Is their function doing one clear thing, or is it trying to do too much?
- Is the loop easy to follow?
- Could the function be reused somewhere else in a larger program?

## Submission Instructions

1. Fork this repository into your own GitHub account.
2. Write your code and commit it to your fork.
3. Submit your repo link using the **Submit Your Repo Link** form in Blackboard.
4. Open the **Class Repo Directory** in Blackboard and find two classmates' repos.
5. Leave a GitHub Issue on each with substantive feedback using the peer review prompt above as your guide.

## Notes

After this week, the training wheels come off. Starting with Topic 08, assignments will be open-ended with just a prompt and a peer review question. This week is your last with a starter to lean on — use it, but push yourself to extend it into something that feels like your own.
