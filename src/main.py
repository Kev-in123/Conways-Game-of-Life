from conway import Conway

c = Conway()

for _ in range(20):
    # print the grid
    c.print_grid()
    # update the grid
    c.cycle()
    # print a line
    print('------------------')
