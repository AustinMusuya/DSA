import java.util.Arrays;
import java.util.HashMap;

public class Main {
    public static void main(String[] args) {
        int [] nums = {2, 7, 11, 15};
        int [] result = twoSum(nums, 9);
        int [] result2 = twoSum2(nums, 9);

        System.out.println(Arrays.toString(nums));

        System.out.println(Arrays.toString(result));

        System.out.println(Arrays.toString(result2));

    }
    /*
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
*/


// Optimized Approach (hashmap) Time Complexity O(n): Space Complexity O(n)

    /*
    We will loop through the array and store each value to a hashmap/dictionary
    in the (key:value) pair of (number:index) in the array. (i.e, 2 : 0, 7 : 1 )

    A variable "complement" that is the target sum minus the array[i] i.e (9 - 2 = 7)
    will be compared to see if it is existent in the hashmap/dicitionary.

    If it is then we will return an array of the two indices [0, 1]

    If not we will keep on adding values till the end of the array
    and return an empty array if we cannot find the sum pair indices

    */
    public static int [] twoSum(int [] array, int target){
        HashMap<Integer, Integer> numToIndex = new HashMap<>();
        for(int i = 0; i< array.length; i++){
            int complement = target - array[i];
            if (numToIndex.containsKey(complement)){
                return new int[] {numToIndex.get(complement), i};
            }
            numToIndex.put(array[i], i);
        }
        return new int[] {};
    }


// Brute Force Approach nested loop Time Complexity O(n^2): Space Complexity O(1)

    /* 
    We will have two loops (outer and inner) where we will check to see if array[i] is equal to 
    array[j]

    if so then we will return the two indices of the elements in the array

    Input: nums = [2,7,11,15], target = 9

    */
    
    public static int [] twoSum2(int [] array, int target){
        for (int i = 0; i < array.length; i++ ){
            for (int j = i + 1; j < array.length; j++){
                if (array[i] + array[j] == target){
                    return new int[] {i, j};
                }
            }
        }
        return new int[] {};
    }
}
