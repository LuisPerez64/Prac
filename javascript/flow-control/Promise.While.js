/**
 * Created by lperez on 4/22/17.
 * Looking into more flow control with regards to Loop Conditions with Promises
 * There are two methods so far that I've seen,
 *   My own implementation, which requires recursion.
 *      Not really good, due to intense recursion blowing the stack.
 *  The Promise.while Implemented by a user from site "http://blog.victorquinn.com/javascript-promise-while-loop"
 */

const Promise = require('bluebird');
/**
 *  @param condition: Function which evaluates to true or false
 *  @param action: A Promise that gets called until the condition is met
 *  @returns promise:
 */
const promiseWhile = function(condition, action) {
    let resolver = Promise.defer();

    let loop = function() {
        if (!condition()) return resolver.resolve();
        return Promise.cast(action())
            .then(loop)
            .catch(resolver.reject);
    };

    process.nextTick(loop);

    return resolver.promise;
};