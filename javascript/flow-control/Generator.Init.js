/*
	Generators are functions which allow lazy sequencing in languages that 
	 do not inherently produce them.
	They are, at root, of format: function* () {...; yield 'doSomething';...}
	 The yield is a stop point, yielding the result of the current step to the
	 caller.
	Never re-use a generator, must make a new call to the function
	 They will remain at the last stage of their yield, and continue from there
	 unless that is the wanted result. 
*/
/*
	SImple generator function with a one-off call.
*/
console.log("Beginning genInit output");
genInit = function*() {
  console.log("Handle the yield");
  yield 5;
  console.log("Nothing else to do")
}
var g = genInit()
  /*
  	The variable is instantiated, and the generator's next function is invoked.
  	This spools up the generator, and brings up the first yield. At which point
  	the generator returns.  
  */
  //{}: The function was called, but next's not been called on the Generator
console.log(g);

/*
'.next()' comes back with it's results
 done(bool): More yieldable content? true : false
 value(*): Whatever is yielded from the generator
*/
//Handle the yield
//{ value: 5, done: false }: A yield was met, and returned.
console.log(g.next().value)
  //Nothing else for next to operate on, reaches the end of the function.
console.log(g.next().value)

/*
	A yield can handle a for loop, or any other type of iterative loop internally
	Once the yield is met, it returns, leaving the function awaiting a .next() call
	to be able to continue on.
*/
console.log("\n\nBeginning genMulti output");
genMulti = function*() {
  for (var ind = 0; ind < 10; ind++)
    yield(ind * 2)
}

g = genMulti();
console.log(g.next().value)
console.log(g.next().value)

//Generators are iterators, meaning they can be treated as parameters to loops
for (q of g) {
	// Will resolve q to the value field in the returned object
  console.log("For Loop: ", q)
}

/*
	Passing values in to be dealt with as parameters to yield
	Also emulating the Lazy Sequence aspect of a yield. It can go forever
	if needed, but safeguards shoule be in place to stop that behavior
	Any variables that may need to be initialized within the scope of the
	 generator function must be initialized if wanted.
*/
console.log("\n\nBeginning genValue output");
genValue = function* (init, fini){
	let i = init;
	for(; i < fini; i++)
		yield (fini - i)
}

g = genValue(0, 10);
for(let q of g)
	console.log(q)

console.log("\n\nBeginning genValue Second Iteration output");
g = genValue(0, 100)
/* 
	Once passed into the for...of construct, if the generator is stopped partway
	The generator is destroyed, it reaches the end of it's function. Safeguards
	 against possibly leaving a zombie generator?
*/
for(let q of g){
	console.log(q)
	if (q <= 95)
		break
}
//Displaying the generator state issue.
console.log("The Generator Object after the break in for...of", g.next())

/*
	Next can be used to actively mutate the actions as the yield goes forth
	Paasing it's arguments forward, and storing them in yield. 
	Shell
*/
console.log("\n\nBeginning genArr output");
var arr = []
genArr = function*() {
	while (true){
	arr.push(yield)
	}
}

g = genArr()
//Get to the yield
g.next()
g.next("poip")
g.next(13)
g.next(15)
// Calling return goes to the end of the  generator, terminating it.
g.return()
console.log("Array yielded from genArr: ", arr)


console.log("\n\nBeginning genStar output");
/*
	yield*: Allows operations to be done iterables, or other generators
	Expanding on this concept in other Generator.*
*/
genStar= function*(inp, inp2) {
  var tmp = inp,
    tmp2 = inp2;
  yield* [tmp, tmp2]
}

g = genStar(3, 'Book');
console.log(g.next().value)
console.log(g.next().value)