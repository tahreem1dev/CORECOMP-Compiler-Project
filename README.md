# CORECOMP – Mini Compiler Project

## Project Overview
CORECOMP is a fully functional mini compiler developed in Python for the Compiler Construction course.
It demonstrates the complete working of a compiler, from reading source code to producing output,
covering all major phases with clear logical checks and intermediate steps. 

This project uses a simple custom language named **CoreLang** and showcases how
programs are processed step by step in a real compiler workflow.

## Technologies & Tools
- **Language:** Python 3  
- **IDE:** Visual Studio Code  
- **OS:** Windows  
- No external Python libraries are required

## Features & Compiler Phases
CORECOMP implements the compiler phases in a simple and effective way:

1. **Lexical Analysis (Lexer)**  
   - Converts source code into tokens for parsing.

2. **Syntax Analysis (Parser)**  
   - Builds a parse tree and checks grammar.

3. **Semantic Analysis**  
   - Ensures logical correctness: variable declaration, redeclaration, type consistency.  
   - Uses a symbol table and provides semantic feedback.

4. **Intermediate Code Generation (ICG)**  
   - Generates three-address intermediate code for further processing.

5. **Code Optimization**  
   - Applies basic optimizations for cleaner intermediate/final code.

6. **Final Code Generation**  
   - Produces final target-level output from optimized intermediate code.

## Project Structure

  CORECOMP/
  │
  ├── lexer/ # Lexical analyzer
  ├── parser/ # Syntax analyzer
  ├── semantic/ # Semantic analyzer
  ├── icg/ # Intermediate code generator
  ├── optimizer/ # Code optimizer
  ├── codegen/ # Final code generator
  ├── tests/ # Test programs for semantic and other phase checks
  ├── main.py # Compiler driver (runs complete pipeline)
  └── README.md # Project overview & instructions

## How to Run
1. Open terminal in the **CORECOMP root folder**.  
2. Run the main compiler:
   ```bash
   python main.py

For semantic testing only:
python -m tests.test_semantic_runner

     


Output will show which test programs passed semantic checks and which failed.

## Sample Test Programs
- tests/sample_correct.core → Fully valid program
- tests/sample_redeclare.core → Checks variable redeclaration errors
- tests/sample_undeclared.core → Checks for undeclared variable usage
- tests/sample_typemismatch.core → Checks for type mismatch errors


## Project Status
- All compiler phases fully implemented and verified
- Lexical, syntax, semantic, intermediate code, optimization, and code generation phases working correctly
- Test programs cover redeclaration, undeclared variables, and type mismatch
- Project complete, functional, and ready for academic evaluation

## Key Highlights
- Developed for educational purposes, focusing on clarity and concept demonstration
- CoreLang syntax simple to highlight compiler construction principles
- Symbol tables, semantic validation, and intermediate code fully demonstrated
- Designed for easy understanding of compiler workflow



