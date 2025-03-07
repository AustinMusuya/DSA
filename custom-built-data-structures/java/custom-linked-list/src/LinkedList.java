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
// increament the length class variable by one then return the object

// method: printList
// create a method, printList(). This should atleast try to represent the value of linked list in an array.
// create an empty array. Create a variable to show the currentNode and set it equal to the head of the linked list.
// create a while loop  for whenever the currentNode isn't null/none, you add the currentNode.value to the array
// set the currentNode equal to the currentNode.next
// return the array after exiting the loop


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

    public void printList() {
        Node current = head;
        while (current != null) {
            System.out.print(current.value + " -> ");
            current = current.next;
        }
        System.out.println("null");
    }
}
