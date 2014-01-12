TERM_CHOICES = (
	(0, 'Winter'),
	(1, 'Spring'),
	(2, 'Summer'),
	(3, 'Fall'),)

TIMES_CHOICES = []
for i in range(0, 48):
	TIMES_CHOICES.append((i, str((i % 24) / 2 or 12) + ":" + ("30" if i % 2 else "00") + (" PM" if i / 24 else " AM")))

def num2term(num):
	for pair in TERM_CHOICES:
		if pair[0] == num:
			return pair[1]
	return "Error"