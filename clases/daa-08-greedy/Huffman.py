from Heap import *

def Huffman_compression(nodes):
    n = len(nodes)
    heap = Heap()
    for node in nodes:
        heap.push(node)
    for i in range(1, n):
        z = Node()
        z.left = heap.pop()
        z.right = heap.pop()
        z.freq = z.left.freq + z.right.freq
        heap.push(z)
    return heap.root[1]

def Huffman_transform(data):
    n = len(data)
    uniq_arr = dict()
    for number in data:
        if uniq_arr.get(number) == None:
            uniq_arr.update({number : Node(number, 1 / n)})
        else:
            a = uniq_arr[number]
            a.freq = ((a.freq * n) + 1) / n
    values = uniq_arr.values()
    arr = []
    for val in values:
        arr.append(val)
    return arr

def Huffman(array):
    """Toma un sets de datos y los comprime usando el algoritmo de Huffman

    *array*, es pasado a la funcion 'Huffman_transform' y este retorna un
    arreglo de nodos para ser comprimidos. Luego es enviado a 'Huffman_Compression'
    que retorna el arbol binario con los datos comprimidos."""
    array = Huffman_transform(array)
    return Huffman_compression(array)

def inorder(node):
    if node == None:
        return
    inorder(node.left)
    print(node.symbol, node.freq)
    inorder(node.right)

if __name__ == '__main__':
    from sys import argv
    filename = argv[1]

    A = [] # creates an empty array
    with open(filename, 'r') as f:
        for line in f:
            A.append(int(line))
    inorder(Huffman(A))
