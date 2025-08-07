class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next: ListNode | None = None

class BasicOperationListNode:
    def Create_List(self, num: int, L: ListNode) -> ListNode: # 创建链表
        L_new = L
        for i in range(num):
            number = int(input('Please give me a number to add to the ListNode: '))
            P = ListNode(number)
            L_new.next = P
            L_new = P
        return L
    
    
    def Delete_ListNode(self,target:int , L:ListNode) -> ListNode: #删除值为3的节点
        L_new = L
        if(L_new.next == None ): #如果链表为空，直接返回None
            return ListNode 
        else:
            while(L_new.next != None): 
                if(L_new.next.val == target): 
                    p = L_new.next 
                    p1 = p.next 
                    L_new.next = p1 
                    L_new = L_new.next 
        return L 
    def Inset_ListNode(self,idex:int,val:int,L:ListNode ) -> ListNode:#在不包括头结点的第idex个节点后面插入一个值为val的节点
        L_new = L
        for i in range(idex):
            L_new = L_new.next
        P = ListNode(val)
        P1 = L_new.next
        L_new.next = P
        P.next = P1

    def SearchList(self,target:int,L:ListNode)-> ListNode:# 返回查找值为val的那个节点
        L_new = L
        while(L_new.val != target):
            L_new = L_new.next
        return L_new

            

def print_(head :ListNode):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next               

print('初始化链表\n') 
head = ListNode(1)
op = BasicOperationListNode()
print('#########################创建一个3个节点的链表##############################################')
op.Create_List(3, head) 
print_(head)
print('\n')
print('################################插入节点####################################################')
op.Inset_ListNode(2,3,head)
print('\n')
print_(head)
print('\n')
print('################################删除节点####################################################')
op.Delete_ListNode(3,head)
# 打印链表验证
print('\n')
print_(head)
print('\n')
print('################################查找####################################################')
L = op.SearchList(2,head)
print( L)

