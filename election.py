from mpi4py import MPI
import sys
import time

def get_name(rank):
    return chr(ord('a') + rank)

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

neighbors = None
value = 0
if rank == 0: # a
    value = 4
    neighbors = [1, 9]
elif rank == 1: # b
    value = 6
    neighbors = [0, 6, 2]
elif rank == 2: # c
    value = 3
    neighbors = [1, 3, 4]
elif rank == 3: # d
    value = 2
    neighbors = [2, 4, 5]
elif rank == 4: # e
    value = 3
    neighbors = [2, 3, 5, 6]
elif rank == 5: # f
    value = 10
    neighbors = [3, 4, 8]
elif rank == 6: # g
    value = 2
    neighbors = [1, 4, 7, 9]
elif rank == 7: # h
    value = 8
    neighbors = [6, 8]
elif rank == 8: # i
    value = 5
    neighbors = [5, 7]
elif rank == 9:
    value = 4
    neighbors = [0, 6]
    
starting_node = int(sys.argv[1])

root = None
if rank == starting_node:
    for r in neighbors:
        comm.send(rank, dest=r)
    for r in neighbors:
        comm.recv(source=r)
else:
    requests = [None for _ in neighbors]
    for i, r in enumerate(neighbors):
        requests[i] = comm.irecv(source=r)

    while root is None:
        for req in requests:
            if req.get_status():
                root = req.wait()
                break
        
    # a partir daqui já tem pai 
    for r in neighbors:
        comm.send(rank, dest=r)
    for i, req in enumerate(requests):
        req.wait()
    

for r in neighbors:
    if r != root:
        comm.isend((rank, -1), dest=r)

requests = [None for _ in neighbors]
for i, r in enumerate(neighbors):
    requests[i] = comm.irecv(source=r)

values = []
recieved = []

while len(values) < len(neighbors):
    for i in range(len(neighbors)):
        if i not in recieved and requests[i].get_status():
            recieved.append(i)
            values.append(requests[i].wait())
 
values.append((rank, value))
best = max(values, key=lambda x: x[1])

if rank != starting_node:
    comm.send(best, dest=root)
else:
    print(f"No eleito foi: ({get_name(best[0])}, {best[1]})")