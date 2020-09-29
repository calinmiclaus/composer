#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  composer.py
#  
#  Copyright 2020 Călin Miclăuș <mcalin@arlug.ro>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


# Format of the array: midi_note_value, octave, name1, name2
# Use https://pypi.org/project/MIDIUtil/ for midi integration

from mxm.midifile import MidiOutFile
import subprocess

notes = [
[48,3,"C","Do"],
[49,3,"C#","Do#"],
[50,3,"D","Re"],
[51,3,"D#","Re#"],
[52,3,"E","Mi"],
[53,3,"F","Fa"],
[54,3,"F#","Fa#"],
[55,3,"G","Sol"],
[56,3,"G#","Sol#"],
[57,3,"A","La"],
[58,3,"A#","La#"],
[59,3,"B","Si"],

[60,4,"C","Do"],
[61,4,"C#","Do#"],
[62,4,"D","Re"],
[63,4,"D#","Re#"],
[64,4,"E","Mi"],
[65,4,"F","Fa"],
[66,4,"F#","Fa#"],
[67,4,"G","Sol"],
[68,4,"G#","Sol#"],
[69,4,"A","La"],
[70,4,"A#","La#"],
[71,4,"B","Si"],

[72,5,"C","Do"],
[73,5,"C#","Do#"],
[74,5,"D","Re"],
[75,5,"D#","Re#"],
[76,5,"E","Mi"],
[77,5,"F","Fa"],
[78,5,"F#","Fa#"],
[79,5,"G","Sol"],
[80,5,"G#","Sol#"],
[81,5,"A","La"],
[82,5,"A#","La#"],
[83,5,"B","Si"],
]


#TODO:
# adaugă funcție note_id (care să returneze int). Îți va fi mai ușor să creezi midi-uri custom (make_midi("Do","Re","Mi")...    

# What format should we use for output.
# 2=american(C), 3=italian(Do)
notation_type = 3

#fifths = ["C", "G", "D", "A", "E", "B", "F#", "C#", "G#", "D#", "A#", "F"]

# all the notes
chromatic = ["Do","Do#","Re", "Re#", "Mi", "Fa", "Fa#", "Sol", "Sol#", "La", "La#", "Si"]

magic_list=["Do-major","Re-minor","Mi-minor", "Fa-major", "Sol-major", "La-minor", "Si-diminished"]
magic_list1=[["Do","major-scale"],["Re","minor-scale"],["Mi","minor-scale"], ["Fa","major-scale"], ["Sol","major-scale"], ["La","minor-scale"], ["Si","minor-diminished-scale"]]
magic1=[ [1,0],[2,5],[3,6],[4,5],[5,1],[6,2] ]
magic2=[ [1,0],[2,5],[3,6],[4,1],[5,1],[6,2] ]

# chords and scales progressions. Each unit is a semitone, 0 being the root note
major_scale = [0,2,4,5,7,9,11,12]
minor_scale = [0,2,3,5,7,8,10,12]
minor_diminished_scale = [0,2,3,5,7,8,9,12]
romanian_scale = [0,2,3,6,7,9,10,12]
phrygian_scale = [0,1,3,5,7,8,10,12]

major_chord = [0,4,7]
minor_chord = [0,3,7]

# should we print the octave beside each note ? 0=false, 1=true
print_octave = 0

# returns the index (int) of note in the array, looking for it by name (any notation) and octave
def note_index(note,octave):
	for i in range(len(notes)):
		# check for both notation types (2,3) so we can specify any notation for the note argument
		if( note == notes[i][2] or note == notes[i][3] and octave == notes[i][1]):
		   return i

	return False

# return the midiid (int) of a 'note' in an 'octave'
def note_midiid(note,octave):
	for i in range(len(notes)):
		# check for both notation types (2,3) so we can specify any notation for the note argument
		if( note == notes[i][2] or note == notes[i][3] and octave == notes[i][1]):
		   return notes[i][0]

	return False

