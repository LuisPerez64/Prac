import time

for inp in range(10,0,-1):
    print('{0} second{1} left til termination'.format(inp, 's' if inp != 1 else ''))
    time.sleep(1)
    
