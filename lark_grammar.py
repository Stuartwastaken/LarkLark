lark_lark_grammar = f"""
start: (_WS? stmt _WS?)+

stmt: "tweet" NAME "=" expr                         -> assign_var      // Variable assignment
    | "chirp" expr                                  -> print_expr      // Print expression
    | "caw" NAME "squack" expr _WS? LCURLY stmt+ RCURLY  -> for_loop    // For loop
    | "screech" expr "mew" stmt                     -> if_stmt         // If statement
    | "quack" expr                                  -> input_expr      // Input expression
    | "chirr" NAME "(" param_list? ")" LCURLY stmt+ RCURLY     -> func_def        // Function definition
    | "hoot" NAME "(" (expr ("," expr)*)? ")"       -> func_call       // Function call

expr: NUMBER                                        -> number
    | NAME                                          -> var
    | expr "+" expr                                 -> add
    | expr "-" expr                                 -> sub
    | expr "*" expr                                 -> mul
    | expr "/" expr                                 -> div

param_list: NAME ("," NAME)*

LCURLY: "{{"
RCURLY: "}}"

%import common.CNAME -> NAME
%import common.NUMBER
%import common.WS_INLINE
%ignore WS_INLINE
%ignore _WS

_WS: (" " | "\\n" | "\\t")+
"""
