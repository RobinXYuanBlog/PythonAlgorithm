## Matrix chain multiplication ##
## MCM(A1A2.....An) = min(i)(A1,A2,...,Ai)(Ai+1,...An)


def mcm(chain):
    n = len(chain)

    aux = {(i, i): (0,) + chain[i] for i in range(n)}

    for i in range(1, n):
        # start point
        for j in range(1, n-i):
            best = float('inf')
            for k in range(j, j+i):
                lcost, lname, lrow, lcol = aux[j, k]
                rcost, rname, rrow, rcol = aux[j+1, k+1]
                cost = lcost + rcost + lrow * lcol * rcol
                var = '(%s%s)' % (lname, rname)
                print(lcost, lname, lrow, lcol)

mcm([('A', 10, 20), ('B', 20, 30), ('C', 30, 40)])
