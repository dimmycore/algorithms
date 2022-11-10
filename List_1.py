# Сейчас мы попробуем создать класс LinkedList, реализующий список.
# Элементы списка будут представлять собой экземпляры класса Node.
class Node:
    def __init__(self, value = None, next_ = None):
        self.value = value
        self.next = next_

    def __str__(self):
        return 'Node value' + str(self.value)

class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def clear(self):
        self.__init__()

    def __str__(self):
        R = ''

        pointer = self.first
        while pointer is not None:
            R += str(pointer.value)
            pointer = pointer.next
            if pointer is not None:
                R += ''
        return R
    
  # Мы определили класс Node. Конструктор этого класса принимает значение элемента и ссылку на следующий элемент. По умолчанию они оба None.
# Также был определен метод __str__, который используется для строкового представления объекта.

# Также был определен основной класс LinkedList. Конструктор метода инициализирует ссылки на первый и на последний элемент,
# а также определяется метод clear, который очищает список.

# Сейчас шаг за шагом добавим методы, которые мы вспомнили в предыдущем задании. На первом шаге добавим метод pushleft, 
# который вставляет новый элемент в начало списка. 
    
    

    def pushleft(self, value):
        if self.first is None:
            self.first = Node(value)
            self.last = self.first
        else:
            new_node = Node(value, self.first)
            self.first = new_node

    def pushright(self, value):
        if self.first is None:
            self.first = Node(value)
            self.last = self.first
        else:
            new_node = Node(value)
            self.last.next = new_node
            self.last = new_node

    def popleft(self):
        if self.first is None:  # если список пустой, возвращаем None
            return None
        elif self.first == self.last:  # если список содержит только один элемент
            node = self.first  # сохраняем его
            self.__init__()  # очищаем
            return node  # и возвращаем сохраненный элемент
        else:
            node = self.first  # сохраняем первый элемент
            self.first = self.first.next  # меняем указатель на первый элемент
            return node  # возвращаем сохраненный

    def popright(self):
        if self.first is None:  # если список пустой, возвращаем None
            return None
        elif self.first == self.last:  # если список содержит только один элемент
            node = self.first  # сохраняем его
            self.__init__()  # очищаем
            return node  # и возвращаем сохраненный элемент
        else:
            node = self.last  # сохраняем последний
            pointer = self.first  # создаем указатель
            while pointer.next is not node:  # пока не найдем предпоследний
                pointer = pointer.next
            pointer.next = None  # обнуляем указатели, чтобы
            self.last = pointer  # предпоследний стал последним
            return node  # возвращаем сохраненный


LL = LinkedList()

LL.pushright(1)
LL.pushleft(2)
LL.pushright(3)
LL.popright()
LL.pushleft(4)
LL.pushright(5)
LL.popleft()

print(LL)
