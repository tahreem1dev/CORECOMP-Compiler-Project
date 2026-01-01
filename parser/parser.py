# parser.py
# CoreLang parser
# builds parse tree for declarations and assignments

class parse_node:
    def __init__(self, type, children=None):
        self.type = type
        self.children = children if children else []

    def __str__(self):
        return f"{self.type}: {[str(c) for c in self.children]}"

class CoreParser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def eat(self, type=None):
        tok = self.current()
        if tok is None:
            return None
        if type and tok.type != type:
            raise Exception(f"syntax error: expected {type} line {tok.line}")
        self.pos += 1
        return tok

    def parse(self):
        root = parse_node('program')
        while self.current() is not None:
            tok = self.current()

            # variable declaration
            if tok.value in ['int', 'float']:
                type_node = parse_node(tok.value)
                self.eat()
                next_tok = self.current()
                if next_tok:
                    var_node = parse_node(next_tok.value)
                    self.eat()
                    type_node.children.append(var_node)
                root.children.append(type_node)

            # assignment
            elif tok.type == 'IDENTIFIER' and self.pos + 2 < len(self.tokens):
                next_tok = self.tokens[self.pos + 1]
                rhs_tok = self.tokens[self.pos + 2]
                if next_tok.value == '=':
                    assign_node = parse_node('=')
                    lhs_node = parse_node(tok.value)
                    if rhs_tok.type in ['INT_LITERAL','FLOAT_LITERAL']:
                        rhs_node = parse_node('int' if rhs_tok.type=='INT_LITERAL' else 'float')
                    else:
                        rhs_node = parse_node(rhs_tok.value)
                    assign_node.children.append(lhs_node)
                    assign_node.children.append(rhs_node)
                    root.children.append(assign_node)
                    self.pos += 3
                    continue
                else:
                    root.children.append(parse_node(tok.value))
                    self.eat()
            else:
                root.children.append(parse_node(tok.value))
                self.eat()
        return root
