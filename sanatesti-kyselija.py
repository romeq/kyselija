#!/usr/bin/env python3
import sys


def read_file(file: str) -> list[str]:
    try:
        f = open(file, "r")
    except FileNotFoundError:
        print(f"file '{file}' was not found.", file=sys.stderr)
        return []

    lines = f.readlines()
    f.close()

    return lines


def main():
    if len(sys.argv) < 2:
        print("files are parsed in 'question: answer' form.")
        print(f"usage: {sys.argv[0]} kysymykset.txt", file=sys.stderr)
        return

    questions = read_file(sys.argv[1])
    if len(questions) == 0:
        return

    delim=": "
    failed = 0
    fq = []
    for q in questions:
        print("\033[90m---------------\033[0m")
        x = q.split(delim)
        if len(x) < 2:
            break
        print(f"Question: \033[36m{x[0]}\033[0m")
        ans = input("Answer: ")
        cans = delim.join(x[1:]).removesuffix("\n")
        if len(ans) > len(cans) / 2 and cans.__contains__(ans):
            print()
            continue
        print(f"\033[31mCorrect answer: \033[0m{cans}")
        vq = "My answer and the given correct answer correlate rather in positive way (y/n): "
        if str(input(vq)).lower() != "y":
            failed += 1
            selitys = ": ".join(x[1:])
            fq.append(f"{x[0]} ({selitys})")

        print()
            
    print(f"You failed {failed} times.")
    for q in fq:
        print(f"\t{q}")

if __name__ == "__main__":
    main()

