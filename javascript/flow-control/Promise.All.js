/*
	Promise.all: Allows running a batch of functions asynchronously.
	 returns an array of the resolves promises, will resolve all of the functions
	 if any of the promises reject, then rejects fully. All must pass, else fail.
*/
const Promise = require('bluebird')

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

Promise.all([myAll(1), myAll(2), myAll(3)])
  .then(allVals => {
    for (var ind = 0; ind < allVals.length; ind++) {
      console.log(allVals[ind])
    };
  })

/*
	The Promise in totality is cut short. Only way to attain the results
 	of the resolved promises would be to catch them in a global variable.
	This is not wanted.
*/
Promise.all([myAll(1), myAll(2), myAll(-3)])
  .then(arr => {
    for (var ind = 0; ind < arr.length; ind++) {
      console.log(arr[ind])
    };
  }, arr => {
    console.log(arr)
  })

/* 
  This exception Handle is documented within the .Catch.js file
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