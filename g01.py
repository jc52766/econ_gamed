import helpers as hlp
import random
import pandas as pd
import rich as rich
from rich.prompt import Prompt

# 1 = print game explanation
rich.print("""
***
game 1
given P products.
where each product has a sell price S.
Maximise total sales, assuming you can sell only 3 products. And can only sell 1 unit of each of those 3 products.
Solution structure = product names typed e.g. if products a,c,g is the answer then type 'acg' (no spaces)
Order of product names in solution matter. Must be listed highest to lowest asp
           
Complete example:
           
   P      S
8  i  39.05
9  j  38.81
1  b  37.14
0  a  33.36
7  h  33.04
4  e  27.75
5  f  26.07
6  g  23.53
3  d  22.97
2  c  20.15

Correct answer: ijb       
***
""")

cc = Prompt.ask('Continue?', choices=["y", "n"])

if cc=='n':
    exit()

P = list('abcdefghij')
S = [round(random.randint(20000, 40000)/1000.01,2) for _ in P]
df = pd.DataFrame({'P':P,'S':S}).sort_values('S', ascending=False)
rich.print(df)
answer = ''.join(df.sort_values('S', ascending=False).head(3)['P'])

uans = Prompt.ask('Your answer')

while uans!=answer:
    rich.print("incorrect")
    rich.print("Try again")
    flag_complete = False
    uans = Prompt.ask('Your answer')

rich.print("correct")
rich.print("Challenge completed.")
flag_complete = True

rich.print(f"Your passcode for next level is [bold cyan]{hlp.pcodes[2]}[/bold cyan]")
input('Press any key to exit.')
