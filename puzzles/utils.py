import ast
import re

def solve_math_problem(question):
    if not re.match(r"^[\d\s\+\-\*\/\(\)]+$", question):
        raise ValueError ('Invalid characters  in the problem')
    
    try: 
        result = eval(question)
    except Exception as e:
        raise ValueError(f'Error solving problem {e}')
    return result