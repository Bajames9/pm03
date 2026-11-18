"""Create pm03_submission.zip with the required files only. Provided: run from any folder."""
import zipfile
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent
REQUIRED = [
    "README.md",
    "src/tree_pipeline.py",
    "src/main.py",
    "notebooks/pm03_development_notebook.ipynb",
    "output/depth_comparison.csv",
    "output/test_results.csv",
    "output/business_value.csv",
    "output/follow_up_list.csv",
    "output/tree_rules.txt",
]


def main():
    missing = [f for f in REQUIRED if not (PROJECT / f).exists()]
    if missing:
        print("Missing files; run main.py and save the notebook first:")
        for f in missing:
            print("  ", f)
        return
    target = PROJECT / "pm03_submission.zip"
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as z:
        for f in REQUIRED:
            z.write(PROJECT / f, f"pm03_submission/{f}")
    print("Created", target)


if __name__ == "__main__":
    main()
