def add(numbers: str) -> int:
    if not numbers:
        return 0
    
    delimiter, numbers = parse_delimiter(numbers)
    numbers = numbers.replace("\n", delimiter)
    
    return sum(
        int(num) for num in numbers.split(delimiter) 
        if num and int(num) <= 1000
    )

def parse_delimiter(numbers: str):
    if numbers.startswith("//"):
        parts = numbers.split("\n", 1)
        return parts[0][2:], parts[1]
    return ",", numbers
