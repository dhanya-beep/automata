def is_accepted(input_string):
	current_state = q0;
	
	for symbol in input_string:
		if current_state == q0:
			if symbol == 'a':
				current_state = q1
			else:
				return false;
		
		elif current_state == q1:
			if symbol == 'a':
				current_state = q1
			elif symbol == 'b':
				current_state = q2
			else:
				return false
		
		elif current_state == 'q2':
			if symbol == 'b':
				current_state = q2
			else:
				return false
		
		else:
			return false
	return current_state == q2
	
if __name__ == "main":
	input_string == input("enter an string")
	if is_accepted(input_string):
		print("yes it is accepted")
	else:
		print("not accepted")
