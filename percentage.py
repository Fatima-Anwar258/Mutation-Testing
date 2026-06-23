def calculate_percentage(marks_obtained, total_marks):
    if total_marks <= 0:
        raise ValueError("Total marks must be greater than zero")

    if marks_obtained < 0:
        raise ValueError("Marks cannot be negative")

    if marks_obtained > total_marks:
        raise ValueError("Marks cannot exceed total marks")

    return (marks_obtained / total_marks) * 100


def main():
    marks_obtained = float(input("Enter marks obtained: "))
    total_marks = float(input("Enter total marks: "))

    percentage = calculate_percentage(
        marks_obtained,
        total_marks
    )

    print(f"Percentage = {percentage:.2f}%")
