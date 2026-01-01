# main.py
# CORECOMP main script
# runs lexer, parser, semantic analyzer, ICG, and Optimization

from lexer.lexer import lexer
from parser.parser import CoreParser
from semantic.semantic import semantic_analyzer
from icg.icg import icg_generator
from opt.optimizer import optimizer
from codegen.codegen import code_generator 

def run_compiler(file_path):
    # read source code
    with open(file_path, 'r') as f:
        source = f.read()

    print(f"\nCompiling file: {file_path}\n{'-'*40}")

    # 1️ Lexer
    lx = lexer(source)
    tokens = lx.tokenize()
    print("Tokens:")
    for t in tokens:
        print(f"type: {t.type}, value: {t.value}")

    # 2️ Parser
    ps = CoreParser(tokens)
    tree = ps.parse()
    print("\nParse tree generated.")

    # 3️ Semantic Analysis
    sa = semantic_analyzer(tree)
    try:
        sa.check_semantics()
        print("Semantic check passed")
    except Exception as e:
        print(f"Semantic Error: {e}")
        return  # stop compilation if semantic error

    # 4️ Intermediate Code Generation
    icg = icg_generator()
    icg.generate(tree)
    print("\nIntermediate Code (3-address):")
    for instr in icg.get_code():
        print(instr)

    # 5️ Optimization
    opt = optimizer(icg.get_code())
    optimized_code = opt.optimize()
    print("\nOptimized Intermediate Code:")
    for instr in optimized_code:
        print(instr)

        # 6️ Code Generation
    cg = code_generator(optimized_code)
    final_code = cg.generate()
    print("\nFinal Generated Code (Python pseudo code):")
    for line in final_code:
        print(line)

if __name__ == "__main__":
    
    run_compiler('tests/sample_correct.core')
