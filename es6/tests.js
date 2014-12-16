var assert = require("assert");
var helpers = require("./helpers");

describe('Range Helpers', function() {
    describe('ascendingRange', function() {

        it('should return a 20 item list', function() {
            var zero_ninteteen = helpers.ascendingRange(0, 20, 1);
            assert.equal(true, Array.isArray(zero_ninteteen));
            assert.equal(20, zero_ninteteen.length);
        });

        it('should include start and not include end', function() {
            var zero_ninteteen = helpers.ascendingRange(0, 20, 1);
            assert.equal(0, zero_ninteteen[0]);
            assert.equal(19, zero_ninteteen[zero_ninteteen.length - 1]);
        });
    });

    describe('ascendingRangeGen', function() {

        it('should return generator whose first item is zero', function() {
            var range = helpers.ascendingRangeGen(0, 20, 1);

            var first = range.next().value;
            assert.equal(first, 0);
        });

        it('should return generator whose first item is one', function() {
            var range = helpers.ascendingRangeGen(1, 20, 1);
            var first = range.next().value;
            assert.equal(first, 1);
        });

        it('should not include last number', function() {

            var last = 20;

            range = helpers.ascendingRangeGen(0, last, 1);

            var memo = undefined;

            for (x of range) {
                memo = x;
            }
            assert.equal(19, memo);
        });
    });
});