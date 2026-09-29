# 1. Custom Exception
class RecordNotFoundError(Exception):
    pass


# 2. DatabaseRecord Class
class DatabaseRecord:
    def __init__(self, record_id, data):
        self.record_id = int(record_id)
        self.data = dict(data)

    def __repr__(self):
        return f"Record(id={self.record_id}, data={self.data})"

    def __str__(self):
        return self.__repr__()


# 3. Custom Iterator Class
class ResultSetIterator:
    def __init__(self, records_list):
        self._records = records_list
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._records):
            record = self._records[self._index]
            self._index += 1
            return record
        raise StopIteration


# 4. DatabaseResultSet Class
class DatabaseResultSet:
    def __init__(self, records_list):
        self._records = list(records_list)

    def __len__(self):
        return len(self._records)

    def __iter__(self):
        return ResultSetIterator(self._records)

    def __getitem__(self, key):
        # Integer indexing (0-based)
        if isinstance(key, int):
            return self._records[key]
        
        # String lookup by "name" attribute inside record data
        if isinstance(key, str):
            for record in self._records:
                if record.data.get("name") == key:
                    return record
            raise RecordNotFoundError(f"Record with name '{key}' not found in database.")
        
        raise TypeError(f"Invalid key type: {type(key).__name__}. Expected int or str.")


# Example Walkthrough
if __name__ == "__main__":
    # Setup records
    r1 = DatabaseRecord(101, {"name": "Alice", "role": "Admin"})
    r2 = DatabaseRecord(102, {"name": "Bob", "role": "User"})

    results = DatabaseResultSet([r1, r2])

    # 1. Length
    print(len(results))  # Output: 2

    # 2. Integer Indexing
    print(results[0].data["role"])  # Output: Admin

    # 3. String lookup
    record = results["Bob"]
    print(record.record_id)  # Output: 102

    # 4. Iteration
    for rec in results:
        print(rec.record_id)
    # Output:
    # 101
    # 102

    # 5. Missing key lookup
    try:
        missing = results["Charlie"]
    except RecordNotFoundError as e:
        print(e)  # Output: Record with name 'Charlie' not found in database.
