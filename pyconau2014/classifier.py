"""A command line tool for classifying tweets collected by get_twitter.py

take care, will overwrite output_filename

Run this using:

python classifier.py input_filename output_filename

(obviously replacing the last two)

If output_filename exists, this will load that file's contents and rewrite it.
Be careful!!! 
This functionality allows you to quit the program and restart at a later time,
without losing your progress. However if the file is not legitimate, what
will likely happen is that you will lose that file.

"""
import sys
import os
import csv

input_filename = sys.argv[1]
output_filename = sys.argv[2]

existing_lines = dict()

if os.path.exists(output_filename):
	with open(output_filename) as inf:
		for line in inf:
			if len(line.strip()) == 0:
				continue
			data = line.split(",")
			y = int(data[-1])
			text = ",".join(data[:-1])
			existing_lines[text] = y
	print("Loaded {} existing entries".format(len(existing_lines)))

with open(input_filename) as inf, open(output_filename, 'w') as outf:
	for line, prediction in existing_lines.items():
		outf.write("{},{}\n".format(line, prediction))
	for line in inf:
		line = line.strip()
		print("\n\n\n")
                print("num {}".format(len(existing_lines)))
		print(line)
		if line in existing_lines:
			print("Already found: {}".format(existing_lines[line]))
			prediction = existing_lines[line]
			continue
		else:
			a = raw_input("\nIs this spam? (enter for 'no')")
			prediction = 0
			if a.lower() == 'y':
				prediction = 1
		existing_lines[line] = prediction
		print("Prediction: {}".format(prediction))
		outf.write("{},{}\n".format(line, prediction))

		
