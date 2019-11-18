import codecs
import sys

inputfile = str(sys.argv[1]) #sys.argv[0] is the name of the python program, sys.arg[1] is the file path
#filepath = '/dropbox/19-20/473/project3/fsm-input.utf8.txt'
f = codecs.open(inputfile,encoding = 'utf-8') #('input.utf8.txt', encoding='utf-8')
lines = f.readlines()
f.close()

outputfile = str(sys.argv[2])

out = file(outputfile, "w" )

inputText = ''

for i in range(len(lines)):
        lineText = lines[i],
        lineText = str(lineText)[3:-3]
        inputText = inputText + lineText.rstrip()

mergedText = eval('u\''+inputText+'\'')
maxIndex = len(mergedText)

#Character set definition : unicode

#V1 0E40, 0E41, 0E42, 0E43, 0E44
#C1 0E01 - 0E2E
#C2 0E19, 0E21, 0E23, 0E25, 0E27
#V2 0E31, 0E34, 0E35, 0E36, 0E37, 0E38, 0E39, 0E47
#T 0E48, 0E49, 0E4A, 0E4B
#V3 0E22, 0E27, 0E2D, 0E32
#C3 0E01, 0E07, 0E14, 0E19, 0E1A, 0E21, 0E22, 0E27

V1 = [u"\u0E40", u"\u0E41", u"\u0E42", u"\u0E43", u"\u0E44"]

C1 = [u"\u0E01", u"\u0E02", u"\u0E03", u"\u0E04", u"\u0E05", u"\u0E06", u"\u0E07", u"\u0E08", u"\u0E09", u"\u0E0A",
      u"\u0E0B", u"\u0E0C", u"\u0E0D", u"\u0E0E", u"\u0E0F", u"\u0E10", u"\u0E11", u"\u0E12", u"\u0E13", u"\u0E14",
      u"\u0E15", u"\u0E16", u"\u0E17", u"\u0E18", u"\u0E19", u"\u0E1A", u"\u0E1B", u"\u0E1C", u"\u0E1D", u"\u0E1E",
      u"\u0E1F", u"\u0E20", u"\u0E21", u"\u0E22", u"\u0E23", u"\u0E24", u"\u0E25", u"\u0E26", u"\u0E27", u"\u0E28",
      u"\u0E29", u"\u0E2A", u"\u0E2B", u"\u0E2C", u"\u0E2D", u"\u0E2E"]

C2 = [u"\u0E19", u"\u0E21", u"\u0E23", u"\u0E25", u"\u0E27"]

V2 = [u"\u0E31", u"\u0E34", u"\u0E35", u"\u0E36", u"\u0E37"]

T = [u"\u0E48", u"\u0E49", u"\u0E4A", u"\u0E4B"]

V3 = [u"\u0E22", u"\u0E27", u"\u0E2D", u"\u0E32"]

C3 = [u"\u0E01", u"\u0E07", u"\u0E14", u"\u0E19", u"\u0E1A", u"\u0E21", u"\u0E22", u"\u0E27"]


#D-FSM Rules

currentstate = 0 #initial state
begin = 0
end = -1
index = -1

syllables = ''

for char in mergedText:
    
    index = index + 1

    if char == '\n':
        #End of line text. write remaining characters.
        end = index
        syllable = mergedText[begin:end]

        syllables = syllables + syllable 

#        print(syllables.encode('utf-8'))

        out.write(syllables.encode('utf-8'))
        out.write('\n')

        syllables = ''
        currentstate = 0 
        begin = index + 1

    if currentstate == 0: # state 0
        #Accept V1/C1
        if char in V1:
            #V1 to 1:
            currentstate = 1
            #print('0 -> 1')
        elif char in C1:
            #C1 to 2
            currentstate = 2
            #print('0 -> 2')
        elif begin < maxIndex:
	    #syllable must begin with either V1 or C1
            if mergedText[begin] in V1 or mergedText[begin] in C1:
                pass
            else:
                begin = begin + 1

    elif currentstate == 1: # state 1
        #Accept C1
        if char in C1:
            #C1 to 2
            currentstate = 2 
            #print('1 -> 2')
    elif currentstate == 2: # state 2
        #Accept C2/V2/T/V3/C3/V1/C1
        if char in C2:
            #C2 to 3
            currentstate = 3
            #print('2 -> 3')
        elif char in V2:
            #V2 to 4
            currentstate = 4
            #print('2 -> 4')
        elif char in T:
            #T to 5
            currentstate = 5
            #print('2 -> 5')          
        elif char in V3:
            #V3 to 6
            currentstate = 6
            #print('2 -> 6')          
        elif char in C3:
            #C3 to 9
            currentstate = 9
            #print('2 -> 9')        
        elif char in V1:
            #V1 to 7
            currentstate = 7
            #print('2 -> 7')          
        elif char in C1:
            #C1 to 8
            currentstate = 8
            #print('2 -> 8')  
  
    elif currentstate == 3: # state 3
        #Accept V2/T/V3/C3
        if char in V2:
            #V2 to 4
            currentstate = 4
            #print('3 -> 4') 
        elif char in T:
            #T to 5
            currentstate = 5
            #print('3 -> 5')
        elif char in V3:
            #V3 to 6
            currentstate = 6
            #print('3 -> 6') 
        elif char in C3:
            #C3 to 9
            currentstate = 9
            #print('3 -> 9') 
    elif currentstate == 4: # state 4
        #Accept T/V3/C3/V1/C1
        if char in T:
            #T to 5
            currentstate = 5
            #print('4 -> 5')
        elif char in V3:
            #V3 to 6
            currentstate = 6
            #print('4 -> 6')
        elif char in C3:
            #C3 to 9
            currentstate = 9
            #print('4 -> 9')
        elif char in V1:
            #V1 to 7
            currentstate = 7
            #print('4 -> 7')
        elif char in C1:
            #C1 to 8
            currentstate = 8
            #print('4 -> 8')
    elif currentstate == 5: # state 5
        #Accept V3/C3/V1/C1
        if char in V3:
            #V3 to 6
            currentstate = 6
            #print('5 -> 6')
        elif char in C3:
            #C3 to 9
            currentstate = 9
            #print('5 -> 9')
        elif char in V1:
            #V1 to 7
            currentstate = 7
            #print('5 -> 7')
        elif char in C1:
            #C1 to 8 
            currentstate = 8
            #print('5 -> 8')
    elif currentstate == 6: # state 6
        #Accept C3/V1/C1
        if char in C3:
            #C3 to 9
            currentstate = 9
            #print('6 -> 9')
        elif char in V1:
            #V1 to 7
            currentstate = 7
            #print('6 -> 7')            
        elif char in C1:
            #C1 to 8
            currentstate = 8
            #print('6 -> 8')             
    elif currentstate == 7: # state 7
        #Break before previous character
        end = index - 1
        syllable = mergedText[begin:end]
        syllables = syllables + syllable + ' '
        
	begin = end

        currentstate = 1
        #print('7 -> 1')    
        
    elif currentstate == 8: # state 8
        #Break before previous character
        end = index - 1
        syllable = mergedText[begin:end]
        syllables = syllables + syllable + ' '
        
	begin = end

        currentstate = 2
        #print('8 -> 2')

    elif currentstate == 9: # state 9
        #Break now
        end = index
        syllable = mergedText[begin:end]
        syllables = syllables + syllable + ' '

	#syllable must begin with either V1 or C1
        if mergedText[end] in V1 or mergedText[end] in C1: 
            begin = end
        else: #extend
            begin = end+1 #begin at
        
        currentstate = 0
        #print('9 -> 0')
