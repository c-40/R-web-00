def max1(a, b):
    return a if a > b else b



# Display dependency matrix
def printMatrix(m, e1, e2):
    print("Lamport Clock Assignments:")
    print("\t", end="")
    for j in range(e2):
        print(f"e2{j+1}", end="\t")
    for i in range(e1):
        print(f"\ne1{i+1}", end="\t")
        for j in range(e2):
            print(m[i][j], end="\t")

# Display event arrows
def printFlow(p1, p2, m, e1, e2):
    print("\n\nEvent timeline with message flow:")
    for i in range(e1):
        print(f"P1: e1{i+1}({p1[i]})", end="")
        for j in range(e2):
            if m[i][j] == 1:
                print(f" ───> e2{j+1}({p2[j]}) [P2]", end="")
        print()
    for j in range(e2):
        found = False
        for i in range(e1):
            if m[i][j] == -1:
                print(f"P2: e2{j+1}({p2[j]}) ───> e1{i+1}({p1[i]}) [P1]")
                found = True
        if not found:
            print(f"P2: e2{j+1}({p2[j]})")

# Main function
def lamportLogicalClock(e1, e2, m):
    # Initialize timestamps
    p1 = [i + 1 for i in range(e1)]
    p2 = [i + 1 for i in range(e2)]

    # Print dependency matrix
    printMatrix(m, e1, e2)

    # Apply Lamport rules
    for i in range(e1):
        for j in range(e2):
            if m[i][j] == 1:  # message from P1[i] to P2[j]
                p2[j] = max1(p2[j], p1[i] + 1)
                for k in range(j + 1, e2):
                    p2[k] = p2[k - 1] + 1
            elif m[i][j] == -1:  # message from P2[j] to P1[i]
                p1[i] = max1(p1[i], p2[j] + 1)
                for k in range(i + 1, e1):
                    p1[k] = p1[k - 1] + 1

    # Show timestamps and flow
    printFlow(p1, p2, m, e1, e2)

# Driver code
if __name__ == "__main__":
    e1 = 5  # Events in P1
    e2 = 3  # Events in P2
    m = [[0] * e2 for _ in range(e1)]

    # Define message dependencies
    m[1][2] = 1   # P1 e12 sends to P2 e23
    m[4][1] = -1  # P2 e22 sends to P1 e15

    lamportLogicalClock(e1, e2, m)
