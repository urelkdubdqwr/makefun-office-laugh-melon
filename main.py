# Writes a single short office-life joke out to an entry.txt file for judging.
import os

ENTRY_TEXT = (
    "I put 'team player' on my review. Then I watched four people reply-all "
    "'me too' to an email about replying less."
)


def main():
    # Default to /output because that path is guaranteed writable in the container.
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
