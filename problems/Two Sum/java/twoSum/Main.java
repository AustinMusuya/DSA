import java.util.Arrays;
import java.util.HashMap;

public class Main {
    public static void main(String[] args) {
        int [] nums = {2, 7, 11, 15};
        int [] result = twoSum(nums, 9);

        System.out.println(Arrays.toString(nums));

        System.out.println(Arrays.toString(result));

    }
    /*
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
*/


// Optimized Approach (hashmap) Time Complexity O(1): Space Complexity O(n)

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
}
