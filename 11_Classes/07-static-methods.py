# Методы, которые являются общими для класса и всех экземпляров класса
# и не имеют доступ к данным экземпляров классов, называются
# статическими методами.
#
# Для создания статических методов используется декоратор
# staticmethod.
#
# Декоратор – это специальная функция, которая изменяет поведение
# функции или класса. Для применения декоратора следует перед
# соответствующим объявлением указать символ @, имя необходимого
# декоратора и список его аргументов в круглых скобках.
# Если передача параметров декоратору не требуется, скобки не указываются.


class MyClass:
    # Объявление атрибута класса
    class_attribute = 8

    # Конструктор
    def __init__(self):
        self.data_attribute = 42

    # Статический метод. Обратите внимание, что у него нет параметра
    # self, поскольку он не связан ни с одним из экземпляров класса
    # не имеет доступа к атрибутам-данным
    @staticmethod
    def static_method():
        print(MyClass.class_attribute)

    # Обычный метод
    def instance_method(self):
        print(self.data_attribute)


if __name__ == '__main__':
    # Вызов статического метода
    MyClass.static_method()
    # Инстанцирование объекта
    obj = MyClass()
    # Вызов метода
    obj.instance_method()
    # Аналогично атрибутам класса, доступ ко статическим методам
    # можно получить и через экземпляр класса
    obj.static_method()