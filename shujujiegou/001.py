class Node(object):
    '''节点类'''
    def __init__(self,item):
        # 一个变量记录数据内容
        self.item = item
        # 一个变量记录下一个节点对象
        self.next = None

class SingleLinkList(object):
    '''单链表'''
    def __init__(self):
        '''初始化链表'''
        self.__head = None

    def is_empty(self):
        '''判断链表是否为空'''
        return self.__head is None
    
    def length(self):
        '''链表长度'''
        # cur初始指向头节点
        cur = self.__head
        # 初始化长度为0
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count


    def travel(self):
        '''遍历链表'''
        # 从首节点开始遍历
        cur = self.__head
        while cur is not None:
            print(cur.item)
            cur = cur.next

    def add(self,item):
        '''链表头部添加元素'''
        # 创建一个保存item值的节点
        node = Node(item)
        # 让新的头节点记录老的头节点
        node.next = self.__head
        # 让首节点记录新的节点
        self.__head = node

    def append(self,item):
        '''链表尾部添加元素'''
        node = Node(item)

        # 判断如果为空
        if self.is_empty():
            self.__head = node
        # 如果不为空，在尾部添加
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node


    def remove(self):
        '''链表删除元素'''


if __name__ == '__main__':
    sll = SingleLinkList()
    print(sll.is_empty())

    sll.add(3)
    sll.add(2)
    sll.add(5)
    print(sll.is_empty())
    
    sll.travel()

    print(sll.length())

    sll.append(8)

