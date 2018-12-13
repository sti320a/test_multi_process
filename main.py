import subprocess
import time


def run_multi_sleep():
    def run_sleep():
        proc = subprocess.Popen(['python', 'run_sleep.py'])
        return proc

    start = time.time()
    procs = []

    for _ in range(10):
        procs.append(run_sleep())

    for proc in procs:
        proc.communicate()

    end = time.time()

    print("Finished in {} seconds".format(end-start))

run_multi_sleep()