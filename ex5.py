name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74.0 # inches
weight = 180.0 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
metric_height = height * 2.54 # cm
metric_weight = weight * 0.454 # kg

print "Let's talk about %s." % name
print "He's %e inches tall." % height
print "That is %g centimeters." % metric_height
print "He's %f pounds heavy." % weight
print "That is %x kilograms." % metric_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %r depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %r." % (age, height, weight, age + height + weight)