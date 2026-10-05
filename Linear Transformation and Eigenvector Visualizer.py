import check
import math 
import matplotlib.pyplot as plt


class Vector:
    '''
    Fields: x (Float), y (Float)
    '''

    def __init__(self, x1, x2):
        '''
        Constructor: Creates a Vector object by calling
        Vector(x1, x2).

        Effects: Mutates self

        __init__: Vector Float Float -> None
        '''
        self.x = x1
        self.y = x2

    def __repr__(self):
        '''
        Returns a string representation of self.

        __repr__: Vector -> Str
        '''
        s = "Vector({0.x}, {0.y})"
        return s.format(self)
    
    def __eq__(self, other):
        '''
        Returns True if self and other are Vectors with the same
        x and y, and False otherwise.

        __eq__: Vector Any -> Bool
        '''
        return isinstance(other, Vector) and \
               self.x == other.x and \
               self.y == other.y
    
    
class Matrix:
    '''
    Fields: a (Float), b (Float), c (Float), d (Float)
    Represents the 2x2 matrix:
    | a  b |
    | c  d |
    '''

    def __init__(self, x1, x2, x3, x4):
        '''
        Constructor: Creates a Matrix object by calling
        Matrix(x1, x2, x3, x4).

        Effects: Mutates self

        __init__: Matrix Float Float Float Float -> None
        '''
        self.a = x1
        self.b = x2
        self.c = x3
        self.d = x4

    def __repr__(self):
        '''
        Returns a string representation of self.

        __repr__: Matrix -> Str
        '''
        s = "Matrix([[{0.a}, {0.b}], [{0.c}, {0.d}]])"
        return s.format(self)
    
    def __eq__(self, other):
        '''
        Returns True if self and other are Matrices with the same
        a, b, c, and d, and False otherwise.

        __eq__: Matrix Any -> Bool
        '''
        return isinstance(other, Matrix) and \
               self.a == other.a and \
               self.b == other.b and \
               self.c == other.c and \
               self.d == other.d
    

def transform(m, v):
    '''
    Returns a new Vector that is the result of multiplying
    Matrix m by Vector v.

    transform: Matrix Vector -> Vector

    Examples:
       If m = Matrix(2, 1, 1, 2) and v = Vector(1, 0),
       then transform(m, v) => Vector(2, 1)
    '''
    x1 = (m.a * v.x) + (m.b * v.y)
    x2 = (m.c * v.x) + (m.d * v.y)
    new_vector = Vector(x1, x2)
    return new_vector


def get_unit_square():
    '''
    Returns a list of 4 Vectors representing the corners of
    the unit square in order: (0,0), (1,0), (1,1), (0,1).

    get_unit_square: -> (listof Vector)

    Examples:
       get_unit_square()
          => [Vector(0,0), Vector(1,0), Vector(1,1), Vector(0,1)]
    '''
    return [Vector(0,0), Vector(1,0), Vector(1,1), Vector(0,1)]


def transform_square(m):
    '''
    Returns a list of 4 Vectors — the corners of the unit square
    after being transformed by Matrix m.

    transform_square: Matrix -> (listof Vector)

    Examples:
       If m = Matrix(2, 1, 1, 2), then
       transform_square(m)
          => [Vector(0,0), Vector(2,1), Vector(3,3), Vector(1,2)]
    '''
    return list(map (lambda x: transform(m, x), get_unit_square()))


def trace(m):
    '''
    Returns the trace of Matrix m, which is the sum of its
    diagonal elements.

    trace: Matrix -> Float

    Examples:
       If m = Matrix(2, 1, 1, 2),
       then trace(m) => 4.0
    '''
    return m.a + m.d


def det(m):
    '''
    Returns the determinant of Matrix m.

    det: Matrix -> Float

    Examples:
       If m = Matrix(2, 1, 1, 2),
       then det(m) => 3.0
    '''
    return m.a * m.d - m.b * m.c


