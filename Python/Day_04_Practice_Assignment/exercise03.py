def compile_feedback(ratings_dict):
    result_dict = {}
    for course, ratings in ratings_dict.items():
        valid_ratings = []
        for item in ratings:
            try:
                valid_ratings.append(float(item))
            except (ValueError, TypeError):
                print(f"Warning: Invalid rating value '{item}' in course '{course}' skipped.")
        
        try:
            avg = round(sum(valid_ratings) / len(valid_ratings), 2)
            result_dict[course] = avg
        except ZeroDivisionError:
            print(f"Warning: No valid ratings found for course '{course}'. Rating set to 0.0.")
            result_dict[course] = 0.0
            
    return result_dict


feedback_data = {
    "Python Programming": [5, 4, "4", "Great", 5],
    "Machine Learning": [],
    "Deep Learning": ["Good", "Average", None]
}

print("--- Console Warnings ---")
compiled_results = compile_feedback(feedback_data)

print("\n--- Returned Dictionary ---")
print(compiled_results)


