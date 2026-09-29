"""
Week 5 Internship Task
Code Debugging, Refactoring, and Technical Analysis

Project: CampusConnect
Purpose:
- Demonstrate a simulated debugging scenario
- Compare inefficient code with refactored code
- Demonstrate modularization
- Demonstrate algorithm optimization
- Perform validation and testing
"""

# ============================================================
# CAMPUSCONNECT - SAMPLE DATA
# ============================================================

users = [
    {"id": 101, "name": "Rahul"},
    {"id": 102, "name": "Aman"},
    {"id": 103, "name": "Priya"},
    {"id": 104, "name": "Neha"},
]

projects = [
    {
        "id": 1,
        "name": "CampusConnect",
        "owner_id": 101,
        "status": "active"
    },
    {
        "id": 2,
        "name": "UniClock",
        "owner_id": 102,
        "status": "active"
    },
    {
        "id": 3,
        "name": "Career Pilot",
        "owner_id": 103,
        "status": "completed"
    },
    {
        "id": 4,
        "name": "ProjectHub",
        "owner_id": 104,
        "status": "active"
    },
    {
        "id": 5,
        "name": "Student Portal",
        "owner_id": 999,   # Invalid owner ID for testing
        "status": "active"
    }
]


# ============================================================
# PART 1: PROBLEMATIC / UNREFACTORED CODE
# ============================================================

def old_dashboard():
    """
    Simulated old implementation.

    Problems demonstrated:
    1. Nested loops
    2. Repeated searching
    3. Poor variable naming
    4. Multiple responsibilities in one function
    5. Limited validation
    6. Difficult to test
    """

    print("\n" + "=" * 60)
    print("OLD / UNREFACTORED DASHBOARD")
    print("=" * 60)

    data = projects

    for x in data:

        if x["status"] == "active":

            owner_name = "Unknown"

            # Inefficient nested search
            for y in users:
                if x["owner_id"] == y["id"]:
                    owner_name = y["name"]

            print(
                "Project:",
                x["name"],
                "| Owner:",
                owner_name
            )


# ============================================================
# PART 2: REFACTORED FUNCTIONS
# ============================================================

def validate_project(project):
    """
    Validate that a project contains the required fields.
    """

    required_fields = ["id", "name", "owner_id", "status"]

    for field in required_fields:
        if field not in project:
            return False

    if not project["name"]:
        return False

    return True


def filter_active_projects(project_list):
    """
    Return only valid active projects.
    """

    active_projects = []

    for project in project_list:

        if not validate_project(project):
            print(
                f"Warning: Invalid project data found: {project}"
            )
            continue

        if project["status"].lower() == "active":
            active_projects.append(project)

    return active_projects


def create_user_lookup(user_list):
    """
    Convert the user list into a dictionary.

    This allows fast lookup using the user ID.
    """

    return {
        user["id"]: user["name"]
        for user in user_list
    }


def attach_owner_names(project_list, user_lookup):
    """
    Attach owner names to projects using dictionary lookup.
    """

    updated_projects = []

    for project in project_list:

        owner_name = user_lookup.get(
            project["owner_id"],
            "Unknown"
        )

        updated_project = project.copy()
        updated_project["owner"] = owner_name

        updated_projects.append(updated_project)

    return updated_projects


def display_projects(project_list):
    """
    Display projects in a clean format.
    """

    print("\nCampusConnect Active Projects")
    print("-" * 60)

    if not project_list:
        print("No active projects found.")
        return

    for project in project_list:

        print(
            f"Project ID : {project['id']}"
        )

        print(
            f"Project    : {project['name']}"
        )

        print(
            f"Owner      : {project['owner']}"
        )

        print(
            f"Status     : {project['status']}"
        )

        print("-" * 60)


# ============================================================
# PART 3: REFACTORED DASHBOARD
# ============================================================

def refactored_dashboard(project_list, user_list):
    """
    Refactored CampusConnect dashboard.

    Responsibilities are separated into smaller functions.
    """

    print("\n" + "=" * 60)
    print("REFACTORED CAMPUSCONNECT DASHBOARD")
    print("=" * 60)

    # Step 1: Filter valid active projects
    active_projects = filter_active_projects(
        project_list
    )

    # Step 2: Create fast user lookup
    user_lookup = create_user_lookup(
        user_list
    )

    # Step 3: Attach owner names
    projects_with_owners = attach_owner_names(
        active_projects,
        user_lookup
    )

    # Step 4: Display final result
    display_projects(
        projects_with_owners
    )

    return projects_with_owners


# ============================================================
# PART 4: TESTING
# ============================================================

def test_user_lookup():
    """
    Test whether user lookup works correctly.
    """

    user_lookup = create_user_lookup(users)

    assert user_lookup[101] == "Rahul"
    assert user_lookup[102] == "Aman"
    assert user_lookup[103] == "Priya"

    print("PASS: User lookup test")


