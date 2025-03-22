import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        
        int [] numbers = {99, 44, 25 , 6, 7 , 27, 0, 1, 9, 283, 41};

        System.out.println(Arrays.toString(numbers));

        int [] sortedNumbers = mergeSort(numbers);

        System.out.println(Arrays.toString(sortedNumbers));
    }

    public static int [] mergeSort(int[] array){
        //base case
        if(array.length <= 1){ return array;}

        //Divide and conquer Approach
        int middle = array.length / 2;
        int [] left = mergeSort(Arrays.copyOfRange(array, 0, middle));
        int [] right = mergeSort(Arrays.copyOfRange(array, middle, array.length));

        return merge(left, right);
    }

    public static int[] merge(int[] left, int[] right){
        int [] result = new int[left.length + right.length];
        int leftIndex = 0, resultIndex = 0, rightIndex = 0;

        while(leftIndex < left.length && rightIndex < right.length){
            if(left[leftIndex] < right[rightIndex]){
                result[resultIndex++] = left[leftIndex++];
            }else{
                result[resultIndex++] = right[rightIndex++];
            }
        }
        // Add the remaining elements

        while(leftIndex < left.length){
            result[resultIndex++] = left[leftIndex++];
        }
        while(rightIndex < right.length){
            result[resultIndex++] = right[rightIndex++];
        }
        return result;
    }
}
