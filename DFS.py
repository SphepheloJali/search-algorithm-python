class DFS:

    state_num = 0
    visited = set()
    
    def printstate(self, A, B, C, D, E):
        DFS.state_num += 1
        states_dict = {"E": E, "A": A, "B": B, "C": C, "D": D}
        print("\n\nstate :", DFS.state_num, " \n", states_dict)
    
    def moveDisc(self, FROM,TO):
        if (FROM[-1] != 0):
            if(TO[-1] == 0):
                TO.remove(TO[-1])
            TO.append(FROM[-1])
            FROM.remove(FROM[-1])
            if (len(FROM) == 0):
                FROM.append(0)
            self.printstate(A,B,C,D,E)
    def movefromE(self, E, TO):
        if(TO[-1] < E[0]):
            if(TO[-1] == 0):
                TO.remove(TO[-1])
                TO.append(E[0])
                E.remove(E[0])
        self.printstate(A,B,C,D,E)

    def moveToE(self, FROM, E):
        E.insert(0,FROM[-1])
        FROM.remove(FROM[-1])
        if(len(FROM) == 0):
            FROM.append(0)
        self.printstate(A,B,C,D,E)





    def DFS_Search(self,A,B,C,D,E):
         while E:
            current_state = (tuple(A), tuple(B), tuple(C), tuple(D), tuple(E))
            if current_state in DFS.visited:
                continue
            DFS.visited.add(current_state)

            if((A[-1]) <E[0] and E[0]% 2 != 0 ):#E to A
                self.movefromE(E,A)
            if((C[-1]) <E[0] and E[0]% 2 != 0 ):#E to C
                self.movefromE(E,C)
            if((B[-1]) < E[0] and E[0]% 2 == 0 ): #E to B
                self.movefromE(E,B)
            if((D[-1]) < E[0] and E[0]% 2 == 0 ): #E to D
                self.movefromE(E,D)
            if(A[-1] > C[-1] ): # C to A
                self.moveDisc(C,A)
            if(C[-1] > A[-1] ): # A to C
                self.moveDisc(A,C)
            if(D[-1] < B[-1] ): # A to C
                self.moveDisc(D,B)
            if(D[-1] > B[-1] ): # A to C
                self.moveDisc(B,D)

            

            



disc = int(input("Enter a number of Discs (4, 6, or 8): "))
if(disc > 10):
    print("you must Enter a number of Discs (4, 6, or 8):")
else:

    A = [0]
    B = [0]
    C = [0]
    D = [0]
    E = list(range(1, disc + 1))
    initial_states_dict = {"E": E, "A": A, "B": B, "C": C, "D": D}
    print("initial State: ",initial_states_dict,"\n")

    search = DFS()
    search.DFS_Search(A, B, C, D, E)

    