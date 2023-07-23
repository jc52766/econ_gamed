import helpers as hlp
import random
import pandas as pd
import rich as rich
from rich.prompt import Prompt

# 1 = print game explanation
rich.print("""
***
game 2
Same idea as game 1 but now we introduct product costs C and profit R.
Our goal in game 2 is to maximise profit (not sales).
All other constraints still apply.

Complete example:
           
   P      S      C      R
0  a  35.24  14.26  20.98
1  b  27.81  17.93   9.88
2  c  31.23  21.89   9.34
3  d  31.26  28.10   3.16
4  e  23.44  21.63   1.81
5  f  33.50  21.02  12.48
6  g  39.80  17.07  22.73
7  h  37.30  35.67   1.63
8  i  27.53  19.64   7.89
9  j  33.12   0.91  32.21

Correct answer: jga 
***
""")

cc = Prompt.ask('Continue?', choices=["y", "n"])
if cc=='n':
    exit()

pc = Prompt.ask('Enter passcode')
while pc != hlp.pcodes[2]:
    pc = Prompt.ask('passcode incorrect. Enter correct passcode')

P = list('abcdefghij')
S = [round(random.randint(20000, 40000)/1000.01,2) for _ in P]
C = [round(random.random()*_,2) for _ in S]
R = [aa-bb for aa,bb in zip(S,C)]
df = pd.DataFrame({'P':P,'S':S, 'C':C, 'R':R})#.sort_values('R', ascending=False)
rich.print(df)
answer = ''.join(df.sort_values('R', ascending=False).head(3)['P'])

uans = Prompt.ask('Your answer')

while uans!=answer:
    rich.print("incorrect")
    rich.print("Try again")
    flag_complete = False
    uans = Prompt.ask('Your answer')

rich.print("correct")
rich.print("Challenge completed.")
flag_complete = True

rich.print(f"Your passcode for next level is [bold cyan]{hlp.pcodes[3]}[/bold cyan]")
input('Press any key to exit.')
