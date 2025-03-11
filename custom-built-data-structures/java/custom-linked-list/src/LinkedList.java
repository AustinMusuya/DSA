// 10 ---> 50 ---> 40 ---> null

// Creating a simple structure of how we want our linkedlist to be
// head being the start then value and pointer to the next node

// Approach: Create a class that takes the value as the constructor parameter.
// Next create a class variable (head) of an object that takes the value and has a pointer to the next node.
// create a tail that points to the memory address of the head variable
// create a class variable length that starts at value 1

// method: Append
// create a method, append(value), takes value as parameter. This should atleast try to add a new node to the tail of the linked list
// point the tail.next value to the newNode memory address, and change the value to the newNode thereafter
// increment the length class variable by one then return the object

// method: Prepend
// create a method, prepend(value), takes value as parameter. This should atleast try to add a new node to the head of the linked list
// point the newNode.next value to the head memory address, and change the value of the head to the newNode thereafter
// increment the length class variable by one then return the object

// method: printList
// create a method, printList(). This should atleast try to represent the value of linked list in an array.
// create an empty array. Create a variable to show the currentNode and set it equal to the head of the linked list.
// create a while loop  for whenever the currentNode isn't null/none, you add the currentNode.value to the array
// set the currentNode equal to the currentNode.next
// return the array after exiting the loop


//method: insert(index, value)
//This method should insert a node at a certain index


class Node {
    int value;
    Node next;

    public Node(int value) {
        this.value = value;
        this.next = null;
    }
}

public class LinkedList {

    private Node head;
    private Node tail;
    private int length;

    public LinkedList(int value) {
        head = new Node(value);
        tail = head;
        length = 1;
    }

    public Node getHead() {
        return head;
    }

    public Node getTail() {
        return tail;
    }

    public int getLength() {
        return length;
    }

    public void append(int number) {
        Node newNode = new Node(number);
        tail.next = newNode; // Link the last node to the new one
        tail = newNode; // Update tail to the new node
        length++;
    }

    public void prepend(int number){
        Node newNode = new Node(number);
        newNode.next = head;
        head = newNode;
        length++;
    }

    public void insert(int index, int number){
        Node newNode = new Node(number);
        if (index >= this.length || index < 0) {
            this.append(number);
            return;
        }
        if(index == 0){
            this.prepend(number);
            return;
        }
        Node currentNode = traverseIndex(index);
        Node previousNode = traverseIndex(index - 1);
        previousNode.next = newNode;
        newNode.next = currentNode;
        length++;

    }

    public Node traverseIndex(int index){
        if (index >= length || index < 0){ return null; }
        int counter = 0;
        Node currentNode = head;
        while(counter < index){
            currentNode = currentNode.next;
            counter++;
        }
        return currentNode;
    }

    public void remove(int index){
        if (index >= length || index < 0){ System.out.println("Invalid index!");length--; return;}

        if(index == 0){this.head = this.head.next; length--; return;}

        Node previousNode = traverseIndex(index - 1);
        Node unwantedNode = traverseIndex(index);
        previousNode.next = unwantedNode.next;
        
        length--;
    }

    public void reverse(){
        if(this.length == 1){
            System.out.println("Only one node in Linked list");
        }
        tail = head;
        Node first = head;
        Node second = first.next;

        while (second != null){
            Node third = second.next;
            second.next = first;
            first = second;
            second = third;
        }
        head.next = null;
        head = first;

    }

    public void printList() {
        Node current = head;
        while (current != null) {
            System.out.print(current.value + " -> ");
            current = current.next;
        }
        System.out.println("null");
    }
}
