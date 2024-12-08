CURRENT_YEAR = 2017
VINTAGE_AGE = 50

class Guitar:

def main():
    guitars = read_guitars_from_file('guitar.csv')
    print("Guitars:")
    display_guitars(guitars)

    # Sort guitars by year
    guitars.sort()

    print("\nSorted guitars (oldest to newest):")
    display_guitars(guitars)

def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

def __str__(self):
    return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

def get_age(self):
    return CURRENT_YEAR - self.year

def is_vintage(self):
    return self.get_age() >= VINTAGE_AGE

def __lt__(self, other):
    return self.year < other.year

def read_guitars_from_file(filename):
    guitars = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitars.append(Guitar(name, year, cost))
    return guitars

def display_guitars(guitars):
    for guitar in guitars:
        print(guitar)

main()

