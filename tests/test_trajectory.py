import unittest
from tools.trajectory import step, is_prime, steps_to_one, affine_parity_class, audit


class Tests(unittest.TestCase):
    def test_shortened_trajectories(self):
        self.assertEqual([step(x) for x in (1, 2, 3, 5, 7)], [2, 1, 5, 8, 11])
        self.assertEqual([steps_to_one(x) for x in (2, 3, 5, 7, 9, 15)], [1, 5, 4, 11, 13, 12])

    def test_prime_classification(self):
        self.assertEqual([x for x in range(2, 21) if is_prime(x)], [2, 3, 5, 7, 11, 13, 17, 19])

    def test_affine_class(self):
        self.assertEqual(affine_parity_class(3, 4), (9, 5, 16, 2))
        self.assertEqual(affine_parity_class(1, 2), (3, 1, 4, 1))

    def test_finite_audit(self):
        result = audit(100, 5)
        self.assertEqual(result['primes'] + result['composites'], 99)
        self.assertEqual(result['claim_level'], 'finite_sanity_only')


if __name__ == '__main__':
    unittest.main()
