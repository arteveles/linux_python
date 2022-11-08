import subprocess
import numpy
import datetime
from scripts import PS_AUX
from scripts import UNIQ_USERS
from scripts import COUNT_PROC
from scripts import EACH_USER_PROC
from scripts import MEMORY_USAGE
from scripts import MAX_MEM
from scripts import MAX_CPU
from scripts import CPU_USAGE


def now_time():
    return datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


def system_info(value):
    all_info = subprocess.Popen(
        f"{PS_AUX} {value}",
        shell=True,
        stdout=subprocess.PIPE)
    out = all_info.stdout.readlines()
    return out


def decode(value):
    return numpy.char.decode(value)


def strip(value):
    return numpy.char.strip(value, "\n")


def users():
    user = system_info(UNIQ_USERS)
    output = decode(strip(user))
    for items in output:
        return items


def count_process():
    process = system_info(COUNT_PROC)
    output = decode(strip(process))
    for items in output:
        return items


def user_proc():
    user_proc = system_info(EACH_USER_PROC)
    output = decode(user_proc)
    for items in output:
        return items


def memory():
    process = system_info(MEMORY_USAGE)
    output = decode(strip(process))
    for items in output:
        return items


def cpu():
    cpu = system_info(CPU_USAGE)
    output = decode(strip(cpu))
    for items in output:
        return items


def memory_max():
    mem_max = system_info(MAX_MEM)
    output = decode(strip(mem_max))
    return output[1][:21]


def cpu_max():
    cpu_max = system_info(MAX_CPU)
    output = decode(strip(cpu_max))
    return output[1][:21]


def write_to_file(value):
    with open(f"{now_time()}.txt", "w+") as file:
        file.write(value)
        file.close()


if __name__ == "__main__":
    """Count processes"""
    write_to_file(
        f"Пользователи системы: {users()}"
        f"\nПроцессов запущено: {count_process()}"
        f"\nПользовательских процессов: {user_proc()}"
        f"\nВсего памяти используется, %: {memory()}"
        f"\nВсего CPU используется, %: {cpu()}"
        f"\nБольше всего памяти использует: {memory_max()}"
        f"\nБольше всего CPU использует: {cpu_max()}"
    )
