import helpers as hlp
import random
import pandas as pd
import rich as rich
from rich.prompt import Prompt

# 1 = print game explanation
rich.print("""
***
game 4
           
Same as game 3 but this time list which products will be alternate sourced.
But there's a catch.
We have now included information re product availability (or lack of) in alternate source.
Column AA added to represent alternate availability.

If not available in alternate source then product must be primary sourced.
If there is availability then source via most profitable sourcing channel.
So for this challenge return those product with alternate availability where alternate channel is more profitable than primary.
Note that correct answer can be empty.

Order of product names in solution matter. Must be listed highest to lowest financial benefit.

Complete example:

   P      S      C      R     AC     AR     DR     AA
0  a  32.22   3.91  28.31   3.60  28.62  -0.31   True
1  b  27.08   9.71  17.37   6.99  20.09  -2.72  False
2  c  32.28  19.45  12.83  11.10  21.18  -8.35  False
3  d  30.77  24.47   6.30  36.14  -5.37  11.67   True
4  e  31.79  26.14   5.65  20.33  11.46  -5.81  False
5  f  39.67  38.32   1.35  36.53   3.14  -1.79   True
6  g  26.81  16.65  10.16  23.88   2.93   7.23  False
7  h  32.29  22.75   9.54  20.80  11.49  -1.95  False
8  i  38.65  21.72  16.93  12.01  26.64  -9.71   True
9  j  34.88  15.53  19.35  22.71  12.17   7.18  False

Correct answer: 'ifa'
***
""")

cc = Prompt.ask('Continue?', choices=["y", "n"])
if cc=='n':
    exit()

pc = Prompt.ask('Enter passcode')
while pc != hlp.pcodes[4]:
    pc = Prompt.ask('passcode incorrect. Enter correct passcode')

P = list('abcdefghij')
S = [round(random.randint(20000, 40000)/1000.01,2) for _ in P]
C = [round(random.random()*_,2) for _ in S]
R = [aa-bb for aa,bb in zip(S,C)]

AC = [round((0.5+random.random())*_,2) for _ in C]
AR = [aa-bb for aa,bb in zip(S,AC)]

DR = [aa-bb for aa,bb in zip(R,AR)]

AA = [True if random.randint(1, 10)%2==0 else False for _ in range(10)]

df = pd.DataFrame({'P':P,'S':S, 'C':C, 'R':R, 'AC':AC, 'AR':AR, 'DR':DR, 'AA':AA})#.sort_values('R', ascending=False)
rich.print(df)
answer = ''.join(df.query("(DR<=0) & (AA)").sort_values('DR', ascending=True)['P'])

uans = Prompt.ask('Your answer')

while uans!=answer:
    rich.print("incorrect")
    rich.print("Try again")
    flag_complete = False
    uans = Prompt.ask('Your answer')

rich.print("correct")
rich.print("Challenge completed.")
flag_complete = True

rich.print(f"Your passcode for next level is [bold cyan]{hlp.pcodes[5]}[/bold cyan]")
input('Press any key to exit.')
