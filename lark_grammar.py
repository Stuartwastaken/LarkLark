lark_lark_grammar = f"""
start: (_WS? stmt _WS?)+

stmt: "tweet" NAME "=" expr                         -> assign_var      // Variable assignment
    | "chirp" expr                                  -> print_expr      // Print expression
    | "caw" NAME "squack" expr _WS? LCURLY stmt+ RCURLY  -> for_loop    // For loop
    | "screech" expr "mew" (stmt |  LCURLY stmt+ RCURLY   )               -> if_stmt         // If statement
    | "quack" expr                                  -> input_expr      // Input expression
    | "chirr" NAME "(" param_list? ")" LCURLY stmt+ RCURLY     -> func_def        // Function definition
    | func_call                                     -> stmt_func_call  // Use func_call as a statement

expr: NUMBER                                        -> number
    | NAME                                          -> var
    | expr "+" expr                                 -> add
    | expr "-" expr                                 -> sub
    | expr "*" expr                                 -> mul
    | expr "/" expr                                 -> div
    | expr "==" expr                                -> eq
    | func_call                                     -> func_expr       // Use func_call as an expression

func_call: "hoot" NAME "(" (expr ("," expr)*)? ")"  // Define func_call as a separate rule

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