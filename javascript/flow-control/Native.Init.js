/*
	NAtive Javascrip functions Synchronousely, there have been as time has passed
	efforts to make the language run Asynchronously, this is what occurs with 
	 AJAX, and a lot of other points of the model. Introducing Non Blocking BX
	setTimeout is one of the functions that will simkulate Async BX natively 
	 in NodeJS, the main reason for running through this. 
*/
var ind;
console.log("Starting the While Loop")
for (ind = 0; ind < 1000000000; ind++);
console.log("Exited the loop Iterations: "+ ind)

console.log("\nStarting the setTimeout native Async call, timeout of 5 seconds")
setTimeout(() => { console.log("Now the timeout is done.") }, 5000)
console.log("Well I shouldn't come out yet, but setTimeout is Async so...")

