public class customArray {
    public static void main(String[] args) {

        newArray myArray = new newArray();

        myArray.push("Mark");
        myArray.push("Austin");
        myArray.push("James");
        myArray.push("Ben");

        System.out.println("Data: " + myArray.getData() + " " +  "Length: " + myArray.getLength());
        myArray.shift();
        System.out.println("Data: " + myArray.getData() + " " +  "Length: " + myArray.getLength());


    }
}
