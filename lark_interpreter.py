class LarkLarkInterpreter:
    def __init__(self):
        self.environment = {}
        self.functions = {}

    def execute(self, node):
        # Handle leaf nodes (numeric values)
        if isinstance(node, (int, float)):
            return node
        
        # Handle transformed nodes (tuples)
        if isinstance(node, tuple):
            nodetype, *args = node
            
            if nodetype == 'assign_var':
                var_name, value = args
                self.environment[var_name] = self.execute(value)
            elif nodetype == 'print_expr':
                expr, = args
                print(self.execute(expr))
            elif nodetype == 'var':
                var_name, = args
                return self.environment[var_name]
            elif nodetype == 'add':
                left, right = args
                return self.execute(left) + self.execute(right)
            elif nodetype == 'sub':
                left, right = args
                return self.execute(left) - self.execute(right)
            elif nodetype == 'for_loop':
                var_name, count, body = args
                for i in range(int(self.execute(count))):
                    self.environment[var_name] = i
                    self.execute(body)
            elif nodetype == 'func_def':
                func_name, params, body = args
                self.functions[func_name] = (params, body)
            elif nodetype == 'func_call':
                func_name, *params = args
                func_params, body = self.functions[func_name]
                original_env = self.environment.copy()
                self.environment.update(zip(func_params, params))
                result = self.execute(body)
                self.environment = original_env
                return result
            # Add more cases for other AST node types
            else:
                raise NotImplementedError(f"Unknown node type: {nodetype}")
        else:
            raise ValueError(f"Unexpected node format: {node}")

    def run(self, ast):
        # Execute the transformed AST (expected to be a list of top-level statements)
        for node in ast.children:
            self.execute(node)
