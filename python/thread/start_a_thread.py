import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='[Thread %(thread)d] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def thread_function():
    logging.info("Starting")
    time.sleep(2)
    logging.info("End")


if __name__ == "__main__":
    logging.info("First")
    logging.info("Create thread")
    thread = threading.Thread(target=thread_function)
    logging.info("Before start")
    thread.start()
    logging.info("wait for thread to finish")
    thread.join()
    logging.info("all done")
    