# Implementation of Finite Automata

This project contains an interactive Jupyter notebook that demonstrates and implements deterministic (DFA) and nondeterministic (NFA) finite automata in detail.

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Notebook Structure](#notebook-structure)
5. [Features](#features)
6. [Contributing](#contributing)
7. [License](#license)

## Introduction

Automatons.ipynb is a comprehensive educational and experimental tool that helps understand and practice the concepts and operations of finite automata. The notebook is interactive, allowing users to directly run the code, modify examples, and see results in real-time.

## Installation

To install the dependencies required to run the project, follow these steps:

1. Install uv if it's not already installed:
   ```
   pip install uv
   ```

2. Clone the repo:
   ```
   git clone https://github.com/wolgyes/formal_languages
   ```

3. Enter the project directory:
   ```
   cd finite-automata
   ```

4. Create a virtual environment and install the dependencies:
   ```
   uv venv
   source .venv/bin/activate  # On Unix systems
   # or
   .venv\Scripts\activate  # On Windows systems
   
   uv pip install -r requirements.txt
   ```

## Usage

To start the notebook, activate the virtual environment and then run the following command:

```
jupyter notebook Automatons.ipynb
```

## Notebook Structure

1. **Introduction and Imports**
   - Importing necessary libraries

2. **Theoretical Background**
   - Comparison of DFA and NFA

3. **Implementations**
   - Automaton base class
   - DFA class
   - NFA class

4. **Testing and Examples**
   - Testing automata
   - Interactive examples
   - Visualization results

5. **Conclusion and Further Possibilities**

## Features

- Implementation of Deterministic and Nondeterministic Finite Automata
- Visualization of automata
- Word acceptance simulation
- Automata conversion (NFA to DFA)
- JSON import/export functions

## Contributing

If you'd like to contribute to the project, please open an issue or send a pull request.

## License

This project is licensed under the [MIT License](LICENSE).