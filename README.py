import time

def focus_timer(duration):
    start_time = time.time()
    end_time = start_time + duration * 60

    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        minutes = remaining_time // 60
        seconds = remaining_time % 60
        time_str = "{:02d}:{:02d}".format(minutes, seconds)
        print("\rFocus Time: {}".format(time_str), end="")
        time.sleep(1)

    print("\nTime's up! Your focus session is over.")

# 设置专注时长为25分钟（可以根据需要进行调整）
focus_duration = 60

print("Focus Timer - {} minutes".format(focus_duration))
focus_timer(focus_duration)
