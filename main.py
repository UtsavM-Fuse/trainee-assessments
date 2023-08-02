import argparse


def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract the second number from the first number."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


def main():
    """Main function to perform basic mathematical operations."""
    result_addition = add(args.firstNum, args.secondNum)
    result_subtraction = subtract(args.firstNum, args.secondNum)
    result_multiplication = multiply(args.firstNum, args.secondNum)

    print(f"Addition: {args.firstNum} + {args.secondNum} = {result_addition}")
    print(f"Subtraction: {args.firstNum} - {args.secondNum} = {result_subtraction}")
    print(
        f"Multiplication: {args.firstNum} * {args.secondNum} = {result_multiplication}"
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Basic Mathematical Operations")
    parser.add_argument(
        "--firstNum",
        type=float,
        default=0,
        help="First operand",
    )
    parser.add_argument(
        "--secondNum",
        type=float,
        default=0,
        help="Second operand",
    )

    args = parser.parse_args()

    main()
