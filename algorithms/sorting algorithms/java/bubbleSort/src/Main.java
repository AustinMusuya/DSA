import java.util.Arrays;

/*

1. Understanding the Concept

Bubble sort is a comparison-based algorithm that repeatedly swaps adjacent elements
if they are in the wrong order.
The largest (or smallest) element "bubbles" to the correct position in each pass.

2. Initialize the Array or List

Start with an unordered collection of elements that need to be sorted.

3. Outer Loop for Passes

Create a loop that iterates through the list multiple times.
The number of passes should be one less than the total number of elements since,
after n-1 passes, the list will be sorted.

4. Inner Loop for Comparisons

In each pass, compare adjacent elements one by one. If the elements are in the wrong order
(e.g., for ascending order, the first element is greater than the second), swap them.

5. Reduce the Range in Each Pass

After each pass, the largest element (for ascending order) gets placed in its correct position
at the end of the list.
Reduce the range of comparisons by excluding the last sorted element.

6. Check for Early Termination

If a pass completes without any swaps, it means the list is already sorted.
Add an optimization to break out of the loop early when no swaps occur.

7. Return the Sorted List
Once all passes are completed, return or display the sorted list.

*/
public class Main {
    public static void main(String[] args) {
        int [] numbers =  {99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0};
        System.out.println("Unsorted array: " + Arrays.toString(numbers));

        bubbleSort(numbers);


        System.out.println("Bubble Sorted array: " + Arrays.toString(numbers));
    }

//    The Real Bubble sort
    public static int [] bubbleSort(int[] array){
        for(int i = 0; i < array.length - 1; i++){
            boolean swapped = false; // Track if swaps happen
            for(int j = 0; j < array.length - 1 - i; j++ ){ // Reduce range
                if(array[j] > array[j+1]){
                //Swap adjacent elements
                    int temp = array[j];
                    array[j] = array[j+1];
                    array[j+1] = temp;
                    swapped = true;
                }
            }
            if(!swapped) {break;} // Exit if no swaps (already sorted)
        }
        return array;
    }
}
