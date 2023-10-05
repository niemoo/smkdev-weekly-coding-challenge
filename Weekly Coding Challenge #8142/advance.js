let input_number = 6;

const countCubes = () => {
  for (let i = 1; i <= input_number; i++) {
    let cube = i * i * i;
    console.log(`Current Number is : ${i} and then cube is ${cube}`);
  }
};

countCubes();
