from sh import ping
from sys import argv, exit

def process_output(line, stdin, process):
    print(f'{line = }')
    #print(stdin)
    #print(process)

def call_ping(target):
    pc = ping('-c10',target,_bg=True,_err = process_output, _out = process_output)
    pc.wait()

if __name__ == '__main__':
    if len(argv) < 2:
        exit(-1)
    call_ping(argv[1])
