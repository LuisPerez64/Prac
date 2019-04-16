/*
	Generators play a bigger role in function control than just counting
	They can be used to manipulate the flow of the whole program, allowing
	stricter laws on flow control, but also giving more power to the user, and
	segmenting work to be done only when it's needed, and allowing functions to 
	to be run, only when some requirements are met for them.
*/
// Foo will be called, when the yield needs to be satisfied in this case.
foo = function(inp) {
	console.log("In Foo ", inp)
	return inp*2;
}

gen = function*(inp){
 	let tmp = inp;
	
	console.log("In Gen", 1)
	yield foo(tmp);
 
  console.log("In Gen", 2)
}

console.log("Generator 1, return value of Foo's operation")
g=gen(3);

console.log("Out 1", g.next().value)
console.log("Out 2", g.next().value)


console.log("\n\nGenerator 2, Passing a value to be operated on by foo")
gen2 = function* () {
  console.log("In Gen2", 1)
  yield; // just pause

  console.log("In Gen2", 2)
  foo(yield); // pause waiting for a parameter to pass into `foo(..)`
 
  console.log("In Gen2", 3)
}

g = gen2()

console.log("Out 1", g.next())
console.log("Out 2", g.next(2))
console.log("Out 3", g.next(3))


console.log("\n\nGenerator 3, Passing a value to be operated on by foo, and yielding what it returned")
gen3 = function* () {
  console.log("In Gen3", 1)
  yield; // just pause

  console.log("In Gen3", 2)
  yield foo(yield); // pause waiting for a parameter to pass into `foo(..)`
 
  console.log("In Gen3", 3)
}

g = gen3()

console.log("Out 1", g.next())
console.log("Out 2", g.next(2))
console.log("Out 3", g.next(3))
