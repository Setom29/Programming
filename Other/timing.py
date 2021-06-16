"""https://digitology.tech/posts/funktsii-taiminga-python-tri-sposoba-kontrolirovat-vash-kod/"""
"""
Пример работы кода:
>>> t = Timer()
>>> t.start()

>>> t.stop()   Несколько секунд спустя
Elapsed time: 3.8191 seconds
"""
import time


class TimerError(Exception):
    """Пользовательское исключение, используемое для сообщения об ошибках при использовании класса Timer"""

    def __init__(self):
        self._start_time = None

    def start(self):
        """Запуск нового таймера"""

        if self._start_time is not None:
            raise TimerError(f"Таймер уже работает. Используйте .stop() чтобы его остановить")

        self._start_time = time.perf_counter()

    def stop(self):
        """Остановка таймера и сообщение о времени вычисления"""
        if self._start_time is None:
            raise TimerError(f"Таймер не работает. Используйте .start() чтобы его запустить")
        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        print(f"Вычисление заняло {elapsed_time:0.4f} секунд")
