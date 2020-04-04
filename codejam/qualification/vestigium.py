T = int(input());

for x in range(1,T+1):
    N = int(input());
    matrixLines = [];
    M = [];

    for i in range(N):
        matrixLines.append(input());
    for line in matrixLines:
        matrixRow = [];
        for matrixCell in line.split(' '):
            matrixRow.append(int(matrixCell));
        M.append(matrixRow);

    k = 0;
    for i in range(N):
        k += M[i][i];

    r = 0;
    for row in M:
        if len(row) != len(set(row)):
            r += 1;

    c = 0;
    for col in range(N):
        matrixCol = [];
        for row in M:
            matrixCol.append(row[col]);
        if len(matrixCol) != len(set(matrixCol)):
            c += 1;

    print('Case #%d: %d %d %d' % (x,k,r,c));
