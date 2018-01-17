from multiprocessing import Process

def f(name):
    print("Hello", name)

if __name__ == '__main__':
    p = Process(target=f, args=('Sagar',))
    p.start()
    p.join()