# def is_multiple_of_five(n):
#     return not n % 5
#
#
# def get_multiples_of_five(n):
#     return list(filter(is_multiple_of_five, range(n)))
#
# def get_multiples_of_fivex(n):
#     return list(filter(lambda k: not k % 5, range(n)))
# print(get_multiples_of_five(45))
# print(map(lambda *a: a, range(3)))
# _ = list                # create an "alias" to list
# # 1 iterable
# print(_(map(lambda *a: a, range(3))))                       # 1 iterable
# print(_(map(lambda *a: a, range(3), 'abc')))                # 2 iterables
# print(_(map(lambda *a: a, range(3), 'abc', range(4, 7))))   # 3
# # map stops at the shortest iterator
# print(_(map(lambda *a: a, (), 'abc')))                      # empty tuple is shortest
# print(_(map(lambda *a: a, (1, 2), 'abc')))                  # (1, 2) shortest
# print(_(map(lambda *a: a, (1, 2, 3, 4), 'abc')))
_ = list    
students = [
    dict(id=0, credits=dict(math=9, physics=6, history=7)),
    dict(id=1, credits=dict(math=6, physics=7, latin=10)),
    dict(id=2, credits=dict(history=8, physics=9, chemistry=10)),
    dict(id=3, credits=dict(math=5, physics=5, geography=7)),
]


def decorate(student):
    # create a 2-tuple (sum of credits, student) from student dict
    return (sum(student['credits'].values()), student['credits'])


def undecorate(decorated_student):
    # discard sum of credits, return original student dict
    return decorated_student[1]


print(sum(students[0]['credits'].values()))
print(decorate(students[0]))
students = sorted(map(decorate, students), reverse=True)
print(students)


students = _(map(undecorate, students))
print(students)