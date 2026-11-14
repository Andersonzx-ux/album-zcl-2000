import sys, numpy as np, colorsys
from PIL import Image
base=sys.argv[1]
im=np.asarray(Image.open(f'{base}/assets/cover.jpg').convert('RGB')).astype(float)
H,W,_=im.shape
L=0.2126*im[...,0]+0.7152*im[...,1]+0.0722*im[...,2]
hx=lambda c:'#%02X%02X%02X'%tuple(int(round(v)) for v in c)
med=lambda a:np.median(a.reshape(-1,3),axis=0)
# letras do nome: escuras e azuis/vermelhas, na faixa y 290-340
y0,y1=290,340
sub=im[y0:y1]; r,g,b=sub[...,0],sub[...,1],sub[...,2]
navy=(b>r+25)&(b>g+15)&(L[y0:y1]<130)
red=(r>g+70)&(r>b+50)&(L[y0:y1]<190)
for n,m in [('navy',navy),('red',red)]:
    ys,xs=np.nonzero(m); print(n,'px',m.sum(),'bbox x',xs.min(),xs.max(),'y',ys.min()+y0,ys.max()+y0,'median',hx(np.median(sub[m],axis=0)),'darkest10%',hx(np.mean(sub[m][L[y0:y1][m]<=np.percentile(L[y0:y1][m],10)],axis=0)))
any_=navy|red; ys,xs=np.nonzero(any_); print('texto bbox x',xs.min(),xs.max(),'y',ys.min()+y0,ys.max()+y0)
reg={'foliage_top':(0,120,120,420),'foliage_mid':(180,300,300,400),'yellow_sweater':(380,470,20,200),'yellow_sweater_hi':(230,290,60,150),'mint_sweater':(240,300,440,600),'mint_sweater_low':(430,500,430,520),
 'denim_left':(560,630,20,250),'denim_right':(560,630,490,630),'skin_zeze':(150,200,130,190),'skin_luc':(140,190,440,520),'hair_zeze':(15,60,110,220),'hair_luc':(20,50,430,540),'shadow_jeans':(520,560,300,380),'corner_tl':(0,60,0,60),'top_bright':(0,40,200,420)}
for k,(a,b2,c,d) in reg.items(): print(k,hx(med(im[a:b2,c:d])))
# percentis de luminância global
f=im.reshape(-1,3);Lf=L.reshape(-1)
for lo,hi in [(0,5),(5,25),(25,50),(50,75),(75,95),(95,100)]:
    a,b2=np.percentile(Lf,[lo,hi]); m=(Lf>=a)&(Lf<=b2); print('lum',lo,hi,hx(np.median(f[m],axis=0)))
# saturados dominantes por matiz
hsv=np.array([colorsys.rgb_to_hsv(*(p/255)) for p in f[::37]])
import collections
c=collections.Counter(np.floor(hsv[:,0]*12).astype(int)); print('hue12',sorted(c.items()))
