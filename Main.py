import timeit

setup = """
from GameMaster import GameMaster
"""

main = """
GM = GameMaster(verbose=True, plot=True)
GM.play_game()
"""

plots = """
GM.plot()
"""

print(timeit.timeit(stmt=main, setup=setup, number=1))
print("seconds to complete and plots")
