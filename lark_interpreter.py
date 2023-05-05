class LarkLarkInterpreter:
    def __init__(self):
        self.environment = {}
        self.functions = {}

    def execute(self, node):
        if isinstance(node, (int, float)):
            return node
        
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
                func_name, param_list, body = args
                self.functions[func_name] = (param_list, body)
            elif nodetype == 'func_call':
                func_name, params = args
                func_params, body = self.functions[func_name]
                original_env = self.environment.copy()
                params_values = [self.execute(p) for p in params]
                self.environment.update(zip(func_params, params_values))
                self.execute(body)
                self.environment = original_env
            elif nodetype == 'if_stmt':
                condition, stmt = args
                if self.execute(condition):
                    self.execute(stmt)
            elif nodetype == 'input_expr':
                prompt, = args
                return input(prompt)
            elif nodetype == 'string':
                return str(node)
            else:
                raise NotImplementedError(f"Unknown node type: {nodetype}")
        else:
            raise ValueError(f"Unexpected node format: {node}")

    def run(self, ast):
        for node in ast:
            self.execute(node)
