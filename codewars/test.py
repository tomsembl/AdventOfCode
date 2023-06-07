import codewars_test as test
from solution import first_impossible

sample_test_cases = [
    ('2 stones', [
        ([(0,0), (0,3)],   2),
        ([(0,0), (0,2)],   6),
        ([(0,0), (1,0)],  11),
        ([(1,2), (3,3)],  13),
        ([(0,0), (2,2)],  17),
    ]),
    ('3 stones', [
        ([(0,4), (1,0), (4,4)],   2),
        ([(0,0), (0,1), (1,1)],  15),
        ([(2,0), (0,2), (2,2)],  19),
        ([(0,2), (3,0), (5,2)],  26),
    ]),
    ('4–6 stones', [
        ([(0,0), (2,1), (2,2), (3,3)],                25),
        ([(3,2), (3,0), (1,6), (0,7), (3,1)],         23),
        ([(8,2), (1,0), (2,5), (0,7), (3,6), (6,8)],  34),
    ]),
]

@test.describe('Sample tests')
def sample_tests():
    for name, test_cases in sample_test_cases:
        @test.it(name)
        def _():
            for stones, expected in test_cases:
                msg = f'first_impossible({stones})'
                test.assert_equals(first_impossible(stones), expected, msg)