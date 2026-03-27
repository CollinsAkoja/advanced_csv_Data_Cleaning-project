import csv
from typing import Dict


def is_valid_score(score: str) -> bool:
    try:
        v = float(score)
        return 0 <= v <= 100
    except (ValueError, TypeError):
        return False


def validate_and_extract(row: Dict[str, str]):
    """Return cleaned dict or None if invalid.

    Accepts rows with either:
    - 'name', 'score', 'department'
    - 'first_name', 'last_name' (or 'last name'), 'score', 'department'
    """
    # Department
    dept = (row.get("department") or "").strip()
    if not dept:
        return None

    # Score
    score_raw = row.get("score")
    if score_raw is None or str(score_raw).strip() == "":
        return None
    if not is_valid_score(score_raw):
        return None
    score = float(score_raw)

    # Name handling
    first = last = ""
    if row.get("first_name"):
        first = (row.get("first_name") or "").strip().title()
        # support header 'last name' with space
        last = (row.get("last_name") or row.get("last name") or "").strip().title()
    elif row.get("name"):
        parts = (row.get("name") or "").strip().split()
        if parts:
            first = parts[0].title()
            last = " ".join(parts[1:]).title() if len(parts) > 1 else ""
    else:
        return None

    if not first:
        return None

    return {"first_name": first, "last_name": last, "score": score, "department": dept.title()}


def process_csv(input_file: str, output_file: str, invalid_file: str = None):
    cleaned = []
    invalid = []

    with open(input_file, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            out = validate_and_extract(row)
            if out:
                cleaned.append(out)
            else:
                invalid.append(row)

    # write cleaned
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        fieldnames = ["first_name", "last_name", "score", "department"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(cleaned)

    # write invalid if requested
    if invalid_file and invalid:
        keys = list(invalid[0].keys())
        with open(invalid_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=keys + ["reason"])
            writer.writeheader()
            for r in invalid:
                r2 = r.copy()
                r2["reason"] = "missing/invalid field or score out of range"
                writer.writerow(r2)

    print(f"Cleaned rows: {len(cleaned)}")
    print(f"Invalid rows: {len(invalid)}")


if __name__ == "__main__":
    process_csv("students.csv", "cleaned_students.csv", "invalid_rows.csv")




