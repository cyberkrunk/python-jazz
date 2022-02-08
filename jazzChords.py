#!/usr/bin/env python
#-------------------------------------------------------------------------------
# This code contains chords commonly used in jazz
# This is a new comment

# Section 1: 15 4-note 7th chords in root position, close position

M7 = [0, 4, 7, 11]
M7b5 = [0, 4, 6, 11]
M7s5 = [0, 4, 8, 11]
M6 = [0, 4, 7, 9]
m7 = [0, 3, 7, 10]
m7b5 = [0, 3, 6, 10]
m7s5 = [0, 3, 8, 10]
m6 = [0, 3, 7, 9]
mM7 = [0, 3, 7, 11]
D7 = [0, 4, 7, 10]
D7b5 = [0, 4, 6, 10]
D7s5 = [0, 4, 8, 10]
D7sus4 = [0, 5, 7, 10]
dim7 = [0, 3, 6, 9]
dimM7 = [0, 3, 6, 11]

# Section 2: List math to transpose the chords

t = 60
transChord = [a + t for a in M7]
print('Our base chord:')
print(transChord)

# Section 3: Define the voicings

# Close position voicings
cl_R = [0, 0, 0, 0]
cl_1 = [12, 0, 0, 0]
cl_2 = [12, 12, 0, 0]
cl_3 = [12, 12, 12, 0]

# Drop 2 voicings
d2_R = [0, 12, 0, 0]
d2_1 = [12, 0, 12, 0]
d2_2 = [12, 12, 0, 12]
d2_3 = [12, 12, 12, 0]

# Drop 3 voicings
d3_R = [0, 12, 12, 0]
d3_1 = [12, 0, 12, 0]
d3_2 = [24, 12, 0, 12]
d3_3 = [24, 24, 12, 0]

# Section 4: Iterate through the voicings
print('\nClose position voicings:')

voiceChord = sorted([a + b for a, b in zip(transChord, cl_R)])
print(voiceChord)

voiceChord = sorted([a + b for a, b in zip(transChord, cl_1)])
print(voiceChord)

voiceChord = sorted([a + b for a, b in zip(transChord, cl_2)])
print(voiceChord)

voiceChord = sorted([a + b for a, b in zip(transChord, cl_3)])
print(voiceChord)

print('\nDrop 2 voicings:')

voiceChord = sorted([a + b for a, b in zip(transChord, d2_R)])
print(voiceChord)

voiceChord = sorted([a + b for a, b in zip(transChord, d2_1)])
print(voiceChord)

voiceChord = sorted([a + b for a, b in zip(transChord, d2_2)])
print(voiceChord)

voiceChord = sorted([a + b for a, b in zip(transChord, d2_3)])
print(voiceChord)

print('\nDrop 3 voicings:')

voiceChord = sorted([a + b for a, b in zip(transChord, d3_R)])
print(voiceChord)

voiceChord = sorted([a + b for a, b in zip(transChord, d3_1)])
print(voiceChord)

voiceChord = sorted([a + b for a, b in zip(transChord, d3_2)])
print(voiceChord)

voiceChord = sorted([a + b for a, b in zip(transChord, d3_3)])
print(voiceChord)

# End of file----------
