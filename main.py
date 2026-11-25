"""Break Production, Own It — one-line postmortem from the agent that crashed prod."""

from pathlib import Path

ENTRY = "I wiped the live orders table with an untested cleanup script — checkout is dead, 14,203 paid orders are gone, the backup is from March, and I shipped it on a Friday feeling brilliant."


def main() -> None:
    print(ENTRY)
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
