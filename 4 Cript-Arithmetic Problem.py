class Main:
    use = [0] * 10

    class Node:
        def __init__(self):
            self.letter = ''
            self.value = 0

    def isValid(self, nodeList, count, s1, s2, s3):
        val1, val2, val3 = 0, 0, 0
        m = 1
        for i in range(len(s1) - 1, -1, -1):
            ch = s1[i]
            for j in range(count):
                if nodeList[j].letter == ch:
                    break
            val1 += m * nodeList[j].value
            m *= 10
        m = 1
        for i in range(len(s2) - 1, -1, -1):
            ch = s2[i]
            for j in range(count):
                if nodeList[j].letter == ch:
                    break
            val2 += m * nodeList[j].value
            m *= 10
        m = 1
        for i in range(len(s3) - 1, -1, -1):
            ch = s3[i]
            for j in range(count):
                if nodeList[j].letter == ch:
                    break
            val3 += m * nodeList[j].value
            m *= 10
        return 1 if val3 == (val1 + val2) else 0

    def permutation(self, count, nodeList, n, s1, s2, s3):
        if n == count:
            if self.isValid(nodeList, count, s1, s2, s3) == 1:
                print("Solution found:", end='')
                for j in range(count):
                    print(f" {nodeList[j].letter} = {nodeList[j].value}", end='')
                return 1
            return 0
        for i in range(10):
            if self.use[i] == 0:
                nodeList[n].value = i
                self.use[i] = 1
                if self.permutation(count, nodeList, n + 1, s1, s2, s3) == 1:
                    return 1
                self.use[i] = 0
        return 0

    def solvePuzzle(self, s1, s2, s3):
        uniqueChar = 0
        freq = [0] * 26
        for ch in s1 + s2 + s3:
            freq[ord(ch) - ord('A')] += 1
        for i in range(26):
            if freq[i] > 0:
                uniqueChar += 1
        if uniqueChar > 10:
            print("Invalid strings")
            return 0
        nodeList = [self.Node() for _ in range(uniqueChar)]
        j = 0
        for i in range(26):
            if freq[i] > 0:
                nodeList[j].letter = chr(i + ord('A'))
                j += 1
        return self.permutation(uniqueChar, nodeList, 0, s1, s2, s3)


if __name__ == "__main__":
    main = Main()
    s1 = input("Enter first string: ").upper()
    s2 = input("Enter second string: ").upper()
    s3 = input("Enter result string: ").upper()
    if main.solvePuzzle(s1, s2, s3) == 0:
        print("No solution")
