 var l = new Error("Throwing CustomError")
 l.type = 'CustomError'

 try {
   throw (l)
 } catch (e) {
   console.log(e.message)
 }
 console.log(l.type)