

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class QuickSortLinkedList:
    def __init__(self):
        self.head=None
    def addNode(self,data):
        if (self.head == None):
            self.head = Node(data)
            return
        curr = self.head
        while (curr.next != None):
            curr = curr.next
        newNode = Node(data)
        curr.next = newNode

    def printList(self,n):
    
        j=1
        while (n != None):
            print(j,". Vehicle Register Number:",n.data[4],"  Liscence Number:",n.data[3],"  Name:",n.data[1]," Age:",n.data[0]," Time of charge:",n.data[2],"\n")
            n = n.next
            j=j+1
    def paritionLast(self,start, end):
        if (start == end or start == None or end == None):
            return start
        pivot_prev = start
        curr = start
        pivot = end.data
        while (start != end):
            if (start.data < pivot):
                pivot_prev = curr
                temp = curr.data
                curr.data = start.data
                start.data = temp
                curr = curr.next
            start = start.next
        temp = curr.data
        curr.data = pivot
        end.data = temp
        return pivot_prev
    def sort(self, start, end):
        if(start == None or start == end or start == end.next):
            return
        pivot_prev = self.paritionLast(start, end)
        self.sort(start, pivot_prev)
        if(pivot_prev != None and pivot_prev == start):
            self.sort(pivot_prev.next, end)
        elif (pivot_prev != None and pivot_prev.next != None):
            self.sort(pivot_prev.next.next, end)

if __name__ == "__main__":
    ll = QuickSortLinkedList()
    ll.addNode(['18','Raghav','2:20','ABC201902','TN 09 PA 8978'])
    ll.addNode(['20','Rahul','4:20','ABC201908','TN 09 BA 8288'])
    ll.addNode(['19','Lokesh','13:25','ABC202028','TN 09 LA 8489'])
    ll.addNode(['48','Jadhhav','11:40','ABC200247','TN 09 PA 7848'])
    ll.addNode(['18','Adhava','5:20','ABC202007','TN 09 IO 8778'])
    n = ll.head
    while (n.next != None):
        n = n.next
        
    print("\nRecords before sorting")
    ll.printList(ll.head)
    ll.sort(ll.head, n)
    print("\nRecords after sorting");
    ll.printList(ll.head)
	