def eigenvalues(m):
    '''
    Returns a list of the two eigenvalues of Matrix m, found by
    solving the characteristic polynomial
    lambda^2 - trace(m)*lambda + det(m) = 0.

    eigenvalues: Matrix -> (list Float Float)
    Requires: trace(m)^2 - 4*det(m) >= 0

    Examples:
       If m = Matrix(2, 1, 1, 2),
       then eigenvalues(m) => [3.0, 1.0]
    '''
    t = trace(m)
    d = det(m)
    b = math.sqrt(t ** 2 - 4 * d)
    return [(t + b) / 2, (t - b) / 2]


def eigenvectors(m):
    '''
    Returns a list of two Vectors — the eigenvectors of Matrix m
    found by computing the null space of (A - lambda*I) for each
    eigenvalue lambda.

    eigenvectors: Matrix -> (list Vector Vector)

    Examples:
       If m = Matrix(2, 1, 1, 2),
       then eigenvectors(m) => [Vector(1, 1.0), Vector(1, -1.0)]
    '''
    if m.b == 0 and m.c == 0:
        return [Vector(1, 0), Vector(0, 1)]
    else:
        return list(map(lambda lam: Vector(m.b, lam - m.a), eigenvalues(m)))
    

def visualize(m):
    '''
    Returns None.

    Effects: Displays a plot showing the original unit square,
             the transformed unit square, and the two eigenvector
             directions of Matrix m

    visualize: Matrix -> None

    Examples:
       visualize(Matrix(2, 1, 1, 2)) => None and displays the plot
    '''
    orig = get_unit_square()
    trans = transform_square(m)
    evecs = eigenvectors(m)
    evals = eigenvalues(m)
    ox = list(map(lambda v: v.x, orig)) + [orig[0].x]
    oy = list(map(lambda v: v.y, orig)) + [orig[0].y]
    tx = list(map(lambda v: v.x, trans)) + [trans[0].x]
    ty = list(map(lambda v: v.y, trans)) + [trans[0].y]
    plt.plot(ox, oy, "b-", label="Original unit square")
    plt.plot(tx, ty, "r-", label="After transformation")
    for i in range(len(evecs)):
        plt.annotate("v" + str(i + 1),
                     xy=(evecs[i].x, evecs[i].y),
                     xytext=(0, 0),
                     arrowprops=dict(arrowstyle="->"))
    plt.axhline(0, color="blue", linewidth=0.5)
    plt.axvline(0, color="blue", linewidth=0.5)
    plt.legend()
    plt.title("Example: A = [[" + str(m.a) + ", " + str(m.b) +
              "], [" + str(m.c) + ", " + str(m.d) + "]]")
    plt.grid(True)
    plt.show()


## Tests:
check.expect("T1: vector eq", Vector(2.0, 3.0) == Vector(2.0, 3.0), True)
check.expect("T2: matrix eq", Matrix(2,1,1,2) == Matrix(2,1,1,2), True)
check.expect("T3: transform", transform(Matrix(2,1,1,2), Vector(1,0)),
             Vector(2, 1))
check.expect("T4: unit square", get_unit_square(),
             [Vector(0,0), Vector(1,0), Vector(1,1), Vector(0,1)])
check.expect("T5: transform square", transform_square(Matrix(2,1,1,2)),
             [Vector(0,0), Vector(2,1), Vector(3,3), Vector(1,2)])
check.within("T6: eigenvalue 1", eigenvalues(Matrix(2,1,1,2))[0], 3.0, 0.001)
check.within("T7: eigenvalue 2", eigenvalues(Matrix(2,1,1,2))[1], 1.0, 0.001)
check.expect("T8: eigenvectors", eigenvectors(Matrix(2,1,1,2)),
             [Vector(1, 1.0), Vector(1, -1.0)])

visualize(Matrix(2, 1, 1, 2))