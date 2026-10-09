import ast
import math
import operator


_ALLOWED_OPERATOR_MAP = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.MatMult: operator.matmul,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
    ast.Not: operator.not_,
    ast.Invert: operator.invert,
    ast.BitAnd: operator.and_,
    ast.BitOr: operator.or_,
    ast.BitXor: operator.xor,
    ast.LShift: operator.lshift,
    ast.RShift: operator.rshift,
}


def _build_function_map():
    functions = {
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "asin": math.asin,
        "acos": math.acos,
        "atan": math.atan,
        "atan2": math.atan2,
        "sinh": math.sinh,
        "cosh": math.cosh,
        "tanh": math.tanh,
        "asinh": math.asinh,
        "acosh": math.acosh,
        "atanh": math.atanh,
        "log": math.log,
        "log2": math.log2,
        "log10": math.log10,
        "log1p": math.log1p,
        "exp": math.exp,
        "exp2": math.exp2,
        "expm1": math.expm1,
        "sqrt": math.sqrt,
        "cbrt": lambda x: x ** (1 / 3),
        "pow": pow,
        "ceil": math.ceil,
        "floor": math.floor,
        "trunc": math.trunc,
        "fabs": math.fabs,
        "factorial": math.factorial,
        "gcd": math.gcd,
        "lcm": math.lcm,
        "isclose": math.isclose,
        "isfinite": math.isfinite,
        "isinf": math.isinf,
        "isnan": math.isnan,
        "hypot": math.hypot,
        "degrees": math.degrees,
        "radians": math.radians,
        "fsum": math.fsum,
        "prod": math.prod,
        "erf": math.erf,
        "erfc": math.erfc,
        "gamma": math.gamma,
        "lgamma": math.lgamma,
        "comb": math.comb,
        "perm": math.perm,
        "copysign": math.copysign,
        "dist": math.dist,
    }
    functions.update({
        "pi": math.pi,
        "e": math.e,
        "tau": math.tau,
        "inf": math.inf,
        "nan": math.nan,
    })
    return functions


def _safe_eval(expression, functions):
    tree = ast.parse(expression.strip(), mode="eval")

    def _eval(node):
        if isinstance(node, ast.Constant):
            value = node.value
            if isinstance(value, (int, float)) and not isinstance(value, bool):
                return value
            raise ValueError("Unsupported literal")
        if isinstance(node, ast.BinOp):
            left = _eval(node.left)
            right = _eval(node.right)
            op = _ALLOWED_OPERATOR_MAP.get(type(node.op))
            if op is None:
                raise ValueError(f"Unsupported operator: {type(node.op).__name__}")
            return op(left, right)
        if isinstance(node, ast.UnaryOp):
            operand = _eval(node.operand)
            op = _ALLOWED_OPERATOR_MAP.get(type(node.op))
            if op is None:
                raise ValueError(f"Unsupported unary operator: {type(node.op).__name__}")
            return op(operand)
        if isinstance(node, ast.Name):
            if node.id in functions:
                return functions[node.id]
            raise ValueError(f"Unknown name: {node.id}")
        if isinstance(node, ast.Call):
            if not isinstance(node.func, ast.Name):
                raise ValueError("Only direct function calls are allowed")
            name = node.func.id
            if name not in functions:
                raise ValueError(f"Function not allowed: {name}")
            function = functions[name]
            if not callable(function):
                raise ValueError(f"Name is not callable: {name}")
            args = [_eval(arg) for arg in node.args]
            return function(*args)
        raise ValueError(f"Unsupported syntax: {type(node).__name__}")

    return _eval(tree.body)


def scientific_calculator() -> None:
    """Scientific Calculator Mode."""
    print("Scientific Calculator")
    functions = _build_function_map()

    while True:
        expression = input("\nEnter the expression (e.g., sin(pi/2), sqrt(16)) or ('exit' to return to main menu): ")
        if expression.lower() in {"exit", "quit"}:
            break

        try:
            result = _safe_eval(expression, functions)
            print("-" * 50)
            print("The result is:", result)
            print("-" * 50)
        except Exception as exc:
            print("-" * 50)
            print(f"Invalid input. Please enter a valid mathematical expression. Error: {exc}")
            print("-" * 50)


__all__ = ["scientific_calculator"]
