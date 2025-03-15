import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        int [] numbers =  {99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0};
        System.out.println("Unsorted array: " + Arrays.toString(numbers));

        selectionSort(numbers);

        System.out.println("Selection Sorted array: " + Arrays.toString(numbers));
    }

    public static int [] selectionSort(int[] array){
        for(int i = 0; i < array.length; i++){
            int min = i;
            int temp = array[i];
            for(int j = i+1; j < array.length; j++){
                if(array[j] < array[min]){
                    min = j;
                }
            }
            array[i] = array[min];
            array[min] = temp;
        }
        return array;
    }
}
