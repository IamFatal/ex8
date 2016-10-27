# MemoryExercise
### A quick exercise with memory. ###
* Runs a program
* Uses Valgrind to produce a memory reference trace
* Filter output of trace to focus only on memory references related to the algorithm
* Analyze memory access patterns and examine how programs use memory.

### Programs included: ###
**refstring.py:** used to filter output of Valgrind memory reference trace  
**heaploop.c, matmul.c:** sample programs used in the trace

**analyze.py:**
* translates each memory reference into a page number assuming pages are 4096 bytes
* outputs a table of
 * each unique instruction page with a count of the number of accesses for each page
 * each unique data page with a count of the number of accesses for each page

### Example ###
**e.g. trace file:**  
```0x7ff0008e8,S  
0x400590,I  
0x601020,L  
0x400596,I  
0x7ff0008e0,S  
0x4fdf720,M
```

Each comma-separated line begins with a memory address in hexadecimal, and the character in the second field determines the type of access: **I** - instruction, **S** - store, **L** - load, **M** - modify. **S**, **L**, and **M** accesses are all data accesses.

**analyze.py output:**  
```
Instructions:  
0x400 2

Data:  
0x7ff000 2  
0x601 1  
0x4fdf 1  
  
# of instruction pages: 1 
# of data pages: 		3 
most accessed i-page: 	0x400 2 
most accessed d-page: 	0x7ff000 2
```
