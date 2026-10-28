"""
Day 22 - 2026-10-28
Tool: GPA Calculator
What it does: Turns subject marks into grade points on the common
Bangladesh 5.00 scale, then averages them (optionally weighted by
credit hours) to give the GPA for a term.
Who it helps: School, college and university students who want to
check their GPA as soon as marks come out, without waiting.
"""

# (minimum marks, grade point) on the 5.00 scale
SCALE = [(80, 5.00), (70, 4.00), (60, 3.50), (50, 3.00),
         (40, 2.00), (33, 1.00), (0, 0.00)]


def grade_point(marks):
    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100.")
    for minimum, point in SCALE:
        if marks >= minimum:
            return point
    return 0.00


def gpa(subjects):
    """subjects: list of (marks, credit_hours). Credit-weighted GPA."""
    total_points = 0.0
    total_credits = 0.0
    for marks, credits in subjects:
        total_points += grade_point(marks) * credits
        total_credits += credits
    if total_credits == 0:
        raise ValueError("Total credits cannot be zero.")
    return round(total_points / total_credits, 2)


if __name__ == "__main__":
    my_subjects = [(85, 3), (72, 3), (64, 2), (91, 1)]
    print("Points for 85 marks:", grade_point(85))
    print("Points for 45 marks:", grade_point(45))
    print("My GPA:", gpa(my_subjects))
