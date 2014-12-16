helpers = require('./helpers')



var solution = function() {

    var max = 1000;

    var sum = 0;
    for (x of helpers.ascendingRangeGen(0, 1001, 1)) {

        if (x % 3 == 0 || x % 5 == 0) {
            sum += x;
        }

    };

    return sum;

}