def test_invalid_user():
    """
    Test handling of an invalid owner ID.
    """

    user_lookup = create_user_lookup(users)

    project = {
        "id": 10,
        "name": "Test Project",
        "owner_id": 999,
        "status": "active"
    }

    result = attach_owner_names(
        [project],
        user_lookup
    )

    assert result[0]["owner"] == "Unknown"

    print("PASS: Invalid owner handling test")


def test_active_project_filter():
    """
    Test active project filtering.
    """

    active_projects = filter_active_projects(
        projects
    )

    for project in active_projects:
        assert project["status"] == "active"

    print("PASS: Active project filtering test")


def test_project_validation():
    """
    Test project validation.
    """

    valid_project = {
        "id": 20,
        "name": "Test Project",
        "owner_id": 101,
        "status": "active"
    }

    invalid_project = {
        "id": 21,
        "name": "",
        "owner_id": 101,
        "status": "active"
    }

    assert validate_project(valid_project) is True
    assert validate_project(invalid_project) is False

    print("PASS: Project validation test")


def run_tests():
    """
    Run all tests.
    """

    print("\n" + "=" * 60)
    print("RUNNING TESTS")
    print("=" * 60)

    test_user_lookup()
    test_invalid_user()
    test_active_project_filter()
    test_project_validation()

    print("\nAll tests passed successfully!")


# ============================================================
# PART 5: PERFORMANCE COMPARISON
# ============================================================

def old_lookup(project_list, user_list):
    """
    Simulates the inefficient nested-loop lookup.

    Approximate complexity:
        O(n * m)

    n = number of projects
    m = number of users
    """

    results = []

    for project in project_list:

        owner_name = "Unknown"

        for user in user_list:

            if project["owner_id"] == user["id"]:
                owner_name = user["name"]
                break

        results.append(owner_name)

    return results


def optimized_lookup(project_list, user_list):
    """
    Optimized lookup using a dictionary.

    Creating the dictionary:
        O(m)

    Looking up all projects:
        O(n)

    Overall:
        O(n + m)
    """

    user_lookup = create_user_lookup(
        user_list
    )

    results = []

    for project in project_list:

        owner_name = user_lookup.get(
            project["owner_id"],
            "Unknown"
        )

        results.append(owner_name)

    return results


def compare_performance():
    """
    Demonstrate the conceptual difference between
    the old and optimized lookup methods.
    """

    print("\n" + "=" * 60)
    print("PERFORMANCE COMPARISON")
    print("=" * 60)

    old_result = old_lookup(
        projects,
        users
    )

    optimized_result = optimized_lookup(
        projects,
        users
    )

    print("\nOld lookup result:")
    print(old_result)

    print("\nOptimized lookup result:")
    print(optimized_result)

    if old_result == optimized_result:
        print(
            "\nRESULT: Both implementations produce "
            "the same output."
        )

    print("\nOld approach complexity      : O(n * m)")
    print("Optimized approach complexity: O(n + m)")

    print(
        "\nThe optimized approach avoids repeatedly "
        "searching the complete user list."
    )


# ============================================================
# PART 6: DEBUGGING SIMULATION
# ============================================================

def debugging_report():
    """
    Display a simulated debugging report.
    """

    print("\n" + "=" * 60)
    print("DEBUGGING REPORT")
    print("=" * 60)

    print("\nIssue:")
    print(
        "Dashboard performs repeated searches for project owners."
    )

    print("\nObserved Problem:")
    print(
        "The old implementation searches the complete "
        "user list for every project."
    )

    print("\nRoot Cause:")
    print(
        "Nested loops create unnecessary repeated processing."
    )

    print("\nRefactoring Solution:")
    print(
        "Create a dictionary indexed by user ID and use "
        "constant-time average lookup."
    )

    print("\nAdditional Improvements:")
    print("- Added project validation")
    print("- Separated filtering logic")
    print("- Separated display logic")
    print("- Added error/edge-case handling")
    print("- Added automated tests")

    print("\nStatus:")
    print(
        "Issue analyzed and refactored in the simulated "
        "maintenance prototype."
    )


# ============================================================
# PART 7: MAIN PROGRAM
# ============================================================

def main():

    print("\n")
    print("*" * 60)
    print(" CAMPUSCONNECT - WEEK 5 MAINTENANCE PROTOTYPE")
    print(" Code Debugging, Refactoring & Technical Analysis")
    print("*" * 60)

    # Demonstrate old code
    old_dashboard()

    # Demonstrate refactored code
    refactored_dashboard(
        projects,
        users
    )

    # Run tests
    run_tests()

    # Compare old and optimized approaches
    compare_performance()

    # Display debugging analysis
    debugging_report()

    print("\n" + "=" * 60)
    print("WEEK 5 TASK COMPLETED")
    print("=" * 60)

    print(
        "\nThe prototype demonstrates:"
        "\n1. Code debugging"
        "\n2. Code refactoring"
        "\n3. Modularization"
        "\n4. Algorithm optimization"
        "\n5. Input validation"
        "\n6. Error handling"
        "\n7. Automated testing"
        "\n8. Performance analysis"
    )


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()