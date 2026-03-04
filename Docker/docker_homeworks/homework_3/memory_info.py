import psutil
import platform


def get_cpu_usage():
    return psutil.cpu_percent(interval=1)


def get_memory_usage():
    memory = psutil.virtual_memory()
    return {
        "Всего": f"{memory.total / (1024**3):.2f} GB",
        "Используется": f"{memory.used / (1024**3):.2f} GB",
        "Свободно": f"{memory.available / (1024**3):.2f} GB",
        "Процент использования": f"{memory.percent}%"
    }


def main():
    with open("data/output.txt", "w") as f:
        print("OS:", platform.platform(), file=f)
        print("OS version:", platform.version(), file=f)
        print("=== Мониторинг системы ===", file=f)

        print(f"\nCPU usage: {get_cpu_usage()}%", file=f)

        print("\nMemory usage:", file=f)

        for key, value in get_memory_usage().items():
            print(f"{key}: {value}", file=f)


if __name__ == "__main__":
    main()