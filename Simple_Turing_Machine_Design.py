# Turing Machine Program

'''---------------------------------------------------------------------
DATA MODEL 

A state is a string. States are viewed as the internal states of a Turing 
machine.

A symbol is a string. Symbols are viewed as the symbols that appear in cells 
of a Turing machine.

A configuration is a pair (m,s), where m is a state and s is a symbol.

A direction is either -1, 1, or 0 (for left, right, and no shift).

An action is a triple (m,s,d) where m is state, s is a symbol, and d is a 
direction. The action (m,s,d) intuitively means set the machine to internal 
state m, print the symbol s in the scanned square, and shift in direction d.

An instruction table is a dictionary, whose keys are configurations and whose 
values are actions.. The item (m1,s1):(m2,s2,d) intuitively means if the 
machine is in state m1 and the scanned square contains symbol s1, then put the 
machine in state m2, print the symbol s2 in the scanned square, and shift the 
read/write head in direction d.

A Turing machine is a dictionary of the form {'init':m, 'table':T, 
'haltStates':H} where m is a state (thought of as the initial internal state 
of the machine),  T is an instruction table, and H is a set of states.  

A tape is a list of symbols.

A complete configuration is a dictionary of the form {'state':m, 'tape':T, 
'pos':k} where m is a state, T is a tape, and k is a nonnegative integer. The 
complete configuration {'state':m, 'tape':T, 'pos':k} intuitively is read as 
follows

  1. The internal state of the machine is m;
  2. for i in {0..len(T)-1}, the symbol in square i is T[i];
  3. the symbol in square i, for   i ≥  len(T), is the blank symbol; 
  4. square k is the scanned square.

----------------------------------------------------------- end DATA MODEL'''

# TEST DATA-------------------------------------------------------------

# This section defines test data for the program.



even = 'even'
odd = 'odd'
halteven = 'halteven'
haltodd = 'haltodd'



#An instruction table is a dictionary, whose keys are configurations and whose 
#values are actions.. The item (m1,s1):(m2,s2,d) intuitively means if the 
#machine is in state m1 and the scanned square contains symbol s1, then put the 
#machine in state m2, print the symbol s2 in the scanned square, and shift the 
#read/write head in direction d.

# table,RoshTable:IITable

RoshTable ={(even,'0'):(even,'0',1),(odd,'0'):(even,'0',1),\
   (even,' '):(halteven,' ',0),(odd,' '):(haltodd,' ',0),\
   (halteven,' '):(halteven,' ',0),(haltodd,' '):(haltodd,' ',0),\
   (even,'1'):(odd,'1',1),(odd,'1'):(odd,'1',1),\
   (even,'2'):(even,'2',1),(odd,'2'):(even,'1',1),\
    (even,'3'):(odd,'3',1),(odd,'3'):(odd,'3',1),\
    (even,'4'):(even,'4',1),(odd,'4'):(even,'4',1),\
    (even,'5'):(odd,'5',1),(odd,'5'):(odd,'5',1),\
    (even,'6'):(even,'6',1),(odd,'6'):(even,'6',1),\
    (even,'7'):(odd,'7',1),(odd,'7'):(odd,'7',1),\
    (even,'8'):(even,'8',1),(odd,'8'):(even,'8',1),\
    (even,'9'):(odd,'9',1),(odd,9):(odd,'9',1)\
   }

a, b, x  = 'a','b','x'
h1,h0 = 'h1','h0'


table1 =                 \
{                        \
      (a,x) :(b,' ',1),    \
    (b,x) :(a,' ',1),    \
    (a,' '):(h0,' ',0),  \
    (b,' '):(h1,' ',0),\
      (h0,' '):(h0,' ',0),\
      (h1,' '):(h1,' ',0),
}

# TapeA,TapeB,TapeC,TapeD,TapeE,TpeF: Tape
#A tape is a list of symbols.
TapeA = [x,x,x]
TapeB = [x,x,x,x]
TapeC = [x,x,x,x,x,' ',x]
TapeD= ['1','2','3','4','5',' ']
TapeE= ['1','2','3',' ','5']
TapeF= ['3','4','5','6','7','8']



# CompConA,CompConB : CompleteConfig
#A complete configuration is a dictionary of the form {'state':m, 'tape':T, 
#'pos':k} where m is a state, T is a tape, and k is a nonnegative integer. The 
#complete configuration {'state':m, 'tape':T, 'pos':k}

