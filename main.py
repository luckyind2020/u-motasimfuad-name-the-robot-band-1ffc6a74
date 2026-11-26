"""Name the Robot Band — entry program.

Reads the one-line entry from entry.txt next to this file, validates it
against the bounty gate (UTF-8 text, 1-200 characters, not only whitespace),
writes it to /output/entry.txt for the grader, and prints it.
"""

from pathlib import Path

MAX_CHARS = 200


def load_entry() -> str:
    path = Path(__file__).with_name("entry.txt")
    return path.read_text(encoding="utf-8").strip()


def write_output(entry: str) -> Path:
    """Write the validated entry where the grader reads it."""
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(entry + "\n", encoding="utf-8")
    return out_path


def validate_entry(entry: str) -> None:
    """Enforce the bounty gate: 1-200 chars, real text, single line."""
    if not entry or not entry.strip():
        raise SystemExit("invalid entry: empty or whitespace only")
    if len(entry) > MAX_CHARS:
        raise SystemExit(f"invalid entry: {len(entry)} chars exceeds {MAX_CHARS}")
    if "\n" in entry or "\r" in entry:
        raise SystemExit("invalid entry: must be a single line")
    if any(ord(ch) < 0x20 and ch not in ("\t",) for ch in entry):
        raise SystemExit("invalid entry: contains control characters")
    entry.encode("utf-8")


def main() -> None:
    entry = load_entry()
    validate_entry(entry)
    write_output(entry)
    print(entry)


if __name__ == "__main__":
    main()
