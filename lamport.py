from mpi4py import MPI

comm = MPI.COMM_WORLD

rank = comm.Get_rank()

size = comm.Get_size()

clock_add = 6 + 2*rank

actions = []
# ações predefinidas de cada processo
if rank == 0:
    actions = ['', 's1', '', '', '', '', '', '', '', '', 'r1', '']
elif rank == 1:
    actions = ['', '', 'r0', 's2', '', '', '', 'r2', 's0', '', '', '']
elif rank == 2:
    actions = ['', '', '', '', 'r1', '', 's1', '', '', '', '', '']

# cada um abre seu próprio arquivo para escrever
with open(f"rank_{rank}.txt", "w") as f:
    clock = 0
    for a in actions:
        to_write = ""
        if a != '':
            if a[0] == 's':
                msg = (clock, "oi")
                to_write = f" -> sending message {msg} to {int(a[1])}"
                comm.send(msg, dest=int(a[1]))
            else:
                msg = comm.recv(source=int(a[1]))
                prev = clock
                if msg[0] > clock:
                    clock = msg[0] + 1
                to_write = f" -> recieving message {msg} from {int(a[1])}, prev clock was: {prev}"
        f.write(f"{clock}" + to_write + "\n")
        clock += clock_add