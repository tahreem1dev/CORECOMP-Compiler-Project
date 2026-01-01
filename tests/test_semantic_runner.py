# test_semantic_runner.py
from lexer.lexer import lexer
from parser.parser import CoreParser
from semantic.semantic import semantic_analyzer

test_files = [
    'tests/sample_correct.core',
    'tests/sample_redeclare.core',
    'tests/sample_undeclared.core',
    'tests/sample_typemismatch.core'
]

def run_test(file_name):
    with open(file_name,'r') as f:
        source = f.read()

    lx = lexer(source)
    tokens = lx.tokenize()

    # print tokens for debug
    #print([(t.type,t.value) for t in tokens])

    ps = CoreParser(tokens)
    tree = ps.parse()

    sa = semantic_analyzer(tree)
    try:
        sa.check_semantics()
        print(f"{file_name}: semantic check passed")
    except Exception as e:
        print(f"{file_name}: {e}")

for tf in test_files:
    run_test(tf)

