
numbers = [1,2,3,4,5,6,7,8,9,10]

doubles = [num * 2 for num in numbers]
triples = [num * 3 for num in numbers]
squares = [num * num for num in numbers]
print(f"Numbers: {numbers}")
print(f"Doubles: {doubles}")
print(f"Triples: {triples}")
print(f"Squares: {squares}")

odds = [num for num in numbers if num % 2 == 1]
even = [num for num in numbers if num % 2 == 0]
print(f"Odds: {odds}")
print(f"Even: {even}")
