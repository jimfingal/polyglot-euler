from python.timer import Timer
import json
import importlib

def get_answers():
    answers = None

    with open('answers.txt', 'r') as f:
        answers = json.loads(f.read())

    return answers

if __name__ == "__main__":

    answers = get_answers()
    timer = Timer()
    print "*" * 80
    print "Project Euler Python Solutions"
    print "*" * 80

    for i in xrange(1, 11):

        # Dynamic importing
        module_name = 'python.E%03d' % i

        print "For Solution E%03d" % i

        timer.start()
        solution_func =  importlib.import_module(module_name).solution
        answer = solution_func()
        timer.stop()

        print "Answer: %s" % answer
        assert(answer == answers[i-1])
        print "Time Took: %s" % timer.elapsed()
        print "*" * 80
