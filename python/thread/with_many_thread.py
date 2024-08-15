import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='[Thread %(thread)d] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def thread_function(name):
    logging.info(f"Starting {name}")
    time.sleep(10)
    logging.info(f"End {name}")

if __name__ == "__main__":
    threads = []
    for index in range(3):
        logging.info(f"Create thread {index}")
        thread = threading.Thread(target=thread_function, args=(index,), daemon=True)
        threads.append(thread)
        logging.info(f"Start thread {index}")
        thread.start()

    for index, thread in enumerate(threads):
        logging.info(f"Main Before join {index}")
        thread.join()
        logging.info(f"Main {index} thread done")
    
    """
    Result with End thread index vary from run to run 
    -> Order of thread execution managed by os is hard to predict
    
    """