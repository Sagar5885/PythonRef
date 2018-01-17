import threading
import time
from pip._vendor.distlib.compat import raw_input


class AsyncWrite(threading.Thread):
    def __init__(self, text, out):
        threading.Thread.__init__(self)
        self.text = text
        self.out = out

    def run(self):
        f = open(self.out, 'a')
        f.write(self.text + '\n')
        f.close()
        time.sleep(2)
        print("Finished Background file write to "+self.out)


def main():
    message = raw_input("Enter a string to store: ")
    background = AsyncWrite(message, 'out.txt')
    background.start()
    print("Program can continue to run while it write in another therad!")

    print(100+400)
    background.join()
    print("Waited until thread was finished!")

if __name__ == '__main__':
    main()