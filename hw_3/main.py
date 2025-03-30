from matrix import generate_random_matrix
from collision import find_collisions_matrix
from full_matrix import generate_full_matrix
import numpy as np

def gen_artifacts_1():
    m_first = generate_random_matrix()
    m_second = generate_random_matrix()

    add_file = open("artifacts/3_1/matrix+.txt", "w")
    add_file.write(str(m_first + m_second))

    mul_file = open("artifacts/3_1/matrix*.txt", "w")
    mul_file.write(str(m_first * m_second))

    matmul_file = open("artifacts/3_1/matrix@.txt", "w")
    matmul_file.write(str(m_first @ m_second))


def gen_artifacts_2():
    m_first = generate_full_matrix()
    m_second = generate_full_matrix()

    add_file = open("artifacts/3_2/matrix+.txt", "w")
    add_file.write(str(m_first + m_second))

    sub_file = open("artifacts/3_2/matrix-.txt", "w")
    sub_file.write(str(m_first - m_second))

    mul_file = open("artifacts/3_2/matrix*.txt", "w")
    mul_file.write(str(m_first * m_second))

    matmul_file = open("artifacts/3_2/matrix@.txt", "w")
    matmul_file.write(str(m_first @ m_second))

    pow_file = open("artifacts/3_2/matrix**.txt", "w")
    pow_file.write(str(m_first ** np.random.randint(1, 10)))

    div_file = open("artifacts/3_2/matrix_div.txt", "w")
    div_file.write(str(m_first / m_second))


def gen_artifacts_3():
    a, b, c, d = find_collisions_matrix()

    for matrix, filename in [
        (a, "A.txt"),
        (b, "B.txt"),
        (c, "C.txt"),
        (d, "D.txt")
    ]:
        file = open(f"artifacts/3_3/{filename}", "w")
        file.write(str(matrix))

    ab = a @ b
    ab_file = open("artifacts/3_3/AB.txt", "w")
    ab_file.write(str(ab))

    cd = c @ d
    cd_file = open("artifacts/3_3/CD.txt", "w")
    cd_file.write(str(cd))

    hash_file = open("artifacts/3_3/hash.txt", "w")
    hash_file.write(f"AB hash: {ab.__hash__()}\n")
    hash_file.write(f"CD hash: {cd.__hash__()}\n")

def main():
    gen_artifacts_1()
    gen_artifacts_2()
    gen_artifacts_3()


if __name__ == "__main__":
    main()
