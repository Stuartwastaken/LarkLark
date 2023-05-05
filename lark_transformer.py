from lark import Transformer, Token

class LarkLarkTransformer(Transformer):
    def start(self, args):
        return args

    def stmt(self, args):
        return args[0]

    def assign_var(self, args):
        var_name, value = args
        return ('assign_var', str(var_name), value)

    def print_expr(self, args):
        return ('print_expr', args[0])
    
    def eq(self, args):
        return ('eq', args[0], args[1])
    
    def stmt_func_call(self, args):
        return args[0]
    
    def if_stmt(self, args):
        condition = args[0]
        body = args[1] if len(args) == 2 else args[2]  # Handle the case where the body is enclosed in curly braces
        if isinstance(body, list):
            body = body[0]
        return ('if_stmt', condition, body)
    
    def func_expr(self, args):
        return args[0]

    def for_loop(self, args):
        var_name, count = args[0], args[1]
        body = args[2] if len(args) == 3 else args[3]  # Handle the case where the body is enclosed in curly braces
        return ('for_loop', str(var_name), count, body)

    def func_def(self, args):
        func_name = args[0]
        if len(args) == 4:
            params, body = [], args[2]
        else:
            params, body = args[1], args[3]
        param_list = [str(p) for p in params] if params else []
        return ('func_def', str(func_name), param_list, body)

    def func_call(self, args):
        func_name = args[0]
        params = args[1] if len(args) > 1 else []  # Get the parameters if they exist
        if not isinstance(params, list):  # Ensure that params is always a list
            params = [params]
        return ('func_call', str(func_name), params)

    def number(self, args):
        return float(args[0])

    def var(self, args):
        return ('var', str(args[0]))

    def add(self, args):
        return ('add', args[0], args[1])

    def sub(self, args):
        return ('sub', args[0], args[1])

    def param_list(self, args):
        return args

    def NAME(self, args):
        return Token('NAME', args[0])

    # Additional transformation methods can be added as needed
