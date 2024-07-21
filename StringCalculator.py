def add(numbers: str) -> int:
    if not numbers:
        return 0
    
    delimiter, numbers = parse_delimiter(numbers)
    numbers = numbers.replace("\n", delimiter)
    
    return sum(
        min(int(num), 1000) for num in numbers.split(delimiter) if num
    )

def parse_delimiter(numbers: str):
    if numbers.startswith("//"):
        delimiter = numbers[2]
        numbers = numbers[4:]
    else:
        delimiter = ","
    return delimiter, numbers
