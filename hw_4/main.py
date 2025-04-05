import time
import threading
import multiprocessing
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import os
import math

def fibonacci(n):
    if n == 0:
        return 0
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b

def run_sync(n, times):
    start = time.time()
    for _ in range(times):
        fibonacci(n)
    end = time.time()
    return end - start

def run_threads(n, times):
    threads = []
    start = time.time()
    for _ in range(times):
        thread = threading.Thread(target=fibonacci, args=[n])
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    end = time.time()
    return end - start

def run_processes(n, times):
    processes = []
    start = time.time()
    for _ in range(times):
        process = multiprocessing.Process(target=fibonacci, args=[n])
        process.start()
        processes.append(process)
    for process in processes:
        process.join()
    end = time.time()
    return end - start


def gen_artifacts_1():
    n = 100000
    times = 10

    sync_time = run_sync(n, times)
    threads_time = run_threads(n, times)
    processes_time = run_processes(n, times)

    with open("artifacts/4_1/results.txt", "w") as f:
        f.write(f"sync: {sync_time}s\n")
        f.write(f"threads: {threads_time}s\n")
        f.write(f"process: {processes_time}s\n")


def integrate_chunk(f, a, step, start, end):
    acc = 0.0
    for i in range(start, end):
        acc += f(a + i * step) * step
    return acc


def integrate(f, a, b, executor_class, n_jobs=1, n_iter=10000000):
    step = (b - a) / n_iter
    chunk_size = n_iter // n_jobs
    futures = []

    with executor_class(max_workers=n_jobs) as executor:
        for i in range(n_jobs):
            start = i * chunk_size
            end = (i + 1) * chunk_size if i != n_jobs - 1 else n_iter
            futures.append(executor.submit(integrate_chunk, f, a, step, start, end))

    return sum(f.result() for f in futures)


def gen_artifacts_2():
    cpu_num = os.cpu_count()
    func = math.cos
    a, b = 0, math.pi / 2

    with open("artifacts/4_2/results.txt", "w") as f:
        for executor_class in [ThreadPoolExecutor, ProcessPoolExecutor]:
            for n_jobs in range(1, cpu_num * 2 + 1):
                start_time = time.time()
                integrate(func, a, b, executor_class, n_jobs=n_jobs)
                end_time = time.time()
                f.write(f"{executor_class.__name__}, n_jobs={n_jobs}: {end_time - start_time}s\n")


if __name__ == "__main__":
    gen_artifacts_1()
    gen_artifacts_2()
