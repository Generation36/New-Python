import threading

class Thread1(threading.Thread):
    def run(self):
        for i in range(50):
            print("Python")

class Thread2(threading.Thread):
    def run(self):
        for i in range(50):
            print("Java")

t1 = Thread1()
t2 = Thread2()

#race condition needs to avoided here:
t1.start()
t2.start()