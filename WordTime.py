'''
Title           :WordTime
Description     :A Python program to estimate the time taken to type a word.
Author          :Karthikeyan KC
URL             :http://geekswipe.net/technology/computing/measure-the-time-you-take-to-type-a-word-using-python/
Date            :13-10-2015
Version         :0.2
Usage           :python WordTime.py
Python Version  :2.7.8
'''

import Tkinter
import time

key_watcher = Tkinter.Tk()

#compare word input
word_compare_label = Tkinter.Label(key_watcher, text="Type the word that you want to test")
word_compare_label.pack(side=Tkinter.LEFT)

word_compare_entry_box = Tkinter.Entry(key_watcher)
word_compare_entry_box.pack(side=Tkinter.LEFT)

#type word input
word_type_label = Tkinter.Label(key_watcher, text="Repeat the word in your normal typing speed to calculate the time")
word_type_label.pack(side=Tkinter.LEFT)

word_type_entry_box = Tkinter.Entry(key_watcher)
word_type_entry_box.pack(side=Tkinter.RIGHT)

word_compare_entry_box.focus()

def pressed(keyevent):
	#compare word parameters
	compare_word = word_compare_entry_box.get()
	compare_word_size = len(compare_word)
	compare_word_list = tuple(compare_word)
	compare_word_first_letter = str(compare_word_list[0])
	compare_word_last_letter = str(compare_word_list[-1])

	#type word parameters
	type_word = word_type_entry_box.get()
	type_word_size = len(type_word)

	if type_word_size > 0:
		type_word_list = tuple(type_word)
		type_word_first_letter = str(type_word_list[0])
		type_word_last_letter = str(type_word_list[-1])

	if compare_word_size == 1 and type_word_size == 1:
		#Even though you measure time, it is insignificant! Also, it returns 0...
		print "It's just one letter... You at least need a two letter word to calculate the time!"

	if type_word_size == 1 and compare_word_size > 1 and compare_word_first_letter == keyevent.char:
		global start
		start = time.time()

	if type_word_size == compare_word_size and type_word_size != 1: 
		print "Match"
		if compare_word_last_letter == type_word_last_letter:
			stop = time.time()
			total_time = stop-start
			if compare_word == type_word:
				print "You took " + str(float(total_time)) + " seconds to type the word " + str(compare_word) + "."
			else:
				print "You took " + str(float(total_time)) + " seconds to type the word that was similar to " + str(compare_word) + "."
				print "Though the words are of the same size, it doesn't appear that the two words match! Retry again for accurate results..."

word_type_entry_box.bind('<KeyRelease>', pressed)
key_watcher.mainloop()