import platform
import GPUtil
import psutil
import argparse
parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('-a', '--all_information', action='store_true', help='Вся информация')
parser.add_argument('-r', '--memory', action='store_true', help='Оперативная память')
parser.add_argument('-c', '--сpu', action='store_true', help='Процессор')
parser.add_argument('-s', '--storage', action='store_true', help='Накопитель')
parser.add_argument('-g', '--gpu', action='store_true', help='Видеокарта')

def info():
    print(f"\nОперационная система:{platform.system()}")
    print(f"Сетевое имя компьютера:{platform.node()}\n")

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def memory_info():
    svmem = psutil.virtual_memory()
    print("\nОперативная память")
    print(f'Всего оперативной памяти: {get_size(svmem.total)}')
    print(f'Доступной: {get_size(svmem.available)}')
    print(f'Занятой: {get_size(svmem.used)}')

def cpu_info():
    print("\nПроцессор:", platform.processor())
    print(f"Физических ядер:", psutil.cpu_count(logical=False))
    print("Всего ядер:", psutil.cpu_count(logical=True))
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print(f"Ядер {i}: {percentage}%")

def storage_info():
    print(
        f"\nЖесткий диск(Общее, используемое и свободное пространство в байтах, использование в процентах):{str(psutil.disk_usage('/'))}")

def gpu_info():
    gpus = GPUtil.getGPUs()
    list_gpus = []
    for gpu in gpus:
        gpu_name = gpu.name
        gpu_total_memory = f"{gpu.memoryTotal}MB"
        gpu_temperature = f"{gpu.temperature} °C"
        gpu_uuid = gpu.uuid
        print("\nНазвание: ", gpu_name)
        print("Память: ", gpu_total_memory)
        print("Температура: ", gpu_temperature)
        print("UUID: ", gpu_uuid)

args = parser.parse_args()

if args.all_information:
    info()
    memory_info()
    cpu_info()
    storage_info()
    gpu_info()

if args.memory:
    memory_info()

if args.сpu:
    cpu_info()

if args.storage:
    storage_info()

if args.gpu:
    gpu_info()
