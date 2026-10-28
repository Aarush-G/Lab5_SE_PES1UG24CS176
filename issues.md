# Static Code Analysis — Issue Log

| Issue | Type | Original location | Description | Fix approach |
|---|---|---|---|---|
| Unsafe `eval()` | Security | `calculateDiscountedTotal`, line 44 | Evaluating an expression string can execute arbitrary code. | Replaced expression evaluation with a validated numeric discount rate. |
| Weak MD5 hash | Security | `generateItemHash`, line 49 | MD5 is unsuitable for security-sensitive hashing. | Replaced MD5 with SHA-256. |
| Shell command execution | Security | `exportCartReceipt`, line 60 | `os.system()` with a constructed command can allow shell injection. | Removed shell execution and used `print()` for confirmation. |
| Predictable checkout PIN | Security | `generateCheckoutPin`, line 53 | Standard pseudorandom generation is unsuitable for security-sensitive PINs. | Used Python's `secrets` module to generate a cryptographically secure PIN. |
| Mutable default argument | Code quality | `addItemToCart`, line 15 | A mutable list used as a default argument can be shared across function calls. | Changed the default to `None` and append to the audit log only when one is provided. |
| Broad exception handling | Code quality | `removeItemFromCart`, line 28 | A bare `except` can hide unexpected errors. | Check whether the item exists before removing it. |
| Unused imports and variables | Code quality | Multiple locations | Unused code reduces readability and triggers warnings. | Removed unused imports and variables. |
| Naming and documentation | Style | Multiple locations | Function names and missing docstrings violated conventions. | Adopted snake_case names and added docstrings. |
| File handling and formatting | Style | Multiple locations | File encoding, resource handling, whitespace, and line-length issues were reported. | Used a context manager, explicit UTF-8 encoding, and corrected formatting. |

## Verification

- Original Pylint score: 3.86/10
- Final Pylint score: 10.00/10
- Original Bandit findings: 5
- Final Bandit result: No issues identified
- Original Flake8 violations: 7
- Final Flake8 result: No violations reported
