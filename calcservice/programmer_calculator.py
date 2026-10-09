import ast
import operator


_ALLOWED_OPERATOR_MAP = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.BitAnd: operator.and_,
    ast.BitOr: operator.or_,
    ast.BitXor: operator.xor,
    ast.LShift: operator.lshift,
    ast.RShift: operator.rshift,
    ast.Invert: operator.invert,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}


def _safe_eval(expression):
    tree = ast.parse(expression.strip(), mode="eval")

    def _eval(node):
        if isinstance(node, ast.Constant):
            value = node.value
            if isinstance(value, int) and not isinstance(value, bool):
                return value
            raise ValueError("Only integer literals are supported")
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
        raise ValueError(f"Unsupported syntax: {type(node).__name__}")

    return _eval(tree.body)


def programmer_calculator() -> None:
    """Programmer calculator with binary, octal, and hexadecimal support."""
    print("\nProgrammer Calculator")
    valid_bits = {8, 16, 32, 64}

    while True:
        expression = input("Enter your expression (or 'exit' to return to main menu): ").strip()
        expression = expression.upper()
        expression = (
            expression.replace("AND", "&")
            .replace("OR", "|")
            .replace("XOR", "^")
            .replace("NOT", "~")
        )

        if expression.lower() == "exit":
            break

        try:
            bit = int(input("Enter the bit size (8, 16, 32, 64): "))
            if bit not in valid_bits:
                raise ValueError
        except ValueError:
            print("Invalid bit size. Please enter 8, 16, 32, or 64.")
            continue

        signed = input("Signed or Unsigned (s/u): ").strip().lower() == "s"

        try:
            result = _safe_eval(expression)
            if not isinstance(result, int):
                raise ValueError("Result is not an integer.")
        except Exception as exc:
            print(f"Error in expression. Please check your input. {exc}")
            continue

        mask = (1 << bit) - 1
        result &= mask

        def show_bits(value):
            bits = format(value, f"0{bit}b")
            print("\nBit position: ")
            print(" ".join(str(i) for i in range(bit - 1, -1, -1)))
            print(bits)

        show_bits(result)

        toggle = input("Do you want to toggle any bit?(yes/no): ").strip().lower()
        while toggle == "yes":
            try:
                position = int(input("Enter bit position to toggle: "))
                if 0 <= position < bit:
                    result ^= 1 << position
                    result &= mask
                    show_bits(result)
                else:
                    print("Invalid bit position. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid bit position.")
            toggle = input("Do you want to toggle any bit?(yes/no): ").strip().lower()

        if signed:
            sign_bit = 1 << (bit - 1)
            decimal = result - (1 << bit) if (result & sign_bit) else result
        else:
            decimal = result

        print("\nResult:")
        print("decimal:", decimal)
        print("hexadecimal:", format(result, "X"))
        print("octal:", format(result, "o"))
        print("binary:", format(result, f"0{bit}b"))


__all__ = ["programmer_calculator"]
