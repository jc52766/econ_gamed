import helpers as hlp
import rich as rich
from rich.prompt import Prompt
import games as gms

def valid_games():
    return [str(x+1) for x in range(4)]

completed_games=[]

def incomplete_games():
    ic = list(set(valid_games()).difference(completed_games))
    return sorted(ic)

def f_wg():
    wg = Prompt.ask('What game would you like to play?', choices=incomplete_games())
    return wg

wg_map={"1":gms.g01,
        "2":gms.g02,
        "3":gms.g03,
        "4":gms.g04,
        }



while incomplete_games != set([]):
    wg = f_wg()
    wg_map[wg]()
    completed_games.append(wg)

