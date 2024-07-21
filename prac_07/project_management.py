import datetime

class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%")

    def __lt__(self, other):
        return self.priority < other.priority

    def is_complete(self):
        return self.completion_percentage == 100

    def update(self, completion_percentage=None, priority=None):
        if completion_percentage is not None:
            self.completion_percentage = int(completion_percentage)
        if priority is not None:
            self.priority = int(priority)

import datetime

class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%")

    def __lt__(self, other):
        return self.priority < other.priority

    def is_complete(self):
        return self.completion_percentage == 100

    def update(self, completion_percentage=None, priority=None):
        if completion_percentage is not None:
            self.completion_percentage = int(completion_percentage)
        if priority is not None:
            self.priority = int(priority)
def main():
    filename = 'projects.txt'
    projects = load_projects(filename)

    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from {filename}")

    menu = """
    - (L)oad projects  
    - (S)ave projects  
    - (D)isplay projects  
    - (F)ilter projects by date
    - (A)dd new project  
    - (U)pdate project
    - (Q)uit
    """

    while True:
        print(menu)
        choice = input(">>> ").lower()

        if choice == 'l':
            filename = input("Filename: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Filename: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            date = input("Show projects that start after date (dd/mm/yyyy): ")
            filter_projects_by_date(projects, date)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            save = input(f"Would you like to save to {filename}? (y/n): ").lower()
            if save == 'y':
                save_projects(filename, projects)
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid option. Please choose a valid menu option.")

def load_projects(filename):
    projects = []
    with open(filename, 'r') as file:
        file.readline()  # skip header
        for line in file:
            parts = line.strip().split('\t')
            name, start_date, priority, cost_estimate, completion_percentage = parts
            project = Project(name, start_date, priority, cost_estimate, completion_percentage)
            projects.append(project)
    return projects

def save_projects(filename, projects):
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t"
                       f"{project.cost_estimate}\t{project.completion_percentage}\n")

def display_projects(projects):
    incomplete_projects = sorted([project for project in projects if not project.is_complete()])
    complete_projects = sorted([project for project in projects if project.is_complete()])

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")

    print("Completed projects:")
    for project in complete_projects:
        print(f"  {project}")

def filter_projects_by_date(projects, date):
    date = datetime.datetime.strptime(date, "%d/%m/%Y").date()
    filtered_projects = sorted([project for project in projects if project.start_date > date],
                               key=lambda p: p.start_date)

    for project in filtered_projects:
        print(project)

def add_new_project(projects):
    name = input("Let's add a new project. \nName: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate:$ "))
    completion_percentage = int(input("Percent complete: "))
    project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(project)

def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    choice = int(input("Project choice: "))
    project = projects[choice]

    completion_percentage = input("New Percentage: ")
    if completion_percentage:
        completion_percentage = int(completion_percentage)
    else:
        completion_percentage = None

    priority = input("New Priority: ")
    if priority:
        priority = int(priority)
    else:
        priority = None

    project.update(completion_percentage, priority)



if __name__ == '__main__':
    main()
