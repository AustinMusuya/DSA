import java.util.HashMap;
import java.util.Map;

// Try to recreate an array using javascript classes with a few functions.

// Expected output

// {
//     length: 4,
//     data: {
//         0: value1,
//         1: value2,
//         2: value3,
//     },
// }

//  Approach:

// 1. Setup
// Create a class with constructor with field variables of length and data.
// Set the variables to 0 and an empty object/map respectively

// 2. Push Method. (adds item to the end of the list/array)

// Create a push method to add value to the data object.[length] key and increment the length variable by 1

// 3. Pop Method.(removes the last item)

// Create a pop method to delete the last added value at the data.length key (data[this.length - 1]),
// and decrement the length variable by 1

// 4. Shift Method. (Removes the first item)

// If the length is 0 then return undefined as the output
// Set a variable index to the value of 0.

/*
   Loop through the elements while the last item is greater than the index,
   storing the data at index + 1 (data[index + 1]), in data at the current index (data[index])
   then increment index by 1
*/

// Delete the last item and decrement the length by 1
// Return the first item

// 5. Unshift method (adds an item to the beginning of array/list)

// Set variable index and set it to the length of the array.
// Loop through the array while the length of the array/list is more than 0.
// Store the value of data[index -1] to data[index] and decrement the value of index
// set data[0] to the value passed as the parameter.
// Increment the length by 1

public class newArray {
    private int length = 0;
    private Map<Integer, String> data = new HashMap<>();

    public int getLength() {
        return length;
    }

    public Map<Integer, String> getData() {
        return data;
    }

    public int push(String value){
        data.put(length, value);
        this.length++;
        return length;
    }

    public String get(int index){
        return data.get(index);
    }

    public String pop(){
        if (length == 0){
            return null;
        }
        length--;
        return data.remove(length);
    }

    public String shift(){
        if (length == 0){
            return null;
        }
        String firstItem = data.get(0);
        int lastItem = length - 1;
        data.get(lastItem);
        int index = 0;
        while(lastItem > index){
            data.put(index, data.get(index + 1));
            index++;
        }
        data.remove(lastItem);
        length --;
        return firstItem;
    }

    public String unshift(String value){
        int index = length;

        while (index > 0 ){
            data.put(index, data.get(index - 1));
            index--;
        }
        length++;
        return data.put(0, value);
    }

}
