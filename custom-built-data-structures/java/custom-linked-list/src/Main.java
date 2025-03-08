public class Main {
    public static void main(String[] args) {

        LinkedList myList = new LinkedList(10);
        myList.append(20);
        myList.append(30);
        myList.prepend(80);

        System.out.println("Linked List:");
        myList.printList();
        System.out.println(myList.traverseIndex(2));
        myList.insert(0, 120);
        myList.printList();

        System.out.println("Head: " + myList.getHead().value);
        System.out.println("Tail: " + myList.getTail().value);
        System.out.println("Length: " + myList.getLength());

    }
}
