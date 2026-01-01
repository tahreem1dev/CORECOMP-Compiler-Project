# semantic.py
# semantic analyzer
# handles declarations, assignments, type checking

class symbol_table:
    def __init__(self):
        self.scopes = [{}]

    def enter_scope(self):
        self.scopes.append({})

    def exit_scope(self):
        self.scopes.pop()

    def declare(self, name, type, line):
        if name in self.scopes[-1]:
            raise Exception(f"semantic error: redeclaration of '{name}' line {line}")
        self.scopes[-1][name] = type

    def lookup(self, name, line):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        raise Exception(f"semantic error: undeclared variable '{name}' line {line}")

class semantic_analyzer:
    def __init__(self, parse_tree):
        self.tree = parse_tree
        self.symbols = symbol_table()

    def check_semantics(self):
        self.visit(self.tree)

    def visit(self, node):
        if node.type in ['int', 'float']:
            if node.children:
                var_node = node.children[0]
                self.symbols.declare(var_node.type, node.type, 0)

        elif node.type == '=':
            if len(node.children) == 2:
                lhs_name = node.children[0].type
                rhs = node.children[1]

                lhs_type = self.symbols.lookup(lhs_name, 0)

                if rhs.type in ['int','float']:
                    rhs_type = rhs.type
                else:
                    rhs_type = self.symbols.lookup(rhs.type, 0)

                if lhs_type != rhs_type and not (lhs_type=='float' and rhs_type=='int'):
                    raise Exception(f"semantic error: type mismatch for '{lhs_name}'")

        for child in getattr(node, 'children', []):
            self.visit(child)
