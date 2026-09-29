import csv
import json
import os

def process_student_records(input_csv_path, output_json_path):
    total_students = 0
    scores = []
    top_scorer = None
    course_counts = {}

    # Read CSV file using csv.DictReader inside a context manager
    with open(input_csv_path, mode="r", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            total_students += 1
            name = row["name"].strip()
            course = row["course"].strip()
            score = float(row["score"])
            
            scores.append(score)
            
            # Track course enrollment counts
            course_counts[course] = course_counts.get(course, 0) + 1
            
            # Track top scorer
            if top_scorer is None or score > top_scorer["score"]:
                top_scorer = {"name": name, "score": score}

    # Compute average score rounded to 2 decimal places
    average_score = round(sum(scores) / len(scores), 2) if scores else 0.0

    summary_data = {
        "total_students": total_students,
        "average_score": average_score,
        "top_scorer": top_scorer,
        "course_counts": course_counts
    }

    # Write summary report to JSON file with 4-space indentation
    with open(output_json_path, mode="w", encoding="utf-8") as json_file:
        json.dump(summary_data, json_file, indent=4)

    return summary_data


# Example Walkthrough
if __name__ == "__main__":
    csv_path = os.path.join(os.path.dirname(__file__), "students.csv")
    json_path = os.path.join(os.path.dirname(__file__), "summary.json")

    # Create sample CSV file
    sample_csv_content = """student_id,name,course,score
101,Arham,AI,88.5
102,Lisa,BDA,94.0
103,Vinod,AI,96.5
"""
    with open(csv_path, "w", encoding="utf-8") as f:
        f.write(sample_csv_content)

    # Process student records
    result = process_student_records(csv_path, json_path)

    # Display generated JSON output
    with open(json_path, "r", encoding="utf-8") as f:
        print(f.read())
