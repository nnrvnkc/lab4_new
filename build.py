import subprocess
import sys

def run_tests():
    result = subprocess.run([sys.executable, '-m', 'unittest', 'discover'])
    if result.returncode != 0:
        print("Тести не пройдено :(")
        sys.exit(result.returncode)
    print("Усі тести пройдено успішно :)\n")

def build_artifact():
    subprocess.check_call([sys.executable, 'setup.py', 'sdist', 'bdist_wheel'])

def main():
    run_tests()
    build_artifact()

if __name__ == "__main__":
    main()
