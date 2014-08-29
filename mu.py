'''
Author:		Ryan Wagner
		rkwagner@ucsd.edu
		http://github.com/rkwagner
Description:	Song generation file in Python
'''

import wave as w, math as m, struct as s

notes = { 'c': 16.35, 'c#': 17.32, 'd_': 17.32, 'd': 18.35, 'd#':19.45, \
	'e_': 19.45, 'e': 20.60, 'f':21.83, 'f#': 23.12, 'g_': 23.12, \
	'g': 24.50, 'g#': 25.96, 'a_': 25.96, 'a': 27.50, 'a#': 29.14, \
	'b_': 29.14, 'b': 30.87, 'r': 0, 'h': -1, 'l': -1 }

def print_list():
	print 'Valid notes:\nc, c#, d_, d, d#, e_, e, f, f#, g_, g,', \
		'g#, a_, a, a#, b_, b\nValid octaves: 0 - 8'

def print_help():
	print 'Valid arguments:\nr,anything,rest_length_ms \n', \
		'note,octave,length\n(Use # = sharp, _ = flat)\n' \
		'Split arguments with whitespace.'

def get_note(in_note, in_num):
	in_note = in_note * ( 2 ** int( in_num ) )
	return in_note

def music( q ):
	wav = w.open( wav_file, "w" )
	wav.setparams( ( 1, 2, 1000, 0, 'NONE', 'noncompressed' ) )
	for i in range( len( q ) ):
		time = q[i][2]
		if q[i][0] == 'r':
			freq = 1
		else:
			freq = get_note( q[i][0], q[i][1] )
		for j in range( 0, int( time ) ):
			tone = m.sin( m.pi * 2 * freq * j / 1000 )
			vol = 32767 * tone
			wav.writeframes( s.pack( 'h', int( vol ) ) )
		for j in range( 0, 50 ):
			wav.writeframes( s.pack( 'h', 0 ) )
	wav.close( )

wav_file = str(raw_input( 'Filename>' ) + '.wav' )
w_form = str( raw_input( 'Notes>' ) )
try:
	p = w_form.split()
	q = []
	for i in range( 0, len( p ) ):
		q += [p[i].split( ',' )]
	for i in range( 0, len( q ) ):
		q[i][0] = notes[q[i][0]]

except KeyError as desc:
	print 'Input error (', desc, ')'
else:
	if w_form == 'h':
		print_help( )
	elif w_form == 'l':
		print_list( )
	else:
		music( q )
