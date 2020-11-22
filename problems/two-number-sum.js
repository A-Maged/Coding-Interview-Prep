function twoNumberSum(array, targetSum) {
  var allComps = {};

  for (const el of array) {
    var comp = targetSum - el;

    if (allComps[el]) {
      return [el, comp];
    } else {
      allComps[comp] = true;
    }
  }

  return [];
}

console.log(twoNumberSum([-1, 3, 11, 5, -4, 8, 1, 6], 10));
