import subprocess


def run_tests():
    """
    Run unit tests using either unittest or pytest based on user input.
    """
    test_framework = input("Choose test engine (unittest/pytest): ").lower()

    if test_framework == "unittest":
        command = ["python", "-m", "unittest", "discover", "-s", ".", "-v"]
    elif test_framework == "pytest":
        command = ["python", "-m", "pytest", "-v"]
    else:
        print("Invalid option. Select 'unittest' o 'pytest'.")
        return

    subprocess.run(command)


if __name__ == "__main__":
    run_tests()
