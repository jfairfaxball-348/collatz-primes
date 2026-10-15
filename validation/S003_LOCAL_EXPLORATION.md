# S003 exploratory finite log (local Python 3, not a repository checkout)

Prerecorded discovery n=2..100000 and independent holdout n=100001..1000000; shortened T step limit 1000; both showed 0 CST mismatches and 0 capped starts. This scan was exact integer arithmetic but finite and NOT a mathematical validation of CST.

Independent enumeration for k=10..16 over odd positive r>1: OPEN counts 64,128,226,367,734,1295,2114; OPEN+earlier slope crossing counts all 0. Replay of 27 produced first numerical/coefficient crossing j=59, T^59=23, odd count37, offset b=1100931843921811423, D=126176846412426125. Direct U-offset/gcd recurrence checked for m=1..6 on n=[15,35,121,27,3,51,243,231]. All checked assertions passed locally. Original repo clone not accessible because container github DNS unavailable. Hosted CI separately runs actual repository code, tests and canonical validation.
