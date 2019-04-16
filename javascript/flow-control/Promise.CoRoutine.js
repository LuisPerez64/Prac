/*
  Introduction to the bluebird.coroutine module.
  Allows for the use of Generator functions, and yields within code blocks
  Can grant better control flow, and also allows for on-demand memory cuts,
   explained in more depth within the Generators flowControl files.
*/
const Promise = require('bluebird')
let activate = true
myCo = Promise.coroutine(function*(res, rej) {
  console.log("Here")
  return yield new Promise(function(resolve, reject) {
        baseRes = "I'm successful"
        resolve(baseRes)
  })
})
// The yield only gets evaluated at the time of the call to .then
//myCo().then(console.log, console.error)

// Code snippet from bluebird's api, on using Promise.coroutine.
function PingPong() {/*...*/ };

PingPong.prototype.ping = Promise.coroutine(function* (val, limit) {
  //arguments.callee.count = ++arguments.callee.count || 1
  this.limit = this.limit || limit;
    console.log("Ping?", val);
    yield Promise.delay(500);
    if(val > this.limit)
    	return Promise.resolve("Done with %s Pings", limit)
    this.pong(val+1);
});

PingPong.prototype.pong = Promise.coroutine(function* (val) {
    console.log("Pong!", val);
    yield Promise.delay(500);
    this.ping(val+1);
});

var a = new PingPong();
/*
 DIfference between coroutines, and Promises . THe ping is called before the promise 
 is actually resolved, due to the then not returning a thenable object...
*/
myCo().then(console.log).then(a.ping(0, 3));

Promise.delay(5000).then(()=>{console.log("\n\nIn 2nd iter"); return myCo();})
	.then((val)=>{console.log(val); return Promise.resolve(4)}).then(val => {a.ping(0, val);});