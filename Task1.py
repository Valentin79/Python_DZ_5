
# Напишите функцию, которая принимает на вход
# строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов:
# путь, имя файла, расширение файла.

str = "C:/music/my_playlist/higher.mp3"


def func(str):
    a, b = str.split(".")
    *path, name = a.split("/")
    path = "/".join(path)
    return (path, name, b)

print(func(str))