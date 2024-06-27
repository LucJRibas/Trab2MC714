from mpi4py import MPI
import time

comm = MPI.COMM_WORLD
rank = comm.rank

want_data = False
prio = float('inf')

if rank == 4:
    prio = 20
    want_data = True
if rank == 3:
    prio = 8
    want_data = True
elif rank == 0:
    prio = 12
    want_data = True

data_candidates = comm.allgather(want_data) 
prio = comm.allgather(prio)
        
# print(rank, data_candidates, data)

if not want_data:
    requests = [None for _ in data_candidates]
    for i, want in enumerate(data_candidates):
        if i != rank and want:
            requests[i] = comm.isend("ok", dest=i)
    for i, want in enumerate(data_candidates):
        if i != rank and want:
            requests[i].wait()
else:
    while want_data:
        min_rank = prio.index(min(prio))
        if min_rank != rank:
            comm.send("ok", dest=min_rank)
            data_candidates[min_rank] = False
            prio[min_rank] = float('inf')
        else:
            prio[min_rank] = float('inf')
            for i in range(comm.size):
                if i != min_rank:
                    res = comm.recv(source=i)
                    if res != "ok":
                        raise Exception("Not ok!")
            
            
            print(f"{rank} using critical data!")
            time.sleep(2)
            print("slept for 2 seconds")
            want_data = False
            
            for i, want in enumerate(data_candidates):
                if i != min_rank and want:
                    comm.send("ok", dest=i)
                    
		