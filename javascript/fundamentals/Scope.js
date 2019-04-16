var l = 'Global'
console.log("Val:>>>",l, "<< Before Func1\n")
function Func() {
	var l = "In Func1 Scope"
	console.log("Val:>>>",l,"<< Before Let\n")
	{
		let l = "In Block Scope"
		console.log("Val:>>>",l,"<< In Let \n")
	}
	console.log("Val:>>>",l,"<< After Let\n")
}

Func();
console.log("Val:>>>",l, "<< After Func1 / Before Func2\n")
function Func2() {
	l = "In Func2 Using Global"
	console.log("Val:>>>",l,"<<  In Func 2\n")	
}
Func2();
console.log("Val:>>>",l, "<< After Func2\n")
