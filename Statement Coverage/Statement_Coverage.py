import inspect
import sys
import os
import threading
import time

class StatementCoverage:
    def __init__(self, source_file):
        with open(source_file, 'r') as f:
            self.lines = f.readlines()
        self.covered_lines = set()

    def track_line(self, line_number):
        if 1 <= line_number <= len(self.lines):
            self.covered_lines.add(line_number)

    def print_coverage(self, input_description):
        print(f"Coverage for input: {input_description}")
        for i, line in enumerate(self.lines, 1):
            prefix = '  ' if i in self.covered_lines else '# '
            print(f"{prefix}{i} {line.rstrip()}")

def run_with_coverage(program_func, coverage, *args, **kwargs):
    frame = inspect.currentframe()
    try:
        def traceit(frame, event, arg):
            if event == 'line':
                coverage.track_line(frame.f_lineno)
            return traceit

        sys.settrace(traceit)
        result = program_func(*args, **kwargs)
    finally:
        sys.settrace(None)
    
    return result

def run_with_timeout(func, timeout=120):
    result = [None]
    exception = [None]

    def wrapper():
        try:
            result[0] = func()
        except Exception as e:
            exception[0] = e

    thread = threading.Thread(target=wrapper)
    thread.start()
    thread.join(timeout)

    if thread.is_alive():
        raise TimeoutError("Function execution timed out")
    
    if exception[0]:
        raise exception[0]
    
    return result[0]

def example_program(coverage):
    coverage.track_line(inspect.currentframe().f_lineno)
    x = 10
    
    coverage.track_line(inspect.currentframe().f_lineno)
    if x > 5:
        coverage.track_line(inspect.currentframe().f_lineno)
        return x * 2
    
    return x

def main():
    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit(1)
    source_file =  sys.argv[1] #r'c:\Users\EndUser\Downloads\Software Testing and Analysis\test_input.py'
    #os.path.abspath(__file__)
    
    coverage = StatementCoverage(source_file)
    program_input = input("Provide the input to run the program file given: ") #[-23, 0, 6, -4, 34]
    try:
        result = run_with_coverage(lambda: run_with_timeout(lambda: example_program(coverage)), coverage)
        coverage.print_coverage(input)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
