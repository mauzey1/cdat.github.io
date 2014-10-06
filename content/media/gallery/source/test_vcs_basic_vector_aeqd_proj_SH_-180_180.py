
import sys,os
import vcs
import sys
import cdms2
import vtk
import os
import MV2
bg = not False
x=vcs.init()
x.setbgoutputdimensions(1200,1091,units="pixels")
x.setcolormap("rainbow")
gm = vcs.createvector()

p = vcs.createprojection()
ptype = 'aeqd'
p.type = ptype
gm.projection = p

xtra = {}
xtra["latitude"] = (-90.0,0.0)

xtra["longitude"] = (-180.0,180.0)

f=cdms2.open(os.path.join(sys.prefix,'sample_data','clt.nc'))
u=f("u",**xtra)
v=f("v",**xtra)
x.plot(u,v,gm,bg=bg)



x.png('test_vcs_basic_vector_aeqd_proj_SH_-180_180.png')