import numpy as np

def dir_vec(A,B):
 return B-A
def norm_vec(A,B):
 return np,dot(omat,dir_vec(A,B))
def line_gen(A,B):
len=10
  x_AB=np.zeros(2,len)
  lam=np.linspace(0,1,len)
  for i in range(len):
  temp1=A+lam[i]*(B-A)
  x_AB[:,i]=temp1.T
 return x_AB
 def lin_dir_pt(m,A,k1,k2)
 len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(k1,k2,len)
  for i in range(len):
    temp1 = A + lam_1[i]*m
    x_AB[:,i]= temp1.T
 return x_AB
A=np.array([-2,-2])
B=np.array([1,3])
dvec=np.array([-1,1])
omat=np.array([0,1],[-1,0])
AB=np.vstack((A,B)).T

print (dir_vec(A,B))
print (norm_vec(A,B))