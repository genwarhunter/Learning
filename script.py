import sys
import os
import time
import pause


log_file = './file.log'
workers = []

def main():
    if len(sys.argv) < 7:
        print('недостаточно аргументов, \n Пример запуска: python3 script.py -m message, -p 2 -s 2')
        exit()
    message = sys.argv[sys.argv.index('-m')+1]
    processes = int(sys.argv[sys.argv.index('-p')+1])
    iterations = int(sys.argv[sys.argv.index('-i')+1])
    for i in range(processes):
        print(f'P {os.getpid()}: Forking {i}')
        worker_pid = os.fork()
        if not worker_pid:
            now = time.time()
            pause.until(now+iterations*i)
            for j in range(iterations):
                with open(log_file, mode='a+') as file:
                    file.write(f'C {i}: {message} {j+1}\n')
            os.abort()
        workers.append(worker_pid)

    for pid in workers:
        print(f'P: Waiting for {pid}')
        done = os.waitpid(pid, 0)

if __name__ == "__main__":
    try:
        main() 
    except Exception:
        for i in workers:
            os.kill(i)    
