import re

def process_dataset(dataset):
    # 1. Parsing: Extract product name, numeric price (float), and rating (float)
    parsed_data = []
    for item in dataset:
        name = item[0]
        price_match = re.search(r"\d+(?:\.\d+)?", item[1])
        score_match = re.search(r"\d+(?:\.\d+)?", item[2])
        if price_match and score_match:
            price = float(price_match.group(0))
            score = float(score_match.group(0))
            parsed_data.append((name, price, score))
        
    # 2. Filtering: Use filter() with a lambda function to keep price <= 1000.0
    filtered_data = filter(lambda x: x[1] <= 1000.0, parsed_data)
    
    # 3. Mapping: Use map() with a lambda to transform entries into dicts
    mapped_data = map(
        lambda x: {"product": x[0], "price": x[1], "score": x[2]},
        filtered_data
    )
    
    # 4. Sorting: Sort in descending order of score using sorted() with lambda key
    sorted_data = sorted(mapped_data, key=lambda x: x["score"], reverse=True)
    
    # 5. Return the sorted list of dictionaries
    return sorted_data


# Example Walkthrough
data_input = [
    ("Laptop", "Price: 1200", "Rating: 4.8"),
    ("Phone", "Price: 800", "Rating: 4.5"),
    ("Mouse", "Price: 25", "Rating: 4.7"),
    ("Charger", "Price: 15", "Rating: 4.2")
]

output = process_dataset(data_input)
print(output)
