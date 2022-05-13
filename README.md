# Elephant

While studying programming in highschool we were all assigned the task of creating an algorithm to generate unique combinations of the letters in the word `elephant`. At the time I didn't solve it in a way that left me satisfied and it has always stayed with me. 

## Binary counting
As a teenager I was trying to do the binary counting method. I came close but didn't solve it as I hadn't learned enough. This morning, while having a coffee, the solution came to me quite suddenly and clearly. The solution I thought of is in `elephant_counting.py`. 

```
% python3 -m unittest discover test
t
n
nt
a
at
an
ant
h
ht
hn
hnt
ha
hat
han
hant
p
pt
pn
pnt
pa
pat
pan
pant
ph
pht
phn
phnt
pha
phat
phan
phant
e
et
en
ent
ea
eat
ean
eant
eh
eht
ehn
ehnt
eha
ehat
ehan
ehant
ep
ept
epn
epnt
epa
epat
epan
epant
eph
epht
ephn
ephnt
epha
ephat
ephan
ephant
l
lt
ln
lnt
la
lat
lan
lant
lh
lht
lhn
lhnt
lha
lhat
lhan
lhant
lp
lpt
lpn
lpnt
lpa
lpat
lpan
lpant
lph
lpht
lphn
lphnt
lpha
lphat
lphan
lphant
le
let
len
lent
lea
leat
lean
leant
leh
leht
lehn
lehnt
leha
lehat
lehan
lehant
lep
lept
lepn
lepnt
lepa
lepat
lepan
lepant
leph
lepht
lephn
lephnt
lepha
lephat
lephan
lephant
e
et
en
ent
ea
eat
ean
eant
eh
eht
ehn
ehnt
eha
ehat
ehan
ehant
ep
ept
epn
epnt
epa
epat
epan
epant
eph
epht
ephn
ephnt
epha
ephat
ephan
ephant
ee
eet
een
eent
eea
eeat
eean
eeant
eeh
eeht
eehn
eehnt
eeha
eehat
eehan
eehant
eep
eept
eepn
eepnt
eepa
eepat
eepan
eepant
eeph
eepht
eephn
eephnt
eepha
eephat
eephan
eephant
el
elt
eln
elnt
ela
elat
elan
elant
elh
elht
elhn
elhnt
elha
elhat
elhan
elhant
elp
elpt
elpn
elpnt
elpa
elpat
elpan
elpant
elph
elpht
elphn
elphnt
elpha
elphat
elphan
elphant
ele
elet
elen
elent
elea
eleat
elean
eleant
eleh
eleht
elehn
elehnt
eleha
elehat
elehan
elehant
elep
elept
elepn
elepnt
elepa
elepat
elepan
elepant
eleph
elepht
elephn
elephnt
elepha
elephat
elephan
elephant
..
----------------------------------------------------------------------
Ran 2 tests in 0.005s

OK
```

## Split & Merge method
I think that there is also a way to do this–analagous to merge sort–where you split the list and then recursively join it back together. I started this version in `elephant.py` but haven't finished it. 