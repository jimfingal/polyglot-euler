var helpers = require('./helpers')

var solution = function() {

    let max = 1000;
    let sum = 0;

    for (let x of helpers.ascendingRangeGen(0, 1000, 1)) {
        if (x % 3 == 0 || x % 5 == 0) {
            sum += x;
        }
    };

    return sum;
};


exports.solution = solution;