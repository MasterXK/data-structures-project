class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.tail = Node(None)
        self.head = Node(None, self.tail)

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        if self.head.data is None:
            self.head.data = data

        elif self.tail.data is None:
            self.tail.data = data

        else:
            node = Node(data)
            self.tail.next_node = node
            self.tail = node

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.head is None:
            return None

        data = self.head.data
        self.head = self.head.next_node

        return data

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        if self.head.data is None:
            return ''

        result = f'{self.head.data}'
        node = self.head.next_node
        while node:
            data = node.data
            result = f'{result}\n{data}'
            node = node.next_node

        return result
