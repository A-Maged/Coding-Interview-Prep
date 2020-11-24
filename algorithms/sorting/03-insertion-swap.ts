let arr = [3, 2, 9, 7, 1, 3, 0, 1];

console.log(run(arr));

function run(arr) {
  for (let i = 1; i < arr.length; i++) {
    let j = i;

    // if greater than current, then swap it
    while (j > 0 && arr[j - 1] > arr[j]) {
      const current = arr[j];

      arr[j] = arr[j - 1];
      arr[j - 1] = current;

      j--;
    }
  }

  return arr;
}
