# Static Code Analysis — Reflection

### 1. What is static code analysis, and why is it useful?

Static code analysis examines source code without executing it. It helps identify potential bugs, insecure coding patterns, and style violations early in development.

### 2. What did Pylint, Bandit, and Flake8 identify?

Pylint identified code-quality issues such as a mutable default argument, missing docstrings, naming violations, and unused variables. Bandit identified potentially insecure uses of `eval()`, MD5, predictable random numbers, broad exception handling, and shell execution. Flake8 identified formatting problems and unused code.

### 3. Which fixes were most important?

Removing `eval()` and shell command execution was important for security. Replacing MD5 with SHA-256 and using `secrets` for checkout PIN generation improved the relevant security properties. Fixing the mutable default argument and broad exception handling improved maintainability and reliability.

### 4. What did you learn from this lab?

The three tools serve different purposes and complement one another. Static analysis can identify issues before execution, but the findings must be interpreted and the changes verified. Running the tools again confirmed that the corrected program reached a Pylint score of 10.00/10, with no Bandit or Flake8 findings.
