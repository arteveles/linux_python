import array
import os
import subprocess
import jc
import numpy
import datetime


def now_time():
    return datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


def system_info(value):
    all_info = subprocess.Popen(
        f"ps aux {value}",
        shell=True,
        stdout=subprocess.PIPE)
    out = all_info.stdout.readlines()
    return out


def decode(value):
    return numpy.char.decode(value)


def strip(value):
    return numpy.char.strip(value, "\n")


def users():
    user = system_info("""| awk 'NR>1{tot[$1]++;} END{for(id in tot) printf "%s, ", id}'""")
    output = decode(strip(user))
    for items in output:
        return items


def count_process():
    process = system_info("| awk '{print $2}' | wc -l")
    output = decode(strip(process))
    for items in output:
        return items


def user_proc():
    user_proc = system_info("""| awk 'NR>1{tot[$1]++;} END{for(id in tot) printf "%s = %s, ", id, tot[id]}'""")
    output = decode(user_proc)
    for items in output:
        return items

def memory():
    process = system_info(" --sort pmem | awk '{print $4}' | grep -v %MEM")
    output = decode(strip(process))
    # res_sum = numpy.sum([output])
    for items in output:
        print(items)


def write_to_file(value):
    with open(f"{now_time()}.txt", "w+") as file:
        file.write(value)
        file.close()


# def count_proc():
#     return system_info(f"")


if __name__ == "__main__":
    """Count processes"""
    write_to_file(
        f"Пользователи системы: {users()}"
        f"\nПроцессов запущено: {count_process()}"
        f"\nПользовательских процессов: {user_proc()}"
        f"\nВсего памяти используется: {memory()}"
    )

    # print(f"Процессов запущено: {count_proc()}")
