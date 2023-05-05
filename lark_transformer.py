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

    def for_loop(self, args):
        var_name, count, _, body, _ = args  
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
        params = args[1:]  # Get all the remaining arguments as a list
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
