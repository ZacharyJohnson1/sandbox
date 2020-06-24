function findOutlier(integers){
  let odd = integers.filter(i => i % 2 !== 0);
  let even = integers.filter(i => i % 2 === 0);
  if(odd.length > even.length) return even[0];
  else return odd[0];
}