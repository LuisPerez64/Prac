const Promise = require('bluebird');

/*
	Setting up the base frame for a Promise
	Promises are more or less a method for handling Asynchronous
	 functionalities within a Synchronous language. Allowing heavier
	 flow control, and boosting the productivity of the code base.
*/
var promRes = undefined, 
  activate = true;
promiseBase = new Promise(function(resolve, reject) {
  if (activate) {
    baseRes = "I'm successful"
    resolve(baseRes)
  } else {
    baseRes = "I'm a failure. ";
    reject(baseRes)
  }
  /*
		Can still do some handling within the function, but at this point
		the asynchronous effects merge with Synchronous. Nothing can be 
		 returned at this point. Operations could be done on a global scale.
  */
  promRes = 18;
});

/*
	Invoking the promise, with a resolve state
*/
promiseBase.then(function(val) {
  console.log(val)
})
console.log(promRes)

activate = false;
promiseBase.then(undefined, val =>{
  console.log(val);
})

/* 
  If returning a Promise handle, must explicitly set it as a return var
  This is done when using a function, and returning a promise from it, instead
  of explicitly creating a New Promise object.
*/
retPromiseBase = () => {
  Promise.resolve("I like Toast")
  return Promise.resolve("I actually do though...")
}
//$ I actually do though...
retPromiseBase().then(val => console.log(val))