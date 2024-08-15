import random
import threading
import time


class UserManager:
    def __init__(self):
        self.users = {}

    def update_user_data(self, user_id, new_value):
        # Đọc giá trị hiện tại
        current_value = self.users.get(user_id, None)
        
        # Giả lập một số xử lý
        time.sleep(0.1)
        
        # Cập nhật giá trị mới
        self.users[user_id] = new_value
        print(f"Updated user {user_id} from {current_value} to {new_value}")
        
        return new_value

input_values = [1,5,8,9,0]

def worker(user_manager, user_id, worker_id):
    for i in range(5):
        new_value = input_values[i]
        result = user_manager.update_user_data(user_id, new_value)
        print(f"Worker {worker_id}: Updated user {user_id} to {result}")
        time.sleep(random.uniform(0.1, 0.5))  # Random delay

user_manager = UserManager()
user_id_to_update = "user123"

# Tạo hai thread cùng cập nhật một user
thread1 = threading.Thread(target=worker, args=(user_manager, user_id_to_update, 1))
thread2 = threading.Thread(target=worker, args=(user_manager, user_id_to_update, 2))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

final_value = user_manager.users.get(user_id_to_update)
print(f"Final value for user {user_id_to_update}: {final_value}")