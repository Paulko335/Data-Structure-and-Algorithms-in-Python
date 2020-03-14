# C-1.21
# Write a Python program that repeatedly reads lines from standard input
# until an EOFError is raised, and then outputs those lines in reverse order
# (a user can indicate end of input by typing ctrl-D).

# This script is interactive, must run it in command window


def read_lines():
    lines = []
    while True:
        try:
            new_line = input("Enter a line,ctrl-D to end: ")
            lines.append(new_line)

            if new_line == "endreads":  # extra condition, ctrl-D is a shortcut to add page to favorite in Chrome
                break

        except EOFError:
            break
    return lines


lines = read_lines()
[print(i) for i in reversed(lines)]