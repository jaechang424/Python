def m_pow(value, jekob):
    return value ** jekob


print(m_pow(2, 4))
# 파이썬 람다식
m_pow2 = lambda a, b: a ** b
print(m_pow2(3, 3))


def kg_to_pound(kg):
    return kg * 2.20462262


print(str(kg_to_pound(20)) + "pound")