CompConA = {'state':a, 'tape':TapeA, 'pos':0}
CompConB = {'state':b, 'tape':TapeB, 'pos':1}
CompConC = {'state':a, 'tape':TapeC, 'pos':2}
CompConD = {'state':odd, 'tape':TapeD, 'pos':0}
CompConE = {'state':odd, 'tape':TapeE, 'pos':2}
CompConF = {'state':even, 'tape':TapeF, 'pos':3}




# M2: TuringMachine2
#A Turing machine is a dictionary of the form {'init':m, 'table':T, 
#'haltStates':H} where m is a state (thought of as the initial internal state 
#of the machine),  T is an instruction table, and H is a set of states.

M2 = {'init':even, 'table':RoshTable, 'haltStates':{halteven,haltodd}}
M1 = {'init':a, 'table':table1, 'haltStates':{h0,h1} }

#------------------------------------------------------------ end TEST DATA


# scannedSymbol: CompleteConfig -> symbol
#scannedSymbol(C) is the scanned symbol in complete configuration C. If the
#head is one cell past the end of the tape, then the scanned symbol is the empty string ''.
def scannedSymbol(C):
      T = C['tape']
      k = C['pos']
      if k < len(T):
            return T[k]
      if k == len(T):
          return ' '

''' 1.scannedSymbol(CompConD) == '1' '''
''' 2.scannedSymbol(CompConF) == '6' '''
''' 3.scannedSymbol(CompConA) == 'x' '''
''' 4.scannedSymbol(CompConC) == 'x' '''


#action(M,C):TuringMachine*CompleteConfiguration-->state*symbol*position
#action(M,C) is the action taken by the machine M in complete configuration C.
def action(M,C):
    T = M['table']
    sym = scannedSymbol(C)
    state = C['state']
    return T[(state,sym)]

'''1.action(M1,CompConA) == ('b', 'x', 1)
   2.action(M1,CompConB) == ('a', 'x', 1)
   3.action(M2,CompConD) == ('odd', '1', 1)
   4.action(M2,CompConE) == ('odd', '3', 1)
'''
#write(M,C): TuringMachine*CompleteConfiguration-->string
#write(M,C) is the symbol written by M in complete configuration C.
def write(M,C):
      write4= action(M,C)[1]
      return write4
''' 1.write(M1,CompConC)=='x'
    2.write(M1,CompConA)== 'x'
    3.write(M2,CompConE)== '3'
    4.write(M2,CompConD)== '1'

'''
#shift(M,C):TuringMachine*CompleteConfiguration-->integer
#shift(M,C) is the direction the head of M moves on the tape when advanced one step from complete configuration C.
def shift(M,C):
      shift4 = action(M,C)[2]
      return shift4
''' 1.shift(M1, CompConB)==1
    2.shift(M1,CompConC)==1
    3.shift(M2,CompConF)== 1
    4.shift(M2,CompConD)==1
    
'''
#newState(M,C):dictionary*dictionary-->string
#newState(M,C) is the state M enters when advanced one step in complete configuration C.
def newState(M,C):
      newState4 = action(M,C)[0]
      return newState4
''' 1.newState(M1,CompConA)=='b'
    2.newState(M1,CompConB)== 'a'
    3.newState(M2,CompConD) == 'odd'
    4.newState(M2,CompConE)=='odd'
'''
#newPos(M,C):TuringMachine*CompleteConfiguration ~~>position
#newPos(M,C) is the position the head of machine M will move
#to when advanced one step from complete configuration C. If the current head position is 0 and a left
#shift is indicated, the head will remain in position 0 since a left-shift not possible.
def newPos(M,C):
      newPos3 = C['pos'] + shift(M,C)
      return newPos3

''' 1.newPos(M1,CompConC)== 3
    2.newPos(M1,CompConA) == 1
    3.newPos(M2,CompConF)== 4
    4.newPos(M2,CompConE)== 3
'''
      
#newTape(M,C):TuringMachine*CompleteConfiguration-->Tape
#newTape(M,C) is the tape that results when machine M is advanced one step from complete configuration C.
#If the head lies within the current tape, one of it symbols will be changed; if  the head is one cell
#past the end of the tape, the new symbol will be added to the end of the tape. 
def newTape(M,C):
      wa1= write(M,C)
      tyape3 = C['tape']
      
      position3 = C['pos']
      if position3 == len(tyape3):
            return tyape3 + [wa1]
      else :
            return tyape3[:position3] + [wa1] + tyape3[position3 + 1:]
