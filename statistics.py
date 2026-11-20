def calculate_statistics(numbers):
    if not numbers:
        raise ValueError("Список не должен быть пустым")

    return{
        "min": min(numbers),
        "max": max(numbers),
        "average": sum(numbers)/len(numbers)
    }

if __name__ == "__main__":
    print(calculate_statistics([10,20,30]))