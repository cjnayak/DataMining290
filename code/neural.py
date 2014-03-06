#Learning weight
l = 10

#Input value
o1 = 1
o2 = 2

#Hidden Input Values
o3 = 0.7311
o4 = 0.0179
o5 = 0.9933

#Output Value
o6 = 0.8387

#Weights 
weight13 = -3.0
weight14 = 2.0
weight15 = 4.0
weight23 = 2.0
weight24 = -3.0
weight25 = 0.5
weight36 = 0.2
weight46 = 0.7
weight56 = 1.5


def Output_Error(o):
	t6 = 0.0
	err = o*(1.0-o)*(t6-o)
	return(err)
	
def hidden_node(o,err,weight):
	err = o*(1.0-o)*(err*weight)
	return(err)

def adjust_weight(l,weight,o,err):
	adjust_weight = weight+(l*err*o)
	return(adjust_weight)

#Output Error (.8387)
err_6 = Output_Error(o6)

#Hidden Node Error
err_5 = hidden_node(o5,err_6,weight56)
err_4 = hidden_node(o4,err_6,weight46)
err_3 = hidden_node(o3,err_6,weight36)

w_56 = adjust_weight(l,weight56,o5,err_6)
w_46 = adjust_weight(l,weight46,o4,err_6)
w_36 = adjust_weight(l,weight36,o3,err_6)
w_25 = adjust_weight(l,weight36,o2,err_5)
w_24 = adjust_weight(l,weight36,o2,err_4)
w_23 = adjust_weight(l,weight36,o2,err_3)
w_15 = adjust_weight(l,weight36,o1,err_5)
w_14 = adjust_weight(l,weight36,o1,err_4)
w_13 = adjust_weight(l,weight36,o1,err_3)

#Printing the Errors
print "err_3: %s" % err_3
print "err_4: %s" % err_4
print "err_5: %s" % err_5
print "err_6: %s" % err_6

#Printing the Weights 
print "weight13: %s" % w_13
print "weight14: %s" % w_14
print "weight15: %s" % w_15
print "weight23: %s" % w_23
print "weight24: %s" % w_24
print "weight25: %s" % w_25
print "weight36: %s" % w_36
print "weight46: %s" % w_46
print "weight56: %s" % w_56
