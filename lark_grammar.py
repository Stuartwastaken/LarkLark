lark_lark_grammar = f"""
start: (_WS? stmt _WS?)+

stmt: "tweet" NAME "=" expr                          -> assign_var      // Variable assignment
    | "chirp" expr                                   -> print_expr      // Print expression
    | "caw" NAME "squack" expr _WS? LCURLY stmt+ RCURLY  -> for_loop    // For loop
    | "screech" expr COMP_OP expr "mew" _WS? LCURLY stmt+ RCURLY -> if_stmt   // If statement
    | "quack" STRING                                 -> input_str_expr  // Input string expression
    | "chirr" NAME "(" param_list? ")" LCURLY stmt+ RCURLY     -> func_def        // Function definition
    | "hoot" NAME "(" (expr ("," expr)*)? ")"        -> func_call       // Function call

expr: NUMBER                                         -> number
    | STRING                                         -> string
    | NAME                                           -> var
    | expr "+" expr                                  -> add
    | expr "-" expr                                  -> sub
    | expr "*" expr                                  -> mul
    | expr "/" expr                                  -> div
    | "hoot" NAME "(" (expr ("," expr)*)? ")"        -> func_call       // Function call

param_list: NAME ("," NAME)*

LCURLY: "{{"
RCURLY: "}}"

COMP_OP: "==" | "!=" | "<" | ">" | "<=" | ">="

%import common.CNAME -> NAME
%import common.NUMBER
%import common.ESCAPED_STRING -> STRING
%import common.WS_INLINE
%ignore WS_INLINE
%ignore _WS

_WS: (" " | "\\n" | "\\t")+
"""
