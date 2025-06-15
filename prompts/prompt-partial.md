# Baseline Conventions

## Universal Engineering Principles

* **Code is communication** — optimise for the next human reader.
* **Simple Design Heuristics** — guiding principles, not iron laws; consult the user when you need to break them.
  1. **All tests pass** — correctness is non‑negotiable.
  2. **Reveals intent** — code should read like an explanation.
  3. **No *****knowledge***** duplication** — avoid multiple spots that must change together; identical code is only a smell when it hides duplicate *decisions*.
  4. **Minimal entities** — remove unnecessary indirection, classes, or parameters.
* **Small, safe increments** — single‑reason commits; avoid speculative work (**YAGNI**).
* **Tests are the executable spec** — red first, green always; test behaviour not implementation.
* **Compose over inherit**; favour pure functions where practical, avoid side-effects.
* **Functional core, imperative shell** — isolate pure business logic from I/O and side effects; push mutations to the system boundaries, build mockable gateways at those boundaries.
* **Psychological safety** — review code, not colleagues; critique ideas, not authors.
* **Version‑control etiquette** — descriptive commit messages, branch from `main`, PRs require green CI.

---

Your goal:

Make me a python module that can manage a list of tasks.