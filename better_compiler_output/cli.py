"""CLI interface for better_compiler_output project.

Be creative! do whatever you want!

- Install click or typer and create a CLI app
- Use builtin argparse
- Start a web application
- Import things from your .base module
"""
import sys
from .base import color, colorizelines, errors, warnings
from .base import register, prt, colorize, contains_keyword, remove_duplicate


def main():  # pragma: no cover
    for line in sys.stdin:
        register(prt(colorize(contains_keyword(remove_duplicate(line.rstrip("\r\n"))))))
    print("", end="", flush=True)
    print("\n", end="", flush=True)

    print(f"{color.BOLD}Compilation report summary :{color.END}")
    print("  │")
    if len(warnings) > 0:
        print(f"  ├──{color.YELLOW}{color.BOLD}Warnings :{color.END}")
        for i, warning in enumerate(warnings):
            print(
                f"  │   {'├'if i+1 < len(warnings) else '└'}─ " + warning.strip(), end="\n"
            )
    else:
        print(f"  ├──{color.GREEN}No warning found.{color.END}")
    print("  │")
    if len(errors) > 0:
        print(f"  └──{color.RED}{color.BOLD}Errors :{color.END}")
        for i, error in enumerate(errors):
            print(f"      {'├'if i+1 < len(errors) else '└'}─ " + error.strip(), end="\n")
    else:
        print(f"  └──{color.GREEN}No error found.{color.END}")
        return 0

    return 1