# prints out a progression starting from a note and an octave
def print_progression(note, octave, progression):
	# used for octave output (is it supressed or not?)
	octavestr = ""
	
	for delta in progression:
		if(print_octave==1):
			octavestr = "-" + str(octave)
		print(notes[note_index(note,octave)+delta][notation_type] + octavestr + " ", end = '')
	
	print()

# returns out the concatenation of midi_value_ids (str) in a 'progression'
def progression_midiid(note, octave, progression):
    # build up the output in this variable
	out=""
    
	for delta in progression:
		out=out+str(notes[note_index(note,octave)+delta][0]) + " "
	
	return out

# use system 'widemidi' to play 'midi_file"
def play_midi(midi_file):
    cmd = "wildmidi " + midi_file
    returned_value = subprocess.call(cmd, shell=True)  # returns the exit code in unix
    print('returned value:', returned_value)    

# writes a 'sequence' of notes (in midiid notation) to a 'midi_file'
def write_midi_sequence(midi_file,sequence):
    QUARTER = 480
    BAR = QUARTER*4
    GRAND_PIANO = 0

    out_file = open(midi_file, 'wb')
    midi = MidiOutFile(out_file)
    midi.header(format=1, nTracks=2, division=QUARTER)

    ##########################
    # track 0

    # in type 1 midi files first track MUST be a timing and tempo track
    # and no musical events are allowed.
    midi.start_of_track()
    midi.sequence_name(b'Timing track')
    midi.time_signature(nn=4, dd=2, cc=24, bb=8) # optional
    midi.tempo_bpm(135)
    midi.end_of_track()

    ##########################
    # track 1
    CH = 0
    midi.start_of_track()
    midi.patch_change(CH, GRAND_PIANO)
    midi.sequence_name(b'piano roll %i' % CH)

    midi.update_time(0)

    # go trough all notes in 'sequence' and add them to the track
    for NOTE in sequence.split( ):
        midi.note_on(CH, int(NOTE), 0x64)
        midi.update_time(int(BAR/4))                   # how much to sustain a note
        midi.note_off(CH, int(NOTE), 0x40)
        midi.update_time(int(QUARTER/2))        # how much time to wait between notes

    midi.update_time(BAR*4)
    midi.update_time(0)
    midi.end_of_track()

# prints out "magic" cyclic chords
def parse_magic(pos):
	# print the first chord, C
	print(magic_list[0])

	# print tne second chord in the progression
	print(magic_list[pos-1])

	while not pos==1:
		# print the next chord, until we reach C again
		print(magic_list[magic1[pos-1][1]-1])
		pos=magic1[pos-1][1]

# prints out "magic" cyclic chords
def parse_magic1(pos):
	# print the first chord, C
	print(magic_list1[0][1])

	# print tne second chord in the progression
	print(magic_list1[pos-1])

	while not pos==1:
		# print the next chord, until we reach C again
		print(magic_list1[magic1[pos-1][1]-1])
		pos=magic1[pos-1][1]

# prints chords and scales for all notes in chromatic
def brag_progression():
	for note in chromatic:
		for progression in [major_chord, minor_chord, major_scale, minor_scale, minor_diminished_scale, phrygian_scale, romanian_scale]:
			print_progression(note,4,progression)
		print()


def brag_magic():
	for progression in range(1,6):
		print("Progression in "+str(progression+1))
		parse_magic(progression+1)
		print()

def brag_magic1():
	for progression in range(1,6):
		print("Progression in "+str(progression+1))
		parse_magic1(progression+1)
		print()

#print(major_scale("Do",4))
#print(minor_scale1("Do",4))

#print_progression("Do",4,romanian_scale)
#print_progression("Do",4,phrygian_scale)

#brag_progression()
#brag_magic1()

sample_seq=progression_midiid("Do",4,phrygian_scale)

write_midi_sequence('test.mid',sample_seq)
play_midi('test.mid')

