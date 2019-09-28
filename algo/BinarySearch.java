package algo;

/* Binary search implementation.

- The input array is sorted.
- Return the index of target value if found, else return -1. */

class BinarySearch {
    int binarySearch(int[] input, int target) {
        int low = 0, high = input.length-1;
        while (low <= high) {
            int mid = low + (high-low)/2;
            if (input[mid] == target) {
                return mid;
            } else if (input[mid] > target) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        BinarySearch obj = new BinarySearch();
        int[] arr = {1,2,3,4,5};
        int res = obj.binarySearch(arr, 3);
        System.out.println(res);
    }
}