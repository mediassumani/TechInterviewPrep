# Technical Interview Preparation

### A problem-Solving Flow Chart from CTCI

1. Listen (write down important information about the question)
2. Example
3. Brute Force
4. Optimize
5. Walk Through
6. Implement 
7. Test

### Listen

  * Listen very carefully to the question being asked.
  * Make sure you have captured important informations(mentally or writting them down)
  * Listen to keywords such as "sorted" as it might be helful on solving the problem.
  * If you find yourself stuck, make sure to refer back to the information you wrote down.
  
  
### Draw an example

  * An example helps you visualize a question.
  * Example needs to be specific. Should use real numbers or strings(if applicable to the problem)
  * Example needs to be sufficiently large.
  * Example should not be a special case at first.
  

### State a brute force

  * Find a brute force. State it even if it's not optimal.
  * Explain its space and time complexity.
  * It is a great starting point since it helps you get a bigger idea of the problem/solution.
  

### Optimize

  * Look for any unused information. Is the array sorted? use that to improve the brute force
  * Use a fresh diffrent example to view things from a different perspective.
  * Make time vs space tradeoff. Ask your interviewer which needs to be prioritize.
  * Precompute information. Is there a way to reoganize the data beforehand that will save time afterwards?

### Walk through

  * After you've got your algorithm, don't just straight into coding.
  * Take a moment to solidigy your understanding of the algorithm.
  * Make sure to know the variables are and when they change

### Implement

  * Now that you have a good understanding, start coding.
  * If white board, start coding from the far top left
  * Write beautiful code.
  * Error checks.
  * Use other helper funtions, classes/structs or at least pretend they're there and you'll fill the details later.

### Test

  * Should not submit(or say you're done) your code without testing it.
  * Start with a conceptual test - walking through your code line by line and explaining it to the interviewer.
  * Hot spots - base case in recursive code, integer divition, Null nodes in Binary Trees.
  * Test cases - Now use an actual, specific test for the code. Use a small one to be faster to check.
  * Special cases - Test the code against Null, empty, or single element values, the extreme cases, etc...
