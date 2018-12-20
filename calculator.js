/*(function (exports, require, module, __filename, __dirname) {
    // calculator.js is actually executed here
    console.log("Calc");
    module.exports.add = (a,b) => a+b
});*/

module.exports = class Calculator {
    add(a,b) { return a + b }
    substract(a,b) { return a - b }
}

//console.log(module);