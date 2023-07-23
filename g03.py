import helpers as hlp
import random
import pandas as pd
import rich as rich
from rich.prompt import Prompt

# 1 = print game explanation
rich.print("""
***
game 3
Now we introduce an alternate means of sourcing a product. We will refer to this as A.
This alternative source has a cost of AC and profit AR.

The goal is still to maximize profit. To do so source product from primary source when that is more profitable than alternate source, else alternate source product.
Given sales are same regardless of where products are sourced from the only consideration here is the cost difference of primary v alternate sourcing.
 
Your challenge: List all products to be primary sourced.
A support column DR has been added to quantify the difference in profitability between primary and alternate source calculated as R-AR. So is positive where primary sourcing is more profitable.

Assumption is that all products not sourced from primary will be source via alternate source.
In case of zero difference between primary and alternate sourcing profitability then assume that product is sourced from primary.
Examples:
- product A primary source and secondary source both cost $10 then we would source that product from primary.
- product B primary sourcing costs $10 secondary sourcing costs $11 then this product should be primary sourced.
- product C primary sourcing costs $12 secondary sourcing costs $9 then this product should be alternate sourced.

Order of product names in solution matter. Must be listed highest to lowest financial benefit.

Complete example:

   P      S      C      R     AC     AR     DR
0  a  38.51  17.63  20.88  18.23  20.28   0.60
1  b  25.09   8.68  16.41   4.54  20.55  -4.14
2  c  29.09  12.34  16.75  15.71  13.38   3.37
3  d  27.31   1.58  25.73   1.87  25.44   0.29
4  e  26.40  14.17  12.23  13.94  12.46  -0.23
5  f  30.10  20.26   9.84  14.60  15.50  -5.66
6  g  36.02  26.41   9.61  30.58   5.44   4.17
7  h  34.65  10.50  24.15   8.68  25.97  -1.82
8  i  37.21  34.32   2.89  46.54  -9.33  12.22
9  j  34.53  26.38   8.15  23.33  11.20  -3.05
           
Correct answer: igcad        
***
""")

cc = Prompt.ask('Continue?', choices=["y", "n"])
if cc=='n':
    exit()

pc = Prompt.ask('Enter passcode')
while pc != hlp.pcodes[3]:
    pc = Prompt.ask('passcode incorrect. Enter correct passcode')

P = list('abcdefghij')
S = [round(random.randint(20000, 40000)/1000.01,2) for _ in P]
C = [round(random.random()*_,2) for _ in S]
R = [aa-bb for aa,bb in zip(S,C)]

AC = [round((0.5+random.random())*_,2) for _ in C]
AR = [aa-bb for aa,bb in zip(S,AC)]

DR = [aa-bb for aa,bb in zip(R,AR)]

df = pd.DataFrame({'P':P,'S':S, 'C':C, 'R':R, 'AC':AC, 'AR':AR, 'DR':DR})#.sort_values('R', ascending=False)
rich.print(df)
answer = ''.join(df.query("DR>=0").sort_values('DR', ascending=False)['P'])

uans = Prompt.ask('Your answer')

while uans!=answer:
    rich.print("incorrect")
    rich.print("Try again")
    flag_complete = False
    uans = Prompt.ask('Your answer')

rich.print("correct")
rich.print("Challenge completed.")
flag_complete = True

rich.print(f"Your passcode for next level is [bold cyan]{hlp.pcodes[4]}[/bold cyan]")
input('Press any key to exit.')
