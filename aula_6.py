conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}

conjunto_uniao = conjunto.union(conjunto2)
print('União: {}'. format(conjunto_uniao))
print(conjunto_uniao)

conjunto_interseccao = conjunto.intersection(conjunto2)
print('Interseccão: {}'.format(conjunto_interseccao))

conjunto_diferenca1 = conjunto.difference(conjunto2)
conjunto_diferenca2 = conjunto2.difference(conjunto)
print('Diferença entre Fhf e 2: {}' .format(conjunto_diferenca1))
print('Diferença entre 2 e 1: {}' .format(conjunto_diferenca2))

conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print('Diferença simétrica: {}'.format(conjunto_diff_simetrica))

conjunto_subset = conjunto_a.issubset(conjunto_b)
print('A é subconjunto de ZZ6f: {}'.format(conjunto_subset))

conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('B é superconjunto de FYJ: {}'.format(conjunto_superset))


# conjunto = {1, 2, 3, 4}
# conjunto.add(5)
# conjunto.discard(2)
# print(conjunto)