import random
import threading
import time


class UserManager:
    def __init__(self):
        self.users = {}
        self.user_locks = {}
        self.lock_for_new_users = threading.Lock()

    def get_user_lock(self, user_id):
        with self.lock_for_new_users:
            if user_id not in self.user_locks:
                self.user_locks[user_id] = threading.Lock()
            return self.user_locks[user_id]

    def update_user_data(self, user_id, new_value):
        user_lock = self.get_user_lock(user_id)
        with user_lock:
            self.users[user_id] = new_value
            print(f"Updated user {user_id} with value {new_value}")
            time.sleep(2)  # Giả lập thời gian xử lý
            return self.users[user_id]

    def get_user_data(self, user_id):
        user_lock = self.get_user_lock(user_id)
        with user_lock:
            return self.users.get(user_id, None)

def worker(user_manager, user_id, worker_id):
    for _ in range(5):
        new_value = random.randint(1, 100)
        result = user_manager.update_user_data(user_id, new_value)
        print(f"Worker {worker_id}: Updated user {user_id} to {result}")
        time.sleep(random.uniform(0.1, 0.5))  # Random delay

user_manager = UserManager()
user_id_to_update = "user123"
user_id2_to_update = "user2"

# Tạo hai thread cùng cập nhật một user
thread1 = threading.Thread(target=worker, args=(user_manager, user_id_to_update, 1))
thread2 = threading.Thread(target=worker, args=(user_manager, user_id_to_update, 2))
thread3 = threading.Thread(target=worker, args=(user_manager, user_id2_to_update, 3))

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

final_value = user_manager.get_user_data(user_id_to_update)
print(f"Final value for user {user_id_to_update}: {final_value}")