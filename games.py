import helpers as hlp
import random
import pandas as pd
import rich as rich
from rich.prompt import Prompt

def g01():
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

def g02():
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

def g03():
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

def g04():
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

