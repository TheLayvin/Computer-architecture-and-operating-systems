import threading
import time
import random

sensors = {}
lock = threading.Lock()


def sensor(name):
    for i in range(5):
        value = random.randint(0, 100)

        with lock:
            sensors[name] = value
            print(f"{name} оновив значення: {value}")

        time.sleep(0.5)


def monitor():
    for i in range(5):
        time.sleep(1)

        with lock:
            if sensors:
                avg = sum(sensors.values()) / len(sensors)
                print("Поточні дані:", sensors)
                print("Середнє значення:", avg)


def main():
    t1 = threading.Thread(target=sensor, args=("Датчик 1",))
    t2 = threading.Thread(target=sensor, args=("Датчик 2",))
    t3 = threading.Thread(target=sensor, args=("Датчик 3",))

    t1.start()
    t2.start()
    t3.start()

    monitor_thread = threading.Thread(target=monitor)
    monitor_thread.start()

    t1.join()
    t2.join()
    t3.join()
    monitor_thread.join()

    print("Моніторинг завершено")


if __name__ == "__main__":
    main()