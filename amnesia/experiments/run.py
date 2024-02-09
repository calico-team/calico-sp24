import subprocess
import sys


def main():
    # if len(sys.argv) != 2:
    #     _print_err('Incorrect number of arguments')
    #     exit(1)
    
    # _, path_to_program = sys.argv
    path_to_program = 'incr'
    REPS = 5
    for i in REPS:
        subprocess.run([f"./{path_to_program}"], timeout=1)
        print(f"Finished Rep {i}")

if __name__ == '__main__':
    main()
