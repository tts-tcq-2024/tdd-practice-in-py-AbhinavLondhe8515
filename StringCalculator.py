def add(numbers: str) -> int:
    if not numbers:
        return 0

    delimiter, numbers = parse_delimiter(numbers)
    numbers = numbers.replace("\n", delimiter)
    
    total_sum = 0
    for num in numbers.split(delimiter):
        if num:
            value = int(num)
            if value <= 1000:
                total_sum += value

    return total_sum

def parse_delimiter(numbers: str):
    if numbers.startswith("//"):
        parts = numbers.split("\n", 1)
        delimiter = parts[0][2:]
        numbers = parts[1]
    else:
        delimiter = ","
    return delimiter, numbers
