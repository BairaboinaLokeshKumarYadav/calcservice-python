import ast
import math
import operator


_ALLOWED_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
    ast.Not: operator.not_,
}


def _safe_eval(expression):
    expression = expression.strip()
    if not expression:
        raise ValueError("Empty expression")

    tree = ast.parse(expression, mode="eval")

    def _eval(node):
        if isinstance(node, ast.Constant):
            value = node.value
            if isinstance(value, (int, float)) and not isinstance(value, bool):
                return value
            raise ValueError("Unsupported literal")
        if isinstance(node, ast.BinOp):
            left = _eval(node.left)
            right = _eval(node.right)
            op = _ALLOWED_OPERATORS.get(type(node.op))
            if op is None:
                raise ValueError(f"Unsupported operator: {type(node.op).__name__}")
            return op(left, right)
        if isinstance(node, ast.UnaryOp):
            operand = _eval(node.operand)
            op = _ALLOWED_OPERATORS.get(type(node.op))
            if op is None:
                raise ValueError(f"Unsupported unary operator: {type(node.op).__name__}")
            return op(operand)
        if isinstance(node, ast.Name):
            if node.id in {"pi": math.pi, "e": math.e, "tau": math.tau}:
                return {"pi": math.pi, "e": math.e, "tau": math.tau}[node.id]
            raise ValueError(f"Unknown name: {node.id}")
        if isinstance(node, ast.Call):
            if not isinstance(node.func, ast.Name):
                raise ValueError("Only direct function calls are allowed")
            name = node.func.id
            if name not in {"sqrt": math.sqrt, "pow": pow, "abs": abs, "round": round}:
                raise ValueError(f"Function not allowed: {name}")
            args = [_eval(arg) for arg in node.args]
            return {"sqrt": math.sqrt, "pow": pow, "abs": abs, "round": round}[name](*args)
        raise ValueError(f"Unsupported syntax: {type(node).__name__}")

    return _eval(tree.body)


def basic_calculator() -> None:
    """Basic Calculator Mode."""
    print("\nBasic Calculator")
    while True:
        expression = input("\nEnter the expression (e.g., 2 + 3 * 4) or ('exit' to return to main menu): ")
        if expression.lower() in {"exit", "quit"}:
            break
        try:
            result = _safe_eval(expression)
            print("-" * 50)
            print("The result is:", result)
            print("-" * 50)
        except Exception as exc:
            print("-" * 50)
            print(f"Invalid input. Please enter a valid mathematical expression. Error: {exc}")
            print("-" * 50)


__all__ = ["basic_calculator"]
