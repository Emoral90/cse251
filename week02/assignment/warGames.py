import time
START = 0
END = 100_000_001
LAUNCH_CODE = 100_000_000

def main():
    begin_time = time.time()

    for i in range(START, END):
        if i == LAUNCH_CODE:
            print("Global Thermonuclear War Initiated")
            print(f"Total time = {round(time.time() - begin_time, 3)}")
            return

if __name__ == "__main__":
    print("begin")
    main()