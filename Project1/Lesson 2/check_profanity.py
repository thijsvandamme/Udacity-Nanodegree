import urllib

def read_text():
	quotes = open("C:\Users\Thijs\Desktop\Full Stack Web Developer Nano degree\Udacity-Nanodegree-Full-Stack-Web-Developer\Lesson 2\movie_quotes.txt")
	contents_of_file = quotes.read()
	print(contents_of_file)
	quotes.close()
	check_profanity(contents_of_file)

def check_profanity(text_to_check):
	#connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
	connection = urllib.urlopen("http://isithackday.com/arrpi.php?text="+text_to_check)
	output= connection.read()
	#print(output)
	connection.close()

	if "true" in output:
		print("Profanity alert!")
	elif "false"  in output:
		print("this document has no curse words!")
	else:
		print("could not read the document provided!")
read_text()