int binarySearch(int arr[], int n, int key) {
  int low = 0;
  int high = n - 1;
  int mid = (low + high) / 2;

  while (low != high) {
    if (arr[mid] == key) {
      return mid;
    } else if (key < arr[mid]) {
      high = mid - 1;
      mid = (low + high) / 2;
    } else if (key > arr[mid]) {
      low = mid + 1;
      mid = (low + high) / 2;
    }
  }

  return -1;
}
