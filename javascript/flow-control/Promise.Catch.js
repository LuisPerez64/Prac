const Promise = require('bluebird');

myCatch = function(activate) {
  return new Promise(function(resolve, reject) {
    var tmpFuncTwo;
    if (activate === true) {
      tmpFuncTwo = "I'm successful"
      resolve(tmpFuncTwo)
    } else if (activate === false) {
      tmpFuncTwo = "I'm a failure.";
      reject(tmpFuncTwo)
    } else {
      tmpFuncTwo = "Oh this is not good."
      throw new Error(tmpFuncTwo);
    }
  });
}

myAll = (val) => {
  return new Promise(function(resolve, reject) {
    if (val > 0)
      resolve((val + 1) * 5)
    else if (val < 0)
      reject(val * 2)
    else {
      var tmp = new Error("No work for 0");
      tmp.type = 'CustomError';
      reject(tmp);
    }
  })
}

// .catch standard Promises
/*
	With promises, if a chain meets with an error, explicit throw
	the next catch block in the chain is used as the handler.
	Thros are caught by the nearest catch block
*/
myCatch(true)
  .then(function(value) {
    console.log("1 ", value)
    return myCatch()
  })
  .catch(function(e) {
    console.log("2 ", e.message);
    return myCatch(false)
  })
  .then(undefined, function(val) {
    console.log("3 ", val);
    // Throw again
    return myCatch();
  })
  .then(function(val) {
    // Skips this function branch
    console.log("4 I'm not going to be called.")
    return Promise.resolve(val)
  })
  .catch(function(e) {
    console.log("5 Caught the last thrown error")
  })


// .catch using Promise.all 
/* 
  Extrending to the catch block handling, Attempting to call the catch block 
   explicitly will fail. They will reject on the first fail case, so attempting
    to throw from the function that is calling, will not work. 
    For the purpose of maintianing the try/catch syntax, the Exception case
    is wrapped around a resolve in itself, which then throws the Error, which 
    is caught by the needed Catch Block.

*/
Promise.all([myAll(1), myAll(0), myAll(-3)])
  .then(
    arr => {
      for (var ind = 0; ind < arr.length; ind++) {
        console.log(arr)
      };
    }, rej => {
      if (rej.type == 'CustomError')
        throw rej;
      console.log(arr)
    })
  .catch(e => {
    console.log("Catching Internal ", e.message)
  })