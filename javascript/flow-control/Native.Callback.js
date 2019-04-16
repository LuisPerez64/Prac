/*
	A native flow control process for JS, is the callback(cb) function.
	It is executed upon completion of a needed task, else some of the async calls,
	 could be executed with no value. A lof of libraries take advantage of Async
	 functionalities, and most allow you to place cb within them.
*/
function PrintMe(input, cb) {
  console.log(input)
  if (cb)
    cb()
}

PrintMe("The functions below will execute as they come to the stack, printing Hello World");
PrintMe("Hello")
PrintMe("World\n\n")

//PrintMe("\nWith the addition of the setTimout Function, World Hello comes to play.")
tmp = setTimeout(() => {
  PrintMe("Hello\n")
}, 1500)
PrintMe("World")

tmp = setTimeout(() => { PrintMe("\nTo circumvent this situation, and allow better control when doing Async Operations\nCallbacks are used") }, 1800)
tmp = setTimeout(() => {
    PrintMe("Hello",
      PrintMe("World\n"))
  },
  2500)

tmp = setTimeout(() => { PrintMe("\nWith this, the user is able to chain functions together, based on their callbacks.") }, 3000)
tmp = setTimeout(() => {
  PrintMe("Hello", PrintMe("World", PrintMe("Nope, I don't wanna be here. Goodbye World\n\n")))
}, 3500)