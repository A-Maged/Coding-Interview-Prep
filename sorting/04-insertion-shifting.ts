let arr = [3, 2, 9, 7, 1, 3, 0, 1];

console.log(run(arr));

function run(arr: number[]) {
  for (let index = 0; index < arr.length; index++) {
    let currentItem = arr[index];
    let indexCopy = index;

    /* keep shifting items until our item is bigger */
    while (indexCopy > 0 && arr[indexCopy - 1] > currentItem) {
      arr[indexCopy] = arr[indexCopy - 1];
      indexCopy--;
    }

    /* insert our item */
    arr[indexCopy] = currentItem;
  }

  return arr;
}
