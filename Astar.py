#220055031 Sphephelo Jali
class Astar:
    state_num = 0
    heuristic = 0
    cost = 0
    evaluationF = 0

    def printstate(self, A, B, C, D, E):
        print("\n")
        Astar.state_num += 1
        State_dict = {"E": E, "A": A, "B": B, "C": C, "D": D}

        Astar.heuristic = len(E)  # Number of discs left in E
        Astar.cost = 1  # Cost is the number of states visited (moves)
        Astar.evaluationF = Astar.heuristic + Astar.cost
        
        print(f"h(n) : {Astar.heuristic} \n" 
              f"g(n) : {Astar.cost} \n" 
              f"f(n) : {Astar.evaluationF} \n " 
              f"State : {Astar.state_num}  {State_dict}")
    
    def astar_search(self,A,B,C,D,E):
       
        #print("initial state \n", State_dict)
        while E:
            if not E :
               
                break
           
            if(A[0] == 0 or B[0] == 0 or  C[0] == 0 or D[0] == 0 ):
                for i in range(len(E)):
                    if(min(E)%2 != 0 and A[0] == 0):
                        A[0] = min(E)
                        E.pop(0)
                        self.printstate(A,B,C,D,E)
                    elif(min(E)%2 != 0 and C[0] == 0):
                        C[0] = min(E)
                        E.pop(0)
                        self.printstate(A,B,C,D,E)
                           
                    if(min(E)%2 == 0 and B[0] == 0):
                        B[0] = min(E)
                        E.pop(0)
                        self.printstate(A,B,C,D,E)
                    elif(min(E)%2 == 0 and D[0] == 0):
                        D[0] = min(E)
                        E.pop(0)
                        self.printstate(A,B,C,D,E)
            elif((A[0] != 0 and C[0] != 0 ) or  ( D[0] != 0 and D[0] != 0 )):
                if (A[0] < C[0] and A[0] != 0):
                    if(min(A) == A[0]):
                        C.append(A[0])
                        A[0] = 0
                        self.printstate(A,B,C,D,E)
                     
                if (B[0] < D[0] and B[0] != 0):
                    if(min(B) == B[0]):
                        D.append(B[0])
                        B[0] = 0
                        self.printstate(A,B,C,D,E)
                a = A+B+C+D
               
                for i in a:
                    if E[0] >i  and A[0] !=0 and len(C) >1 and B[0] != 0:
                        b = A + C
                        if b:
                            Min = min(b)
                        if Min in A:
                            A.remove(Min)
                        elif Min in C:
                            C.remove(Min)
                   
                    # Insert Min back at the start of E
                        E.insert(0, Min)
                        self.printstate(A, B, C, D, E)
                   
                    if(len(E) == 1 and len(D) > 1):
                        c = B + D
                        if c:
                            Min = min(c)
                        if Min in B:
                            B.remove(Min)
                        elif Min in D:
                            D.remove(Min)
                   
                        
                    # Insert Min back at the start of E
                        E.insert(0, Min)
                        self.printstate(A, B, C, D, E)
                        
                        if((len(E) == 3 and len(D)> 1)):
                            D.remove(D[-1])
                            E.insert(0,D[-1])
                   
                       
                if (max(A) > C[0] and C[0] != 0):
                    A.append(C[0])
                    C[0] = 0
                    self.printstate(A,B,C,D,E)
                   
                if (B[0] > D[0] and D[0] != 0):
                    if(min(D) == D[0]):
                        B.append(D[0])
                        D[0] = 0
                        self.printstate(A,B,C,D,E)    
                   
                       
            if not E:
                print("Final state is Reached!! with ", Astar.state_num, " States using a DFS Search")

# Main Execution
disc = int(input("Enter a number of Discs (4, 6, or 8): "))
if(disc > 8):
    print("you must Enter a number of Discs (4, 6, or 8):")
else:

    A = [0]
    B = [0]
    C = [0]
    D = [0]
    E = list(range(1, disc + 1))
    print(" h(n) : 8 \n g(n) : 0  ")
    initial_states_dict = {"E": E, "A": A, "B": B, "C": C, "D": D}
    print("initial State: ",initial_states_dict,"\n")

    search = Astar()
    search.astar_search(A, B, C, D, E)
