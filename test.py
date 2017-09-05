
week = 0
one = 25000.0
two = 25000.0
three = 25000.0
for x in range(0, 365):
    week += 1
    if week == 6:
        print "------"
    elif week == 7:
        week = 0
    else:
        one=one*1.01
        two=two*1.02
        three=three*1.03
        print "%.0f" % one + "     %.0f" % two + "     %.0f" % three
