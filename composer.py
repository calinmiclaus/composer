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

#TODO:
# parametrizează octava. Fă un array Do[3,4,5]. Sau o funcție. Trebuie să returneze și midi value. poate fi adăugat doar un câmp la notes pentru easy fix
# diferențele între octave se pot face cu -12 sau +12. Înmulțit cu un factor, în funcție de câte octave în plus sau în minus se merge


# notation_type: 1=american(C4), 2=italian(Do4)
notation_type = 2

# first value is the midi note value. Use https://pypi.org/project/MIDIUtil/ for midi integration
notes = [
[48,"C-3","Do-3"],
[49,"C#-3","Do#-3"],
[50,"D-3","Re-3"],
[51,"D#-3","Re#-3"],
[52,"E-3","Mi-3"],
[53,"F-3","Fa-3"],
[54,"F#-3","Fa#-3"],
[55,"G-3","Sol-3"],
[56,"G#-3","Sol#-3"],
[57,"A-3","La-3"],
[58,"A#-3","La#-3"],
[59,"B-3","Si-3"],

[60,"C-4","Do-4"],
[61,"C#-4","Do#-4"],
[62,"D-4","Re-4"],
[63,"D#-4","Re#-4"],
[64,"E-4","Mi-4"],
[65,"F-4","Fa-4"],
[66,"F#-4","Fa#-4"],
[67,"G-4","Sol-4"],
[68,"G#-4","Sol#-4"],
[69,"A-4","La-4"],
[70,"A#-4","La#-4"],
[71,"B-4","Si-4"],

[72,"C-5","Do-5"],
[73,"C#-5","Do#-5"],
[74,"D-5","Re-5"],
[75,"D#-5","Re#-5"],
[76,"E-5","Mi-5"],
[77,"F-5","Fa-5"],
[78,"F#-5","Fa#-5"],
[79,"G-5","Sol-5"],
[80,"G#-5","Sol#-5"],
[81,"A-5","La-5"],
[82,"A#-5","La#-5"],
[83,"B-5","Si-5"],
]

# folosește-te aici de octava parametrizată, dacă poți
#fifths = ["C-4", "G-4", "D-4", "A-4", "E-4", "B-4", "F#-4", "C#-4", "G#-4", "D#-4", "A#-4", "F-4"]

chromatic = ["Do-4","Do#-4","Re-4", "Re#-4", "Mi-4", "Fa-4", "Fa#-4", "Sol-4", "Sol#-4", "La-4", "La#-4", "Si-4"]

magic_list=["Do-major","Re-minor","Mi-minor", "Fa-major", "Sol-major", "La-minor", "Si-dimiinshed"]

magic1=[ [1,0],[2,5],[3,6],[4,5],[5,1],[6,2] ]
magic2=[ [1,0],[2,5],[3,6],[4,1],[5,1],[6,2] ]

def find_note_index(note):
	for i in range(len(notes)):
		if(note==notes[i][notation_type]):
		   return i
	return False


def major_chord(note):
	return(
	notes[find_note_index(note)][notation_type] + " " + 
	notes[find_note_index(note)+4][notation_type] + " " + 
	notes[find_note_index(note)+7][notation_type]
	)

def minor_chord(note):
	return(
	notes[find_note_index(note)][notation_type] + " " + 
	notes[find_note_index(note)+3][notation_type] + " " + 
	notes[find_note_index(note)+7][notation_type]
	)

def major_scale(note):
	return(
	notes[find_note_index(note)][notation_type] + " " + 
	notes[find_note_index(note)+2][notation_type] + " " + 
	notes[find_note_index(note)+4][notation_type] + " " + 
	notes[find_note_index(note)+5][notation_type] + " " + 
	notes[find_note_index(note)+7][notation_type] + " " + 
	notes[find_note_index(note)+9][notation_type] + " " + 
	notes[find_note_index(note)+11][notation_type] + " " +
	notes[find_note_index(note)+12][notation_type]
	)

def minor_scale(note):
	return(
	notes[find_note_index(note)][notation_type] + " " + 
	notes[find_note_index(note)+2][notation_type] + " " + 
	notes[find_note_index(note)+3][notation_type] + " " + 
	notes[find_note_index(note)+5][notation_type] + " " + 
	notes[find_note_index(note)+7][notation_type] + " " + 
	notes[find_note_index(note)+8][notation_type] + " " + 
	notes[find_note_index(note)+10][notation_type] + " " +
	notes[find_note_index(note)+12][notation_type]
	)

def minor_diminished_scale(note):
	return (
	notes[find_note_index(note)][notation_type] + " " + 
	notes[find_note_index(note)+2][notation_type] + " " + 
	notes[find_note_index(note)+3][notation_type] + " " + 
	notes[find_note_index(note)+5][notation_type] + " " + 
	notes[find_note_index(note)+7][notation_type] + " " + 
	notes[find_note_index(note)+8][notation_type] + " " + 
	notes[find_note_index(note)+9][notation_type] + " " +
	notes[find_note_index(note)+12][notation_type]
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
		print(nota + " Gamă majoră " + ": " + major_scale(nota))
		print(nota + " Gamă minoră " + ": " + minor_scale(nota))
		print(nota + " Gamă minoră diminished " + ": " + minor_diminished_scale(nota))
		print(nota + " Acord major " ": " + major_chord(nota))
		print(nota + " Acord minor " + ": " + minor_chord(nota))
		print()


def brag_progression():
	for progression in range(1,6):
		print("Progression in "+str(progression+1))
		parse_magic1(progression+1)
		print()


brag_progression()
brag_notes()
