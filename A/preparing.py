import sys

if __name__ == '__main__':
    out_file = sys.argv[1]
    file = open(out_file, "w")
    file.write('#include <iostream>\nvoid print_A() {\nstd::cout<<"Hello from A";} ')
    file.close
