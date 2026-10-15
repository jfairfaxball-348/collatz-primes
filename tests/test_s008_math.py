"""S008 exact finite regression; universal Collatz / Terras CST remain OPEN."""
import unittest
from collections import Counter
from test_s007_math import OLD,ROWS,T,tr

CERT=OLD+ROWS

def cross(n,k):
 z=n;a=0
 for j in range(1,k+1):
  a+=z&1;z=T(z)
  if 3**a < 2**j:return j
 return None

def band(a):
 b=1;P=3**(a+1)
 while 2**(a+b+2)<=P:b+=1
 M=2**(b+2)
 return b,P,M,2**a*M-P,pow(P,-1,M)

def inverse(w):
 r=z=a=0
 for j,ch in enumerate(w):
  if bool(z&1)!=(ch=="O"):
   r+=2**j;z+=3**a
  if ch=="O":z=(3*z+1)//2;a+=1
  else:z//=2
 return r,z

class S008Math(unittest.TestCase):
 def test_dichotomy(self):
  good=[];bad=[]
  for r in range(11,8192,16):
   (good if any(r%2**j==x for x,j in CERT) else bad).append(r)
  self.assertEqual((len(good),len(bad)),(441,71))
  self.assertEqual(Counter(r%256 for r in bad),{27:26,91:15,155:15,251:15})
  self.assertEqual(Counter(tr(r,13)[2] for r in bad),{9:37,10:25,11:8,12:1})
  self.assertEqual(Counter(cross(r,13) for r in good),{5:256,7:64,8:64,10:24,12:14,13:19})
  for r in bad:
   self.assertIsNone(cross(r,13))
   for q in (0,1,17):
    n=r+8192*q
    self.assertTrue(all(tr(n,j)[0]>n for j in range(1,14)))
  for r in good:
   for q in (0,1,17):
    n=r+8192*q
    self.assertLess(tr(n,cross(n,13))[0],n)

 def test_two_run(self):
  near=[]
  for a in range(3,401):
   b,P,M,D,t0=band(a)
   self.assertGreaterEqual(D*t0,M-1)
   self.assertEqual((D*t0+1)%M,0)
   if D<M:near.append(a)
   if a<=150:
    for q in (0,1,5):
     t=t0+M*q;n=2**a*t-1;j=a+b+2
     z,w,_=tr(n,j)
     self.assertEqual((w,z),("O"*a+"EO"+"E"*b,(P*t-1)//M))
     self.assertEqual(n-z,(D*t-(M-1))//M)
     self.assertEqual(cross(n,j),j)
     self.assertLess(z,n)  # finite, NOT theorem for all a
  self.assertEqual(near,[4]) # checked only 3<=a<=400
  self.assertEqual(band(4),(2,243,16,13,11))
  self.assertEqual(tr(175,8),(167,"OOOOEOEE",5))

 def test_general_two_run_identity(self):
  for a in range(3,8):
   for c in range(1,5):
    for d in range(1,5):
     for b in range(1,7):
      w="O"*a+"E"*c+"O"*d+"E"*b
      M=2**(c+d+b);P=3**(a+d);K=3**d*(2**c-1)-2**(c+d)
      t=(-K*pow(P,-1,M))%M
      self.assertGreater(t,0)
      n=2**a*t-1;r,z=inverse(w)
      self.assertEqual(n%2**len(w),r)
      self.assertEqual(tr(n,len(w))[1],w)
      self.assertEqual(z,(P*t+K)//M)
      self.assertEqual(n-z,((2**a*M-P)*t-(M+K))//M)
      for q in (1,3):
       nxt=n+2**len(w)*q
       self.assertEqual(tr(nxt,len(w))[1],w)
       self.assertEqual(tr(nxt,len(w))[0],z+P*q)
  self.assertEqual(3*(2-1)-4,-1)
  self.assertEqual(3*(4-1)-8,1)
  self.assertEqual(9*(2-1)-8,1)

 def test_historical_adversaries_and_mod3(self):
  self.assertEqual((tr(7,7)[0],tr(7,8)[0]),(5,8))
  self.assertEqual(tr(27,59)[0],23)
  self.assertEqual(tr(91,45)[0],61)
  self.assertEqual((3*121+1)//4,91)
  self.assertEqual((3*15+1)//2,23)
  self.assertEqual((3*23+1)//2,35)
  self.assertEqual((3*681+1)//4,511)
  for y in range(1,100,2):
   ks=[k for k in range(1,20) if (2**k*y-1)%3==0]
   if y%3==0:self.assertEqual(ks,[])
   elif y%3==1 and y>1:
    self.assertTrue(all((2**k*y-1)//3>y for k in ks))
   elif y%3==2 and y>1:self.assertLess((2*y-1)//3,y)
