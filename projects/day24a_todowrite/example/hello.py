"""Minimal greeting example used by the s05 TodoWrite demo."""


def greet(name: str) -> None:
    """Print a greeting addressed to ``name``.

    Args:
        name: The person or thing to greet.
    """
    message: str = f"Hello, {name}"
    print(message)


if __name__ == "__main__":
    greet("Claude")
