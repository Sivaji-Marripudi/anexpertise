class Check:
    def _init_(self, l1,l2):
        self.l1 = l1
        self.l2 = l2
def is_check(poly,poi):
    P = []
    Q = []
    R = []  
    l = len(poly)
    for i in range(l):
        p1,p2 = poly[i],poly[(i + 1) % l]
        a,b,c = -(p2.l2 - p1.l2),p2.l1 - p1.l1,-(a*p1.l1 + b*p1.l2)
        P.append(a)
        Q.append(b)
        R.append(c)
    K = []
    l1 = len(A)
    for i in range(l1):
        d = P[i]*poi.l1 + Q[i]*poi.l2+R[i]
        K.append(d)
    t = all(k >= 0 for k in K)
    t1 = all(k <= 0 for k in K)
    return t or t1
poly = [Check(-3,2),Check(-2,-0.8),Check(0,1.2),Check(2.2,0),Check(2,4.5)]
s = Check(0,0)
print(is_check(poly,s))