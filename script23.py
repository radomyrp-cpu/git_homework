import colorama
import inspect



print("Name:", colorama.__name__)
print("Module:", inspect.ismodule(colorama))
print("Function:", inspect.isfunction(colorama.init))
print("Class:", inspect.isclass(colorama.AnsiToWin32))
print(hasattr(colorama, "Fore"))
print(callable(colorama.init))
# Смотрим что есть в библиотеке
for name in dir(colorama):
    print(name)
# фор хранит цвета текста
print("Fore:", dir(colorama.Fore))
#  бек хранит цвета фона
print("Back:", dir(colorama.Back))
# стайл хранит варианты яркости и сброс оформления
print("Style:", dir(colorama.Style))
# инит настраивает вывод, strip=False оставляет коды цветов
colorama.init(strip=False)
# рєд делает текст красным
# RESET_ALL сбрасывает цвет текста, фон и яркость
print(colorama.Fore.RED + "Helo" + colorama.Style.RESET_ALL)
# гринн в Back делает фон зелёным
print(colorama.Back.GREEN + "Hello" + colorama.Style.RESET_ALL)
# брайт делает текст ярким
print(colorama.Style.BRIGHT + "Hello" + colorama.Style.RESET_ALL)
print("Normal text")
# денаид возвращает исходные потоки вывода
colorama.deinit()