import time
import threading

START = 0
END = 100_000_001
LAUNCH_CODE = 100_000_000

def threaded_function(START, END, increment):
    begin_time = time.time()
    for i in range(START, END, increment):
        if i == LAUNCH_CODE:
            print("Global Thermonuclear War Initiated")
            print(f"Total time = {round(time.time() - begin_time, 3)}")
            return
        

def main():
    

    num_threads = 10
    increment = END // num_threads

    t = threading.Thread(target=threaded_function, args=(START, END, increment))
    t.start()
    t.join()


if __name__ == "__main__":
    print("begin")
    main()