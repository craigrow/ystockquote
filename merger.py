f1 = open("d:\\git\\stockquote\\testMergeInput1.txt", 'r')
f2 = open("d:\\git\\stockquote\\testMergeInput2.txt", 'r')

tf = open("d:\\git\\stockquote\\testMergeOutput.txt", "w")

f1Input = list(f1)
print f1Input

f2Input = list(f2)
print f2Input

f1.close()
f2.close()
tf.close()