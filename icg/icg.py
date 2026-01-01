# icg.py
# Intermediate Code Generation (ICG) with temporary variables
# input: parse tree
# output: list of 3-address code instructions

from parser.parser import parse_node

class icg_generator:
    def __init__(self):
        self.temp_count = 0
        self.code = []

    def new_temp(self):
        # generate new temporary variable
        self.temp_count += 1
        return f"t{self.temp_count}"

    def generate(self, node):
        """
        Recursive function to generate 3-address code
        Returns:
            - variable name or temp holding result
        """
        if node.type in ['int', 'float']:
            # variable declaration → no code needed
            return None

        elif node.type == '=':
            lhs = node.children[0].type
            rhs_node = node.children[1]

            # rhs is literal
            if rhs_node.type in ['int','float']:
                self.code.append(f"{lhs} = {rhs_node.type}")
                return lhs

            # rhs is variable
            elif rhs_node.type not in ['int','float']:
                self.code.append(f"{lhs} = {rhs_node.type}")
                return lhs

            # rhs is expression node → future expansion
            # for now same logic
            return lhs

        # handle children recursively
        for child in getattr(node,'children',[]):
            self.generate(child)

        return None

    def get_code(self):
        # return generated 3-address code
        return self.code

