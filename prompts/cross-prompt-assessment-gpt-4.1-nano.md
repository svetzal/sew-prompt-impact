| Prompt Style | Approach & Key Features                                                                                               | Strengths                                                                                         | Weaknesses                                                                                |
|--------------|-----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| fancy        | • Class-based OOP with a Task model (pydantic) and TaskManager. <br> • Full type hints, docstrings, and next ID tracking. <br> • Provides CRUD methods and filtering. | • Comprehensive design with validation (pydantic). <br> • Clear docstrings and type coverage. <br> • Easy to extend and maintain. | • Slightly verbose for smaller use cases. <br> • Requires pydantic dependency.             |
| medium       | • Functional style with a frozen dataclass Task. <br> • Separate pure functions for add, remove, toggle, list. <br> • Includes thorough unittest test suite.           | • Good test coverage demonstrating best practices. <br> • Clear separation of concerns. <br> • Immutable data model.               | • Requires a separate test file for quick usage. <br> • May need additional validation logic. |
| plain        | • Single-file, class-based approach. <br> • Basic Task class storing description/completion status. <br> • Methods for add, remove, complete, list.                   | • Very straightforward, minimal dependencies. <br> • Easy to integrate quickly in small projects.  | • No explicit tests included. <br> • Lacks type hints and more robust validation.          |

---

## Extended Qualitative Analysis

1) Which prompt style gives the best results overall?  
   • The "fancy" prompt yields the most thorough and well‑structured solution, featuring pydantic for validation, comprehensive type hints, docstrings, and a clear OOP design. If a user values correctness, extensibility, and clarity in a larger project, the "fancy" approach stands out.  
   • However, the "medium" prompt also offers strong benefits, especially its focus on a purely functional style, an immutable data model, and a proper test suite for continuous integration. This approach can be considered equally robust from a software‑engineering perspective.  
   • If the goal is to get a quick, minimal solution without setup overhead, or for a short demo, the "plain" prompt is enough.

2) What aspects of the model's response differ between the different prompt styles?  
   • Code architecture:  
     – "fancy" uses a more OOP‑centric approach combined with pydantic’s data validation.  
     – "medium" emphasizes functional purity and testing.  
     – "plain" presents a straightforward, single‑file solution without advanced features.  
   • Testing:  
     – "medium" includes a dedicated unittest module, demonstrating more rigorous testing.  
     – "fancy" includes some docstring coverage and an OOP approach but doesn’t show explicit tests.  
     – "plain" has example usage within the same file, rather than a separate test suite.  
   • Validation and type usage:  
     – "fancy" has complete type hints and uses pydantic.  
     – "medium" uses standard type hints, a frozen dataclass for immutability, but no external libraries.  
     – "plain" omits explicit type hints.  

3) What aspects of the model's response are consistent across all prompt styles?  
   • Core functionality is the same, providing a means to add, remove, and mark tasks as completed, as well as listing tasks.  
   • All outputs demonstrate straightforward, readable Python code.  
   • Each style is designed to be easily understandable and modifiable according to the user’s needs.