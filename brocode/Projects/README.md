## **Project 1: Task Manager CLI (CRUD in terminal)**

**Estimated time**: 1–2 days
**Goal**: Build a CLI tool to manage tasks (add, list, update, delete, mark as done). Save data in a `.json` file.

### Topics to practice:

* Functions & classes
* File I/O with `json` and `pathlib`
* Basic use of `os`
* Command-line or interactive input
* Assertions and simple testing (`assert`, `unittest` or `pytest`)
* Optional: `dict` comprehension for filtering or task display

### Structure suggestion:

```
project/
├── main.py
├── task_manager.py
├── models.py         # Task class
├── storage.py        # JSON handling
├── utils.py
├── data/
│   └── tasks.json
└── tests/
    └── test_task_manager.py
```

---

## **Project 2: Unit Converter CLI**

**Estimated time**: 1 day
**Goal**: CLI tool for converting between units like °C/°F, km/mi, s/min, etc.

### Topics to practice:

* `lambda` for conversion functions
* `dict` and `dict comprehensions`
* Input handling (interactive or `argparse`)
* Basic use of `assert`
* Optional: CLI interface with `argparse`

### Example structure:

```
project/
├── main.py
├── converters.py     # temperature, length, time, etc.
└── tests/
    └── test_converters.py
```

---

## **Project 3: Health & Fitness Calculator**

**Estimated time**: 1–2 days
**Goal**: A terminal app where the user enters age, height, weight, sex, and activity level. The program calculates BMI, classification, BMR, and estimated calorie needs.

### Topics to practice:

* Functions and optional `User` class
* `lambda` for BMI category logic
* `dict comprehension` for mapping activity levels or ranges
* Input validation using `assert`
* Testing with `unittest` or `pytest`

### Structure suggestion:

```
project/
├── main.py
├── health.py         # All logic for calculations
├── models.py         # Optional: User class
└── tests/
    └── test_health.py
```

---

## **Project 4: File Finder with Filters (CLI)**

**Estimated time**: 1–2 days
**Goal**: A command-line tool that recursively finds files in directories with filters like extension, min/max size, or name pattern.

### Topics to practice:

* `os`, `pathlib` for file and directory operations
* CLI arguments via `argparse`
* Optional class to manage filters
* File metadata handling
* Assertions and unit testing

### Structure suggestion:

```
project/
├── main.py
├── finder.py         # Scanning logic
├── filters.py        # Optional class or helpers
└── tests/
    └── test_finder.py
```

---

## **Project 5: Mini-Grep (Text Search Tool)**

**Estimated time**: 1 day
**Goal**: Build a simple CLI tool that searches for lines matching a string or regex inside `.txt` or `.log` files.

### Topics to practice:

* File reading (`open()`, with `try/except`)
* Line-by-line processing
* Regex with the `re` module (`re.search`, `re.match`)
* Basic use of `os` or `pathlib` to find files
* CLI arguments with `argparse`
* Optional: colored output with `colorama` or ANSI escape codes

---

### Features (start small, then expand):

* Search for a keyword in a single file
* Support for case-insensitive search (`-i`)
* Optional: support basic regex
* Bonus: recursively search files in a folder (like `grep -r`)

---

### 🔧 Suggested structure:

```
project/
├── main.py           # CLI entry point
├── grep.py           # Core search logic
├── utils.py          # Optional helpers (e.g., highlighting matches)
└── tests/
    └── test_grep.py
```

---


