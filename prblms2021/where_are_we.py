import math

def where_are_we(path_points, percent_traveled):
    if percent_traveled < 0 or percent_traveled > 1:
        raise ValueError("Percent traveled must be between 0 and 1")
    
    if len(path_points) < 2:
        raise ValueError("Path must contain at least 2 points")
    
    # Calculate total path length
    total_length = 0
    segment_lengths = []
    for i in range(len(path_points) - 1):
        x1, y1 = path_points[i]
        x2, y2 = path_points[i + 1]
        segment_length = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        total_length += segment_length
        segment_lengths.append(segment_length)
    
    # Find the segment where the point is located
    target_distance = total_length * percent_traveled
    current_distance = 0
    for i, segment_length in enumerate(segment_lengths):
        if current_distance + segment_length >= target_distance:
            # Point is on this segment
            segment_percent = (target_distance - current_distance) / segment_length
            x1, y1 = path_points[i]
            x2, y2 = path_points[i + 1]
            x = x1 + segment_percent * (x2 - x1)
            y = y1 + segment_percent * (y2 - y1)
            return x, y
        current_distance += segment_length
    
    # If we've reached this point, return the last point in the path
    return path_points[-1]

# Example usage
path = [(0, 0), (4, 3), (-4, 9)]
percent = 0.75

result = where_are_we(path, percent)
print(f"Point location at {percent*100}% of the path: {result}")