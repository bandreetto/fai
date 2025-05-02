# FAI

> Use flanker nucleotides to predict A-site location in ribosome profiling data

[![CI](https://github.com/bandreetto/fai/actions/workflows/ci.yml/badge.svg)](https://github.com/bandreetto/fai/actions/workflows/ci.yml)

---

## 🚀 Quickstart

1. **Clone & enter**

   ```bash
   git clone https://github.com/your-user/fai.git
   cd fai
   ```

2. **Create & activate the virtual environment**

   ```bash
   uv venv
   # macOS/Linux
   source .venv/bin/activate
   # Windows (PowerShell)
   .\.venv\Scripts\Activate.ps1
   ```

3. **Install runtime & dev tools**

   ```bash
   uv pip install -r pyproject.toml --extra dev
   uv pip install -e .
   ```

4. **Enable pre-commit hooks**

   ```bash
   pre-commit install
   ```

   Now `black` and `ruff` will run automatically on each commit.

---

## 🧑‍💻 Usage Examples

### REPL

```python
>>> from fai import add_numbers
>>> add_numbers(2, 3)
5
```

TODO: *(Replace with actual functions)*

---

## ✅ Testing

Run all tests:

```bash
pytest
```

- Pytest will discover any `tests/test_*.py` files  
- Execute all `test_*()` functions  
- Report pass/fail summary

---

## 🎨 Formatting & Linting

- **Check formatting**:

  ```bash
  black --check .
  ```

- **Apply formatting**:

  ```bash
  black .
  ```

- **Lint code**:

  ```bash
  ruff check .
  ```

These also run on each commit via `pre-commit`.

---

## 📦 Dependencies

- **Runtime**: defined under `[project].dependencies` in `pyproject.toml`  
- **Dev tools**: under `[project.optional-dependencies.dev]` (pytest, black, ruff, pre-commit)

When you add a new dependency:

1. `uv pip install <package>`  
2. Add it manually to `pyproject.toml`  
3. Re-run `uv pip install -r pyproject.toml --extra dev`
