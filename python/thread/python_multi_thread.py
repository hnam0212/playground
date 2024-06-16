from threading import Lock, Thread
from time import sleep

counter = 0
lock = Lock()
def increase(by):
    global counter
    with lock:
        local_counter = counter
        local_counter += by
        sleep(0.01)
        counter = local_counter
        print(f'counter={counter}')

def increase_without_lock(by):
    global counter

    local_counter = counter
    local_counter += by

    sleep(0.1)

    counter = local_counter
    print(f'counter={counter}')



# create threads
t1 = Thread(target=increase, args=(10,))
t2 = Thread(target=increase, args=(20,))

# start the threads
t1.start()
t2.start()


# wait for the threads to complete
t1.join()
t2.join()


print(f'The final counter is {counter}')


"""
With lock: output return counter = 30 => correct
Without lock: output return counter = 20 
=> Explain:
- counter is a global variable
Thread 1 take counter = 0 and + 10 but it have to sleep
-> Thread 2 take intepreter => +20 at that time counter variable is till 0 , thread 2 sleep
-> Thread 1 take back intepreter => assign counter = 10
-> Thread 2 take back intepreter and assign it to 20

=> counter = 20

Summary: 
- Apply lock in case we have multiple thread trying to modify a single global variable
- Lock doesn't lock any object, it just lock the thread execution
- GIL is only itself intepreter thread-safe, it only protect the interpreter internally

"""