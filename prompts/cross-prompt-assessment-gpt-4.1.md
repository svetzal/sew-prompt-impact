| Prompt Style | Key Features of the Prompt | Key Features of the Output | Strengths                              | Weaknesses                            |
|--------------|----------------------------|----------------------------|----------------------------------------|----------------------------------------|
| Fancy        | • Comprehensive guidelines (naming, style, type coverage, Pydantic, etc.)<br>• Strong emphasis on universal engineering principles<br>• Detailed constraints (e.g., max line length, cyclomatic complexity) | • Provides Pydantic-based model<br>• Thorough docstrings and type hints<br>• Follows black/flake8 standards<br>• Very structured code architecture | • Highly professional output<br>• Clear code style and docstrings<br>• Enforces robust coding conventions | • Potential overengineered approach for small tasks<br>• Setup for linting and formatting can be too detailed for a quick solution |
| Medium       | • Focus on universal principles but less detail than Fancy<br>• Encourages simple design and testable code<br>• No explicit mention of type coverage or linting | • Uses dataclasses for tasks<br>• Clear, minimal OOP approach<br>• Basic in-code quick tests<br>• No advanced validation libraries | • Straightforward code<br>• Uses standard library (dataclasses)<br>• Easy to extend | • Lacks advanced validation<br>• Less formal coverage for linting/type hints |
| Plain        | • Very minimal constraints<br>• Simple instructions: “Make me a python module…”<br>• No real style or linting recommendations | • Basic Python OOP structure<br>• Adds JSON-based persistence<br>• No strict type hints<br>• Flexible approach | • Quick to integrate in small projects<br>• Easy for beginners to understand | • No formal type hints or linting checks<br>• Inconsistent coding style and docstrings |

---

## Qualitative Analysis

1. Which prompt style gives the best results overall?

   • The “fancy” prompt style produces the most thorough and polished code. It includes robust features like type hints, docstrings, and compliance with guidelines such as black, flake8, and mypy. It also integrates Pydantic for validation. This makes it strong in professional settings where consistency, clarity, and correctness are paramount.  
   • The “medium” style is a good balance of simplicity and clarity. Its code is relatively minimal yet adheres to many of the “fancy” style’s design principles.  
   • The “plain” style is quickest to understand and implement but lacks the more advanced features (type safety, thorough docstrings, validation).

2. What aspects of the model's response differ between the different prompt styles?

   • Tooling and advanced Python features:  
     – “Fancy” uses Pydantic for model validation and type annotations throughout.  
     – “Medium” uses only standard library dataclasses.  
     – “Plain” uses basic Python classes without dataclasses or type hints.  
   • Style guidelines and thoroughness:  
     – “Fancy” is explicit about linting, formatting, and universal engineering principles.  
     – “Medium” mentions universal engineering principles but does not explicitly apply style tools.  
     – “Plain” does not invoke these styling or testing tools at all.  
   • Testing approach:  
     – “Fancy” references tests as the “executable spec” (though not fully provided).  
     – “Medium” includes some inline tests under a main guard.  
     – “Plain” also includes a quick usage example but not structured tests.  

3. What aspects of the model's response are consistent across all prompt styles?

   • All include basic task management functionality (adding tasks, removing tasks, marking tasks done, listing tasks).  
   • All provide a straightforward, object-oriented approach to encapsulate tasks and a task manager.  
   • All maintain some sense of clarity around the “purpose” of the code, aiming to keep it easy to extend or integrate.  

Overall, each style successfully delivers a functional “tasks” module. The main differences lie in code sophistication, the integration of best practices and standards, and the adoption of advanced tooling.