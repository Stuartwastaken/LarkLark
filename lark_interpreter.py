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
            elif nodetype == 'eq':
                left, right = args
                return self.execute(left) == self.execute(right)
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
                func_name = node[1]
                args = node[2]
                params, body = self.functions[func_name]
                # Bind parameter names to their corresponding argument values
                for param_name, arg_value in zip(params, args):
                    self.environment[param_name] = arg_value
                # Execute the function body
                return self.execute(body)
            elif nodetype == 'if_stmt':
                condition, body = args
                if self.execute(condition):
                    self.execute(body)
            else:
                raise NotImplementedError(f"Unknown node type: {nodetype}")
        else:
            raise ValueError(f"Unexpected node format: {node}")

    def run(self, ast):
        for node in ast:
            self.execute(node)
