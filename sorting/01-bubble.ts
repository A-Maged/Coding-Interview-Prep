function run(arr: number[]) {
  let swapped = true;

  while (swapped) {
    swapped = false;

    arr.forEach((el, i) => {
      if (el > arr[i + 1]) {
        /* swap */
        arr[i] = arr[i + 1];
        arr[i + 1] = el;

        swapped = true;
      }
    });
  }

  return arr;
}

console.log(run([2, 9, 4, 8, 3, 1, 0]));
