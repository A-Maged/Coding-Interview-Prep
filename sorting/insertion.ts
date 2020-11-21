function run(arr: number[]) {
  for (let i = 1; i < arr.length; i++) {
    for (let j = 0; j < i; j++) {
      if (arr[i] < arr[j]) {
        console.log(arr);

        let [newItem] = arr.splice(i, 1);

        arr.splice(j, 0, newItem);
      }
    }
  }

  return arr;
}

console.log(run([2, 9, 4, 8, 3, 1, 0]));