''' 1. newTape(M1,CompConB)==['x', 'x', 'x']
    2. newTape(M1,CompConC)== ['x', 'x', 'x', 'x', 'x', ' ', 'x']
    3. newTape(M2,CompConD)== ['1', '2', '3', '4', '5', ' ']
    4. newTape(M2,CompConF)== ['3', '4', '5', '6', '7', '8']     
'''
#step(M,C):TuringMachine*CompleteConfiguration-->position*state*tape
#step(M,C) is the complete complete configuration that results from advancing M a single step in complete configuration C.
def step(M,C):
      
      return {'state':newState(M,C),'pos':newPos(M,C),'tape':newTape(M,C)}
'''   1.step(M1,CompConB)== {'pos': 2, 'tape': ['x', 'x', 'x'], 'state': 'a'}
      2.step(M1,CompConA)== {'tape': ['x', 'x', 'x', 'x', ' '], 'state': 'b', 'pos': 1}
      3.step(M2,CompConE)== {'tape': ['1', '2', '3', ' ', '5'], 'state': 'odd', 'pos': 3}
      4.step(M2,CompConD)== {'state': 'odd', 'pos': 1, 'tape': ['1', '2', '3', '4', '5', ' ']}

'''
#run(M,C):TuringMachine*CompleteConfiguration~~>state*position*tape
#If M  halts when run from C, then run(M,C) is the complete configuration that results from
#running M with initial complete configuration C until a halting state is reached. This function
#will be recursive.
def run(M,C):
    if C['state'] in M['haltStates']:
          return C
    else:
          return run(M,step(M,C))
''' 1.run(M1,CompConC) == {'state': 'h1', 'pos': 5, 'tape': ['x', 'x', 'x', 'x', 'x', ' ', 'x']}
    2.run(M1,CompConA) == {'state': 'h0', 'pos': 4, 'tape': ['x', 'x', 'x', 'x', ' ']}
    3.run(M2,CompConF) == {'state': 'halteven', 'pos': 6, 'tape': ['3', '4', '5', '6', '7', '8', ' ']}
    4.run(M2,CompConE)== {'state': 'haltodd', 'pos': 3, 'tape': ['2', '2', '3', ' ', '5']}

'''

#final(M,T,k):TuringMachine*Tape*position~~>stae*tape*position
#If M eventually enters one of its halting states when run from initial tape T and head position k,
#then final(M,T,k) is the complete configuration that results from running M with initial tape T and head
#position k until a halting state is reached.
def final(M,T,k):
      a = M['init']
      C = {'state':a, 'tape':T, 'pos':k}
      return run(M,C)

''' 1.final(M1,TapeB,2)== {'state': 'h1', 'tape': ['x', 'x', 'x', ' '], 'pos': 3}
    2.final(M1,TapeA,1)=={'state': 'h1', 'tape': ['x', 'x', 'x', 'x', ' '], 'pos': 4}
    3.final(M2,TapeF,0)== {'tape': ['3', '4', '5', '6', '7', '8', ' '], 'state': 'halteven', 'pos': 6}
    4.final(M2,TapeD,1)== {'tape': ['1', '2', '3', '4', '5', ' '], 'state': 'haltodd', 'pos': 5}
'''

#display(): CompleteConfiguration → Sprite.
#If C is a complete configuration, then display(C) is a sprite showing the following
def display(CC):
    
    return tape()| stepbutton()| resetbutton()| head()| symbols()| haltstate()| internalstates()

#head(): sprite
#head: is the sprite consisting of the head position
def head():
   L1 = Line(Point(200,150),Point(200,227))
   L2 = Line(Point(200,227),Point(180,200))
   L3 = Line(Point(200,227),Point(220,200))
   return {L1,L2,L3}

#startingxpos:sprite --> int
#startingxpos():is the x coordinate of the starting position of the tape
def startingxpos():
      k = CC['pos']
      x = 160
      x = x -(k*40)
      return x

#symbols(): sprite
#symbols()is the tape with symbols in each cell
def symbols():
      t = CC['tape']
      a = startingxpos()
      b = 250
      s = set()
      for i in range(0,len(t)):
            k = Text(Point((a+40),b),t[i])
            a= a + 40
            s=s |{k}
      return s


