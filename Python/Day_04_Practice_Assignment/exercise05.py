def traverse_nested_config(config_dict, path_str, default=None):
    if not path_str:
        return default
    
    try:
        keys = path_str.split(".")
        current = config_dict
        for key in keys:
            current = current[key]
        return current
    except (KeyError, TypeError, AttributeError):
        return default


# Test Data & Test Cases from Assignment.pdf
config = {
    "server": {
        "host": "127.0.0.1",
        "port": 8080,
        "ssl": {
            "enabled": True,
            "cert_path": "/etc/ssl/certs"
        }
    },
    "database": "postgresql://localhost:5432"
}

# Test Case 1: Valid Path
print("Test Case 1:")
result_1 = traverse_nested_config(config, "server.ssl.cert_path")
print(result_1)
# Output: /etc/ssl/certs

# Test Case 2: Missing Key (Triggers KeyError)
print("\nTest Case 2:")
result_2 = traverse_nested_config(config, "server.database.username", "guest")
print(result_2)
# Output: guest

# Test Case 3: Indexing Non-Dictionary value (Triggers TypeError)
# Here config["database"] is a string, which cannot be indexed with "host"
print("\nTest Case 3:")
result_3 = traverse_nested_config(config, "database.host", "localhost")
print(result_3)
# Output: localhost
