basecalculator = require('./calculator');
class DerivedCalculator extends basecalculator{
    multiply(a,b) { return a*b }
    division(a,b) {
        try {
            let result = a/b
            return (result == "Infinity")? 0 : result;
        }
        catch(e) {
            return 0
        }
    }
}
module.exports = new DerivedCalculator()
