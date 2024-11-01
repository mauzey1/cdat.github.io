import cdms2, sys, vcs

x=vcs.init()

f=cdms2.open(vcs.prefix+"/sample_data/ta_ncep_87-6-88-4.nc")
s=f("ta",slice(0,1),longitude=slice(34,35),squeeze=1)-273.15
s=cdms2.MV2.masked_less(s,-45.)
b=x.createboxfill()
b.level_1=-40
b.level_2=33
x.plot(s,b)

fnm= "test_boxfill_lev1_lev2_ta_missing.png"

x.png(fnm)
