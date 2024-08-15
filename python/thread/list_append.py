import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] [Thread %(thread)d] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
def thread_append(thread_num, list_to_append):
    logging.info(f"{thread_num} start")
    logging.info(list_to_append)
    time.sleep(1)
    list_to_append.append(thread_num)
    logging.info(f"{thread_num} done")

if __name__ == "__main__":
    list_to_append = []
    threads = []
    for i in range(10):
        logging.info(f"Main : Create Thread {i}")
        thread = threading.Thread(target=thread_append, args=(i, list_to_append))
        threads.append(thread)
        logging.info(f"Main : Start Thread {i}")
        thread.start()
    
    for index, thread in enumerate(threads):
        logging.info(f"Main Before join {index}")
        thread.join()
        logging.info(f"Main {index} thread done")
    print(list_to_append)