import numpy as np

msg1 = input('Введите 1 текст: ').lower()
msg2 = input('Введите 2 текст: ').lower()

words = list(set(msg1.split() + msg2.split()))

def get_vector(msg, vocabulary):
    vector = np.zeros(len(vocabulary))
    for word in msg.split():
        if word in vocabulary:
            vector[vocabulary.index(word)] += 1
    return vector
vector1 = get_vector(msg1, words)
vector2 = get_vector(msg2, words)

dot_product = np.dot(vector1, vector2)
norm_vector1 = np.linalg.norm(vector1)
norm_vector2 = np.linalg.norm(vector2)

if norm_vector1 == 0 or norm_vector2 == 0:
    simularity = 0
else:
    simularity = dot_product / (norm_vector1 * norm_vector2)
print('Вектор 1: ',vector1)
print('Вектор 2: ',vector2)
print(f'Идентичность: {simularity:.4f} (на {simularity*100:.1f}%)')
