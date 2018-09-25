import pandas as pd
import numpy as np
import math
from pandas import DataFrame, read_csv
from orm.models import Kelas,Siswa

sw=Siswa.objects.all()
kl=Kelas.objects.all()

def ListKelas(sw):
    if len(sw)>0:
        cols = ['Nilai']
        
        kel ={
            cols[0] : [int(a.kelass.nilai) for a in sw],
        }
        dfkel = pd.DataFrame(data=kel)
        return dfkel
    else:
        return[]

def Hasil_Kelas():
    kl=ListKelas(sw)
    b = 0
    tampung=[]
    for y in range(len(sw)):
        a=(math.pow(kl.Nilai[y],2))
        b = b+a
    for i in range(len(sw)):
        s = kl.Nilai[i]
        ad=s/(math.sqrt(b))
        tampung.append(ad)
    if len(sw)>0:
        cols = ['Jenjang']
        
        kel ={
            cols[0] : [str(a.kelass.jenjang) for a in sw],
        }
        dfkel = pd.DataFrame(data=kel)
    swa={'nama':[a.nama for a in sw]}
    dfswa= pd.DataFrame(data=swa)
    Kelas=pd.DataFrame(data=tampung,columns=['Nilai'])
    new = pd.concat([dfswa,dfkel, Kelas], axis=1)
    return new


def HasilKelas_Pembobotan():
    b=Hasil_Kelas()
    lst=list(b)
    y=0
    d=[]
    lst
    
    for i in range(len(b)):
        y =0.3*b.Nilai[i]
        d.append(y)
        pb=pd.DataFrame(d,columns=['Nilai'])
    if len(sw)>0:
        cols = ['Jenjang']
        
        kel ={
            cols[0] : [str(a.kelass.jenjang) for a in sw],
        }
        dfkel = pd.DataFrame(data=kel)
    swa={'nama':[a.nama for a in sw]}
    dfswa= pd.DataFrame(data=swa)
    new = pd.concat([dfswa,dfkel, pb], axis=1)
    return new
















