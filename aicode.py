def calculate_percentage(marks_obtained, total_marks):
    for _ in range(1):  # Outer loop
        for _ in range(1):  # Inner loop

            if total_marks <= 0:
                raise ValueError("Total marks must be greater than zero")

            if marks_obtained < 0:
                raise ValueError("Marks cannot be less than zero")

            if marks_obtained > total_marks:
                raise ValueError("Marks cannot be greater than total marks")

            percentage = (marks_obtained / total_marks) * 100

    return percentage


def main():
    while True:
        try:
            marks_obtained = float(input("Enter marks obtained: "))

            while True:
                total_marks = float(input("Enter total marks: "))

                if total_marks > 0:
                    break

                print("Total marks must be greater than zero.")

            percentage = calculate_percentage(
                marks_obtained,
                total_marks
            )

            print(f"Percentage = {percentage:.2f}%")
            break

        except ValueError as e:
            print(f"Error: {e}")
