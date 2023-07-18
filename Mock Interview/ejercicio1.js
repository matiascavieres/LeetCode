//declarar el arreglo
//Obtener el largo del arreglo
//Entregar los valores de X al arr
//Entregar los valores de Y al arr
//Resolver Contraints
//1 <= n <= 500
//nums.length == 2n
//1 <= nums[i] <= 10^3

//[2,3,5,4,1,7]

function orderArray(nums,n){
  
  let constraints = 0;
  
  if (1<=n || n<=500){
    constraints+=1;
  }
  
  if (nums.length%2 == 0){
    constraints+=1;
  }
  
  if(1<=nums.length || nums.length<=10^3){
    constraints+=1;
  }
  let arrX=[];
  let arrY=[];
  let newArr= [];
  
  if (constraints == 3){
    for(let i=0;i<n;i++){
      arrX.push(nums[i])
      arrY.push(nums[i+n])
    }
    for(i=0;i<n;i++){
      newArr.push(arrX[i])
      newArr.push(arrY[i])
    }
    return newArr
  }
}

orderArray([2,5,1,3,4,7],3)