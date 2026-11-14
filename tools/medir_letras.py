import sys, numpy as np
from PIL import Image
from scipy import ndimage as ndi
base=sys.argv[1]
im=np.asarray(Image.open(f'{base}/assets/cover.jpg').convert('RGB')).astype(float)
L=0.2126*im[...,0]+0.7152*im[...,1]+0.0722*im[...,2]
hx=lambda c:'#%02X%02X%02X'%tuple(int(round(v)) for v in c)
y0,y1,x0,x1=296,334,56,584
sub=im[y0:y1,x0:x1]; l=L[y0:y1,x0:x1]; r,g,b=sub[...,0],sub[...,1],sub[...,2]
navy=(b>r+25)&(b>g+10)&(l<140); red=(r>g+70)&(r>b+50)&(l<200)
for n,m in [('navy',navy),('red',red)]:
    core=ndi.binary_erosion(m,iterations=1); 
    lab,k=ndi.label(m); 
    objs=ndi.find_objects(lab); boxes=[objs[i-1] for i in range(1,k+1) if (lab==i).sum()>25]
    print(n,'componentes',len(boxes),'core px',core.sum(),'core median',hx(np.median(sub[core],axis=0)),'core mean',hx(sub[core].mean(axis=0)))
    if n=='red': print([ (b_[1].start+x0,b_[1].stop+x0,b_[0].start+y0,b_[0].stop+y0) for b_ in boxes])
both=navy|red; ys,xs=np.nonzero(both); print('bbox',xs.min()+x0,xs.max()+x0,ys.min()+y0,ys.max()+y0)
