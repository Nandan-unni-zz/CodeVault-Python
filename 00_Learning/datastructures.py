aString = "abcd"
aInt = 12
aFloat = 12.34
aComplex = 1j
aList = ["abcd", "efgh", "ijkl"]
aTuple = ("abcd", "efgh", "ijkl")
aSet = {"abcd", "efgh", "ijkl"}
aFrozenset = frozenset({"abcd", "efgh", "ijkl"})
aDict = {1: "abcd", 2: "efgh", 3: "ijkl"}
aBool = True
aBytes = b"abcd"
aByteArray = bytearray(5)
aMemoryView = memoryview(bytes(5))

ds = [aString, aInt, aFloat, aComplex, aList, aTuple, aSet,
      aFrozenset, aDict, aBool, aBytes, aByteArray, aMemoryView]

for d in ds:
    print(d, "-", type(d))
