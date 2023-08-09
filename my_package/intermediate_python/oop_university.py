"""
Module: university_system

This module defines classes for a simple university system.
"""


class University:
    def __init__(self, name: str, location: str) -> None:
        """
        Initialize the University object with name, location, and an empty list of departments.

        Args:
            name (str): The name of the university.
            location (str): The location of the university.

        Returns:
            None
        """
        self._name = name
        self._location = location
        self._departments: list[Department] = []

    def add_department(self, department: "Department") -> None:
        """
        Add a new department to the university.

        Args:
            department (Department): The department object to be added.

        Returns:
            None
        """
        self._departments.append(department)

    def display_details(self) -> None:
        """
        Display the details of the university and its departments.

        Returns:
            None
        """
        print(f"University Name: {self._name}")
        print(f"Location: {self._location}")
        print("Departments:")
        for department in self._departments:
            print(f"  - {department.get_name()}")


class Department(University):
    def __init__(
        self, name: str, location: str, department_name: str, hod: str
    ) -> None:
        """
        Initialize the Department object with name, location, department name, head of the department, and an empty list
        of courses offered.

        Args:
            name (str): The name of the university.
            location (str): The location of the university.
            department_name (str): The name of the department.
            hod (str): The head of the department.

        Returns:
            None
        """
        super().__init__(name, location)
        self._department_name = department_name
        self._hod = hod
        self._courses_offered: list[str] = []

    def add_course(self, course: str) -> None:
        """
        Add a new course to the department.

        Args:
            course (str): The name of the course to be added.

        Returns:
            None
        """
        self._courses_offered.append(course)

    def get_name(self) -> str:
        """
        Get the name of the department.

        Returns:
            str: The name of the department.
        """
        return self._department_name

    def display_details(self) -> None:
        """
        Display the details of the department, including the university details.

        Returns:
            None
        """
        super().display_details()
        print(f"Department Name: {self._department_name}")
        print(f"Head of the Department: {self._hod}")
        print("Courses Offered:")
        for course in self._courses_offered:
            print(f"  - {course}")


# Testing the classes
if __name__ == "__main__":
    # Create a University
    university = University("Kathmandu University", "Dhulikhel")

    # Create departments
    department1 = Department("DoCSE", "Dhulikhel", "Computer Science", "Prof. X")
    department2 = Department("DoEE", "Dhulikhel", "Electrical Engineering", "Prof. Y")

    # Add courses to departments
    department1.add_course("Introduction to Programming")
    department1.add_course("Data Structures and Algorithms")
    department2.add_course("Electronics and Circuits")
    department2.add_course("Power Systems")

    # Add departments to the university
    university.add_department(department1)
    university.add_department(department2)

    # Display university and department details
    university.display_details()
    print("\n")
    department1.display_details()
    print("\n")
    department2.display_details()