#haltstate(): sprite
#haltstate() displays the message "Halt State Reached" in case the machine has halted. 
def haltstate():
      if CC['state'] == h1 or CC['state'] == h0:
            return {Text(Point(160,400),'Halt State Reached')}
      else:
            return {Text(Point(160,400),' ')}
      
#internalstates(): sprite
#internalstate() displays the internalstate of the machine
def internalstates():
      return {Text(Point(200,142),CC['state'])}



  
   
# tape():sprite
# tape() is a sprite of the hashmarks that makes the tape.
 

def tape():
    LT = Line(Point(20,230),Point(580,230))
    LB = Line(Point(20,270),Point(580,270))
    La = Line(Point(20,230),Point(20,270))
    Lb = Line(Point(60,230),Point(60,270))
    Lc = Line(Point(100,230),Point(100,270))
    Ld = Line(Point(140,230),Point(140,270))
    Le = Line(Point(180,230),Point(180,270))
    Lf = Line(Point(220,230),Point(220,270))
    Lg = Line(Point(260,230),Point(260,270))
    Lh = Line(Point(300,230),Point(300,270))
    Li = Line(Point(340,230),Point(340,270))
    Lj = Line(Point(380,230),Point(380,270))
    Lk = Line(Point(420,230),Point(420,270))
    Ll = Line(Point(460,230),Point(460,270))
    Lm = Line(Point(500,230),Point(500,270))
    Ln = Line(Point(540,230),Point(540,270))
    Lo = Line(Point(580,230),Point(580,270))
    return{La,Lb,Lc,Ld,Le,Lf,Lg,Lh,Li,Lj,Lk,Ll,Lm,Ln,Lo,LT,LB,}



    
#resetButton(): sprite
#resetButton() is sprite of the text and circle on dsisplay that make the reset button
def resetbutton():
    circ1 = Circle(Point(450,60),15)
    txt = Text(Point(405,60),'Reset')
    return {txt,circ1}

#stepButto(): sprite
#resetButton() is sprite of the text and circle on dsisplay that make the strp button
def stepbutton():
    circ2 = Circle(Point(100,60),15)  
    txt2= Text(Point(65,60),'Step')
    return{txt2,circ2}

#inStep: int * int → Bool.
#inStep(x,y) iff the point (x,y) is in the step button.
def inStep(x,y):
    if ((((x-100)**2+(y-60)**2)**0.5)<15):
        return True
    else:
        return False

#inReset : int * int → Bool.
#inReset(x,y) iff the point (x,y) is in the reset button.
def inReset(x,y):
    if ((((x-450)**2+(y-60)**2)**0.5)<15):
        return True
    else:
          return False


#initialConfig: CompleteConfiguration. initialConfig is the complete configuration in
#which the machine begins. You can test your code with various starting configurations,
#but for your final submission use complete configuration C1a, shown b

initialConfig = {'state':a, 'tape':TapeA, 'pos':0}

#machine: TuringMachine. machine is the Turing machine that is animated by the program.
#You can test your code with various machines, but for your final submission use machine
#M1a from the test case data that was posted on the Web.

machine = {'init':a, 'table':table1, 'haltStates':{h0,h1} }


# You need to provide display, inReset, inCell, machine and initialConfig, 
# as well as step and all its helpers from the previous project.

######################################################################
# Animated Turing Machine

# Import graphics library by John Zelle,Wartburg Univ.
# downloadable at http://mcsp.wartburg.edu/zelle/python/

from graphics import *

# Create a window 
displayWidth = 600
displayHeight = 500
gameWindow = GraphWin("Turing Machine", displayWidth , displayHeight)


# CC: CompleteConfiguration
#
# The state variable CC represents the current complete configuration.

CC = initialConfig


######################################################################
# The main loop

while(True):
   images = display(CC)
   for x in images: x.draw(gameWindow)

   # wait for a mouse click, and store its
   # coordinates in click
   c = gameWindow.getMouse()
   click = (c.getX(),c.getY())


   # if the reset button has been clicked, reset the
   # game state
   if inReset(click[0],click[1]):
       CC = initialConfig

  
 

   # If 'step' has been clicked, advance the machine
   # note: there was an error in this until 1:20 PM Friday
  
   if inStep(click[0],click[1]):
          CC = step(machine,CC)
           
   # undraw the screen
   for I in images: I.undraw()
  


