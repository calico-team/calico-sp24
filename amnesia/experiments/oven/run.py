import subprocess
import sys


def main():
    # if len(sys.argv) != 2:
    #     _print_err('Incorrect number of arguments')
    #     exit(1)
    
    # _, path_to_program = sys.argv
    path_to_program = 'increment'
    REPS = 1000
    next_input = str(1)
    for i in range(REPS):
        if i % 1000 == 0:
            print(i)
        cp = subprocess.run([f"./{path_to_program}"], input=next_input, text=True, capture_output=True, shell=True)
        next_input = cp.stdout
        # print(f"cp obj {cp}")
        # print(f"Finished Rep {i}")

if __name__ == '__main__':
    main()
