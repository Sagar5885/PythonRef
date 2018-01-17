from multiprocessing import Process
import os

def info(title):
    print(title)
    print('Module Name: ', __name__)
    print('Parent Process Id: ', os.getppid())
    print('Process Id: ', os.getpid())

def f(name):
    info('function f')
    print("Hello", name)

if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('Sagar',))
    p.start()
    p.join()