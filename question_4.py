points_list = [
    {"x": 1, "y": 2},
    {"x": 3, "y": 4},
    {"x": 5, "y": 6},
    {"x": 7, "y": 8}
]
result = next((point for point in points_list if point.get("x") == 5), {})
print(result)
