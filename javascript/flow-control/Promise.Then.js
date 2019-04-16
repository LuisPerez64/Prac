const Promise = require('bluebird');

/*
	Setting up the base frame for a Promise
	Promises are more or less a method for handling Asynchronous
	 functionalities within a Synchronous language. Allowing heavier
	 flow control, and boosting the productivity of the code base.
 	A promise is not directly callable, but can be returned, and acted upon.
 	
 	In the process of initializing the Promise(return), the promise must be 
 	 wrapped in a base function. 
  The created new Promise receives two functions as it's params. 
 	What to do on success or failure
 		resolve: at which point the promise was fulfilled.
 		reject: at which point the promise failed to be fulfilled.
 	These act like callback functions, but are a bit more powerful, and do not
 	 disrupt the active flow of the running code around them, 
 	 they are non-blocking.	
 	Promises inherit variables from the function that contains them's scope
 	 This is of note, due to the, presumed, inability to pass in more parameters.

	myThen takes activate(bool) and resolves/rejects based on that.
*/
myThen = function(activate) {
		return new Promise(function(resolve, reject) {
			var tmpFuncOne;
			if (activate) {
				tmpFuncOne = "I'm successful"
				resolve(tmpFuncOne)
			} else {
				tmpFuncOne = "I'm a failure. ";
				reject(tmpFuncOne)
			}
		});
	}
	/*
		Base format of calling this functions relies on the same syntax as normal.
		But with an added parameter as to what to do after the function executes.
		The "then" keyword, forces strict control flow, as, if nothing fails, the 
		resolve/reject calls are handled there.
	*/
	/*
		Calling myThen without a then, since it returns a promise 
		yields the result:
		Unhandled rejection I'm a failure. 
	*/
	//myThen()

/*
	A promise needs something to handle it if it succeeds or fails. 
	Now adding in the handling. 

	The first example shows handling of the resolve condition.

	The conole.log() in between the two myThen calls, shows a misstep. This echoes 
	the need for the Promises themselves. 

	The second, puts a placeholder on the resolve block, as it expects a param,
	 and  adds a rejection handler.

	The third example shows expanding the Promise chain with then-able functions 
	The .then block controls callFlow,
	if it's given a 'then-able' function as a parameter. It is able to 
	extend the promise chain.
	In all values, the returned content within the resolve/reject is the returned 
	 content from the previous promise resolution.
*/


// I am accepted
// I'm successful
myThen(true)
	.then(function(result) {
		console.log("I am accepted")
		console.log(result);
	})
console.log("These things are Asynchronous, I come out instantly")

//	I was rejected
//	I'm a failure. 
myThen()
	.then(undefined, function(result) {
		console.log("I was rejected")
		console.log(result)
	})

myThen(true)
	.then(function(result) {
		console.log("Chained Now, I am accepted")
		console.log(result);
		return myThen(false)
	})
	.then(undefined, function(result) {
		console.log("Chained Now, I was rejected")
		console.log(result)
	})

