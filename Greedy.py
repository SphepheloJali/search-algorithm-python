#220055031 Sphephelo Jali
class Greedy:
    state_num = 0
    heuristic = 0
    visited = set()

    def printstate(self, A, B, C, D, E):
        print("\n")
        Greedy.state_num += 1
        State_dict = {"E": E, "A": A, "B": B, "C": C, "D": D}

        Greedy.heuristic = len(E)  # Number of discs left in E
       
        
        print(f"h(n) : {Greedy.heuristic} \n" 
              
              f"State : {Greedy.state_num}  {State_dict}")
    
    def addState(self, A, B, C, D, E):
        state = (tuple(A), tuple(B), tuple(C), tuple(D), tuple(E))
        if state not in Greedy.visited:
            self.printstate(A, B, C, D, E)
            Greedy.visited.add(state)
                
    def moveEtoA(self, E, A, B, C, D):
        move_made = False
        if E and E[0] % 2 != 0:
            A.remove(0)
            A.append(E[0])
            E.pop(0)
            move_made = True
        if move_made:
            self.addState(A, B, C, D, E)

    def moveAtoC(self, A, C, B, D):
        move_made = False
        if A and C and A[-1] < C[-1] and C[0] != 0:
            C.append(A[-1])
            A.remove(A[-1])
            if len(A) == 0:
                A.append(0)
            move_made = True
        elif C and C[0] == 0:
            C.pop(0)
            C.append(A[-1])
            A.remove(A[-1])
            if len(A) == 0:
                A.append(0)
            move_made = True
        if move_made:
            self.addState(A, B, C, D, E)

    def moveCtoA(self, C, A, B, D):
        move_made = False
        if C and A and C[-1] < A[-1] and C[-1] != 0:
            A.append(C[-1])
            C.remove(C[-1])
            if len(C) == 0:
                C.append(0)
            move_made = True
        if move_made:
            self.addState(A, B, C, D, E)

    def moveEtoB(self, E, B, A, C, D):
        move_made = False
        if E and E[0] % 2 == 0:
            if 0 in B:
                B[B.index(0)] = E[0]
                E.pop(0)
                move_made = True
        if move_made:
            self.addState(A, B, C, D, E)

    def moveBtoD(self, B, D, A, C):
        move_made = False
        if B and D and B[-1] < D[-1] and D[0] != 0:
            D.append(B[-1])
            B.pop(-1)
            if len(B) == 0:
                B.append(0)
            move_made = True
        elif B and D and D[0] == 0:
            D.pop(0)
            D.append(B[-1])
            B.remove(B[-1])
            if len(B) == 0:
                B.append(0)
            move_made = True
        if move_made:
            self.addState(A, B, C, D, E)

    def moveDtoB(self, D, B, A, C):
        move_made = False
        if D and B and D[-1] < B[-1]:
            B.append(D[0])
            D.append(0)
            D.remove(D[0])
            move_made = True
        if move_made:
            self.addState(A, B, C, D, E)

    def moveEtoC(self, E, C, A, B, D):
        move_made = False
        if E and E[0] % 2 != 0:
            C.remove(0)
            C.append(E[0])
            E.pop(0)
            move_made = True
        if move_made:
            self.addState(A, B, C, D, E)
   
    def moveEtoD(self, E, D, A, B, C):
        move_made = False
        if E and E[0] % 2 == 0:
            if 0 in D:
                D[D.index(0)] = E[0]
                E.pop(0)
                move_made = True
        if move_made:
            self.addState(A, B, C, D, E)
    
    def moveCtoE(self, C, E, A, B, D):
        move_made = False
        if C[-1] != 0 and E[0] % 2 != 0:
            E.insert(0, C[-1])
            C.remove(C[-1])
            move_made = True
        if move_made:
            self.addState(A, B, C, D, E)

    def moveBtoE(self, B, E, A, C, D):
        move_made = False
        if B[-1] != 0 and E[0] % 2 == 0:
            E.insert(0, B[-1])
            B.remove(B[-1])
            move_made = True
        if move_made:
            self.addState(A, B, C, D, E)
    
    def is_final(self, E):
        if len(E) == 0:
            print("final state reached!!!")        
            
    def greedy(self, A, B, C, D, E):
        visited_states = set()  # Track visited states
        while E:
            current_state = (tuple(A), tuple(B), tuple(C), tuple(D), tuple(E))
            if current_state in visited_states:
                continue
            visited_states.add(current_state)
           
            if A[0] == 0:
                self.moveEtoA(E, A, B, C, D)
            if A and A[0] != 0:
                self.moveAtoC(A, C, B, D)
            if A and C and A[-1] != 0 and C[-1] != 0:
                self.moveCtoA(C, A, B, D)
            if B and B[0] == 0:
                self.moveEtoB(E, B, A, C, D)
            if B and B[0] != 0 and len(B) == 1:
                self.moveBtoD(B, D, A, C)
            if D and B and D[-1] != 0 and B[-1] != 0 and len(E) != 0:
                self.moveDtoB(D, B, A, C)
            if C and C[0] == 0:
                self.moveEtoC(E, C, A, B, D)
            if D and D[0] == 0:
                self.moveEtoD(E, D, A, B, C)
            if A and E and C[-1] < E[0] and len(E) < 4 and A[-1] == 1:
                self.moveCtoE(A, E, A, B, D)
            if B and E and B[-1] < E[0] and len(E) < 4 and B[-1] == 2:
                self.moveBtoE(B, E, A, C, D)
            if not E:
                self.is_final(E)
                Greedy.state_num = 0
                break

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

    search = Greedy()
    search.greedy(A, B, C, D, E)