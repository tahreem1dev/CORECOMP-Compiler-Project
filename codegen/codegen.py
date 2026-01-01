# codegen.py
# Code Generation Phase for CORECOMP
# Input: Optimized ICG
# Output: Python pseudo code / final executable representation

class code_generator:
    def __init__(self, icg_code):
        self.icg_code = icg_code
        self.output_code = []

    def generate(self):
        """
        Convert 3-address code to Python-like pseudo code
        """
        for instr in self.icg_code:
            # simple replacement: ints/floats map directly
            # temp variables and variables remain as-is
            self.output_code.append(instr)
        return self.output_code
