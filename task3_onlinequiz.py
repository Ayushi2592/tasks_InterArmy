class QZ:
    def __init__(self):
        self.Qs = []
        self.As = []
        self.PN = ""
        self.RN = ""
        self.AG = ""
        self.TS = 0

    def get_info(self):
        self.PN = input("Enter your name: ")
        self.RN = input("Enter your roll number: ")
        self.AG = input("Enter your age: ")

    def mcq(self, Q, O, CA):
        self.Qs.append({
            'Q': Q,
            'O': O,
            'CA': CA
        })

    def tfq(self, Q, CA):
        self.Qs.append({
            'Q': Q,
            'CA': CA
        })

    def conduct(self):
        self.get_info()

        for i, qd in enumerate(self.Qs, 1):
            print(f"\nQ{i}: {qd['Q']}")
            if 'O' in qd:
                for j, o in enumerate(qd['O'], 1):
                    print(f"{j}. {o}")

                uA = int(input("Enter your choice (1, 2, 3, etc.): "))
                CA = qd['CA']
                if uA == CA:
                    self.As.append(True)
                    self.TS += 1
                    print("Correct!\n")
                else:
                    self.As.append(False)
                    print(f"Wrong! Correct answer is {qd['O'][CA - 1]}\n")

            elif 'CA' in qd:
                uA = input("Enter True or False: ").lower()
                CA = str(qd['CA']).lower()
                if uA == CA:
                    self.As.append(True)
                    self.TS += 1
                    print("Correct!\n")
                else:
                    self.As.append(False)
                    print(f"Wrong! Correct answer is {qd['CA']}\n")

        self.show_results()

    def show_results(self):
        print("\nQuiz Results:")
        print(f"Player Name: {self.PN}")
        print(f"Registration Number: {self.RN}")
        print(f"Age: {self.AG}\n")

        for i, (qd, a) in enumerate(zip(self.Qs, self.As), 1):
            print(f"Q{i}: {qd['Q']}")
            if 'O' in qd:
                print(f"Your Answer: {qd['O'][a - 1]}")
                print(f"Correct Answer: {qd['O'][qd['CA'] - 1]}")
            elif 'CA' in qd:
                print(f"Your Answer: {a}")
                print(f"Correct Answer: {qd['CA']}")

            print()

        print(f"Total Score: {self.TS}/{len(self.Qs)}")
        print("Thanks for playing!")

if __name__ == "__main__":
    qz = QZ()

    qz.mcq("Who created the first computer program?", ["Ada Lovelace", "Alan Turing", "Charles Babbage", "John von Neumann"], 1)
    qz.mcq("What does CPU stand for?", ["Central Processing Unit", "Computer Personal Unit", "Central Processor Unit", "Central Process Unit"], 1)
    qz.mcq("In which year was Python first released?", ["1990", "2000", "1980", "2010"], 1)
    qz.mcq("What is the capital of France?", ["Paris", "Berlin", "Madrid", "Rome"], 1)
    qz.mcq("Which planet is known as the Red Planet?", ["Earth", "Mars", "Jupiter", "Venus"], 2)

    qz.tfq("The moon is made of green cheese.", False)
    qz.tfq("Python is a compiled language.", False)

    qz.conduct()
