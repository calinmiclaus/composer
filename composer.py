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


# notation_type: 2=american(C4), 3=italian(Do4)
notation_type = 3

# first value is the midi note value. Use https://pypi.org/project/MIDIUtil/ for midi integration
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

#fifths = ["C-4", "G-4", "D-4", "A-4", "E-4", "B-4", "F#-4", "C#-4", "G#-4", "D#-4", "A#-4", "F-4"]

chromatic = ["Do","Do#","Re", "Re#", "Mi", "Fa", "Fa#", "Sol", "Sol#", "La", "La#", "Si"]

magic_list=["Do-major","Re-minor","Mi-minor", "Fa-major", "Sol-major", "La-minor", "Si-dimiinshed"]

magic1=[ [1,0],[2,5],[3,6],[4,5],[5,1],[6,2] ]
magic2=[ [1,0],[2,5],[3,6],[4,1],[5,1],[6,2] ]


def find_note_index(note,octave):
	for i in range(len(notes)):
		if(note==notes[i][notation_type] and octave==notes[i][1]):
		   return i
	return False


def major_chord(note,octave):
	return(
	notes[find_note_index(note,octave)][notation_type] + "-" + str(octave) + " " +
	notes[find_note_index(note,octave)+4][notation_type] + "-" + str(octave) + " " +
	notes[find_note_index(note,octave)+7][notation_type] + "-" + str(octave)
	)

def minor_chord(note,octave):
	return(
	notes[find_note_index(note,octave)][notation_type] + "-" + str(octave) + " " +
	notes[find_note_index(note,octave)+3][notation_type] + "-" + str(octave) + " " +
	notes[find_note_index(note,octave)+7][notation_type] + "-" + str(octave)
	)

def major_scale(note,octave):
	return(
	notes[find_note_index(note,octave)][notation_type] + "-" + str(octave) + " " +
	notes[find_note_index(note,octave)+2][notation_type] + "-" + str(octave) + " " +
	notes[find_note_index(note,octave)+4][notation_type] + "-" + str(octave) + " " +
	notes[find_note_index(note,octave)+5][notation_type] + "-" + str(octave) + " " +
	notes[find_note_index(note,octave)+7][notation_type] + "-" + str(octave) + " " +
	notes[find_note_index(note,octave)+9][notation_type] + "-" + str(octave) + " " +
	notes[find_note_index(note,octave)+11][notation_type] + "-" + str(octave) + " " +
	notes[find_note_index(note,octave)+12][notation_type] + "-" + str(octave)
	)

def minor_scale(note,octave):
	return(
	notes[find_note_index(note,octave)][notation_type] + "-" + str(octave) + " " +
	notes[find_note_index(note,octave)+2][notation_type] + "-" + str(octave) + " " +
	notes[find_note_index(note,octave)+3][notation_type] + "-" + str(octave) + " " +
	notes[find_note_index(note,octave)+5][notation_type] + "-" + str(octave) + " " +
	notes[find_note_index(note,octave)+7][notation_type] + "-" + str(octave) + " " +
	notes[find_note_index(note,octave)+8][notation_type] + "-" + str(octave) + " " +
	notes[find_note_index(note,octave)+10][notation_type] + "-" + str(octave) + " " +
	notes[find_note_index(note,octave)+12][notation_type] + "-" + str(octave)
	)

def minor_diminished_scale(note,octave):
	return (
	notes[find_note_index(note,octave)][notation_type] + "-" + str(octave) + " " +
	notes[find_note_index(note,octave)+2][notation_type] + "-" + str(octave) + " " +
	notes[find_note_index(note,octave)+3][notation_type] + "-" + str(octave) + " " +
	notes[find_note_index(note,octave)+5][notation_type] + "-" + str(octave) + " " +
	notes[find_note_index(note,octave)+7][notation_type] + "-" + str(octave) + " " +
	notes[find_note_index(note,octave)+8][notation_type] + "-" + str(octave) + " " +
	notes[find_note_index(note,octave)+9][notation_type] + "-" + str(octave) + " " +
	notes[find_note_index(note,octave)+12][notation_type] + "-" + str(octave)
	)


def parse_magic1(pos):
	
	# print the first chord, C
	print(magic_list[0])

	# print tne second chord in the progression
	print(magic_list[pos-1])

	while not pos==1:
		# print the next chord, until we reach C again
		print(magic_list[magic1[pos-1][1]-1])
		pos=magic1[pos-1][1]

def brag_notes():
	for nota in chromatic:
		print(nota + " Gamă majoră " + ": " + major_scale(nota,4))
		print(nota + " Gamă minoră " + ": " + minor_scale(nota,4))
		print(nota + " Gamă minoră diminished " + ": " + minor_diminished_scale(nota,4))
		print(nota + " Acord major " ": " + major_chord(nota,4))
		print(nota + " Acord minor " + ": " + minor_chord(nota,4))
		print()


def brag_progression():
	for progression in range(1,6):
		print("Progression in "+str(progression+1))
		parse_magic1(progression+1)
		print()


brag_progression()
brag_notes()
#print(major_scale("Do",4))
#print(minor_scale("Do",4))
