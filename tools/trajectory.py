#!/usr/bin/env python3
"""Exact finite Collatz and parity-residue experiments. NOT a universal proof."""
import argparse
import json


def step(n: int) -> int:
    if n < 1:
        raise ValueError('positive integers only')
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def steps_to_one(n: int, cap: int = 100000) -> int:
    if n < 1:
        raise ValueError('positive integers only')
    k = 0
    while n != 1 and k < cap:
        n = step(n)
        k += 1
    if n != 1:
        raise RuntimeError('cap exceeded; do not infer divergence')
    return k


def affine_parity_class(r: int, k: int):
    """T^k(n)=(a*n+b)/2^k for n=r (mod 2^k), n>0."""
    if k < 1 or r < 1 or r >= 2 ** k:
        raise ValueError('require k>=1 and 1<=r<2^k')
    a, b, d = 1, 0, 1
    x = r
    for _ in range(k):
        odd = x % 2
        if odd:
            a, b = 3 * a, 3 * b + d
        d *= 2
        x = step(x)
    assert a * r + b == d * x
    return a, b, d, x


def audit(limit: int, depth: int) -> dict:
    if limit < 2 or depth < 1:
        raise ValueError('limit>=2 and depth>=1 required')
    primes = composites = 0
    prime_max = (-1, -1)
    composite_max = (-1, -1)
    for n in range(2, limit + 1):
        s = steps_to_one(n)
        if is_prime(n):
            primes += 1
            if s > prime_max[0]:
                prime_max = (s, n)
        else:
            composites += 1
            if s > composite_max[0]:
                composite_max = (s, n)
    assertions = 0
    for k in range(1, depth + 1):
        d = 1 << k
        for r in range(1, d, 2):
            a, b, den, x = affine_parity_class(r, k)
            for q in range(9):
                n = r + q * d
                y = n
                for _ in range(k):
                    y = step(y)
                assert den * y == a * n + b
                assert y == x + a * q
                assertions += 2
    for q in range(100):
        n = 3 + 16 * q
        x = n
        for _ in range(4):
            x = step(x)
        assert x == (9 * n + 5) // 16
        assert x < n
        assertions += 2
    return {
        'map': 'shortened',
        'range_inclusive': [2, limit],
        'primes': primes,
        'composites': composites,
        'max_prime_steps_and_start': list(prime_max),
        'max_composite_steps_and_start': list(composite_max),
        'parity_depth': depth,
        'finite_assertions': assertions,
        'claim_level': 'finite_sanity_only',
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--limit', type=int, default=10000)
    parser.add_argument('--depth', type=int, default=8)
    args = parser.parse_args()
    print(json.dumps(audit(args.limit, args.depth), indent=2, sort_keys=True))
