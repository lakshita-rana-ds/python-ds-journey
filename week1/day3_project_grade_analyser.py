# ======================================

# ---------- DAY 3 - PROJECT -----------

# STUDENT GRADE ANALYSER
# DATE - 26 May, 2026

# ======================================



students = {
    "Lakshita": [88, 92, 79, 95, 84],
    "Riya":     [55, 61, 48, 72, 59],
    "Arjun":    [90, 85, 91, 88, 94],
    "Priya":    [35, 42, 50, 38, 45],
}

print("=" * 40)
print("  📊 STUDENT GRADE ANALYSER")
print("=" * 40)

for name, scores in students.items():
    avg = sum(scores) / len(scores)

    if avg >= 85:
        grade, remark = "A", "Excellent 🌟"
    elif avg >= 70:
        grade, remark = "B", "Good 👍"
    elif avg >= 55:
        grade, remark = "C", "Average"
    else:
        grade, remark = "F", "Needs work ⚠️"

    print(f"\n{name}")
    print(f"  Avg: {avg:.1f} | Grade: {grade} | {remark}")
    print(f"  High: {max(scores)} | Low: {min(scores)}")

# List comprehension — students who passed
passed = [n for n, s in students.items() if sum(s)/len(s) >= 55]
print(f"\n✅ Passed ({len(passed)}): {', '.join(passed)}")



# -------- END ---------
