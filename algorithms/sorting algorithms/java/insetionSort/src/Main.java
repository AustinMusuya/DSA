import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        int [] numbers = {99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0};
        System.out.println(Arrays.toString(numbers));
        System.out.println(Arrays.toString(insertionSort(numbers)));
    }

//    Try to implement Insertion Sort
    public static int [] insertionSort(int [] array){
        for(int i = 1; i < array.length; i++){
            int key = array[i];
            int j = i - 1;
            while(j >= 0 && array[j] > key){
                array[j+1] = array[j];
                j--;
            }
            array[j+1] = key; //this is where we do the insertion
        }
        return array;
    }

}
