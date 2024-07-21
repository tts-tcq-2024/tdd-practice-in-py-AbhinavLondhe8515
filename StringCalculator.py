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
        delimiter = numbers[2]
        numbers = numbers[4:]
    else:
        delimiter = ","
    return delimiter, numbers
