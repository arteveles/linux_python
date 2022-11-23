from subprocess import run, PIPE
import datetime
import pandas as pd

res = run(['ps', 'aux'], stdout=PIPE)
procs = res.stdout.decode().split('\n')
titles = procs[0].split()

"""Pandas data"""
# df = pd.DataFrame(procs)

sum = 0
max_cpu = 0
max_mem = 0
max_cpu_1 = 0
max_mem_1 = 0
pid = ''
max_cpu_proc = ''
max_mem_proc = ''
user = 'USER'
pid_list = []
count_mem = []
count_cpu = []
pid_user_list = []
uniq_user_result = []

for p in procs[1:]:

    if not p == '':
        chunks = p.split(maxsplit=len(titles))
        proc_cpu = float(chunks[titles.index('%CPU')])
        proc_mem = float(chunks[titles.index('%MEM')])
        chunk_user = str(chunks[titles.index('USER')])
        chunk_pid = str(chunks[titles.index('PID')])

        if chunk_pid != pid:
            pid = chunk_pid
            uniq_pid = chunks[titles.index('PID')]
            pid_list.append(uniq_pid)
            result_count = pd.Series(pid_list).count()

        if chunk_user != user:
            user = chunk_user
            uniq_user = chunks[titles.index('USER')]
            uniq_user_result.append(uniq_user)
            unique_use = pd.Series(uniq_user_result).unique().tolist()

        if chunk_user >= "":
            user = chunk_user
            uniq_user = chunks[titles.index('USER')]
            pid_user_list.append(uniq_user)
            dictionary = {}
            for item in pid_user_list:
                dictionary[item] = dictionary.get(item, 0) + 1

        if proc_cpu >= max_cpu:
            max_cpu = proc_cpu
            max_cpu_proc = chunks[titles.index('COMMAND')]

        if proc_mem >= max_mem:
            max_mem = proc_mem
            max_mem_proc = chunks[titles.index('COMMAND')]

        if proc_mem >= max_mem or proc_mem <= max_mem:
            max_mem_1 = proc_mem
            count_mem_proc = chunks[titles.index('%MEM')]
            count_mem.append(count_mem_proc)
            sum_m = pd.Series(count_mem, dtype="float64").sum()

        if proc_cpu >= max_cpu or proc_cpu <= max_cpu:
            max_cpu_1 = proc_cpu
            max_cpu_proc_1 = chunks[titles.index('%CPU')]
            count_cpu.append(max_cpu_proc_1)
            sum_c = pd.Series(count_cpu, dtype="float64").sum()


def now_time():
    return datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


with open(f"{now_time()}.txt", "w+") as file:
    file.write(
        f"Пользователи системы: {unique_use}"
        f"\nПроцессов запущено: {result_count}"
        f"\nПользовательских процессов: {dictionary}"
        f"\nВсего MEM используется, %: {sum_m}"
        f"\nВсего CPU используется, %: {sum_c}"
        f"\nБольше всего MEM использует: {max_mem} ({max_mem_proc[:20]})"
        f'\nБольше всего CPU использует:  {max_cpu} ({max_cpu_proc[:20]})'
    )
    file.close()
