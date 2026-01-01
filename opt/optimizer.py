# optimizer.py
# Optimization Phase for CoreLang ICG
# simple optimizations: constant folding & redundant assignment removal

import re

class optimizer:
    def __init__(self, icg_code):
        self.icg_code = icg_code
        self.optimized_code = []

    def is_constant(self, val):
        return re.match(r'^\d+(\.\d+)?$', val)

    def optimize(self):
        constants = {}  # track known constant values

        for instr in self.icg_code:
            # split instruction: lhs = rhs
            if '=' in instr:
                lhs, rhs = [x.strip() for x in instr.split('=')]

                # constant folding: rhs is simple expression with +,-,*,/ and constants
                if any(op in rhs for op in ['+','-','*','/']):
                    # replace known constants
                    for var, val in constants.items():
                        rhs = re.sub(r'\b'+var+r'\b', val, rhs)

                    # evaluate if rhs is now fully numeric
                    try:
                        value = str(eval(rhs))
                        rhs = value
                        constants[lhs] = value
                    except:
                        pass
                elif self.is_constant(rhs):
                    constants[lhs] = rhs  # record constant
                else:
                    if rhs in constants:
                        rhs = constants[rhs]  # replace variable with known constant

                # skip redundant assignment: lhs = lhs
                if lhs == rhs:
                    continue

                self.optimized_code.append(f"{lhs} = {rhs}")

        return self.optimized_code
