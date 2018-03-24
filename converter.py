#!/usr/bin/python3
nm = 0.000001
mm = 1;
cm = 10;
dm = 100;
inch = 25.4;
ft = 304.8;
yd = 914.4;
m = 1000;
km = 1000000;
mile = 1609344;
lea = 4828032;
ms = 0.001;
s = 1;
minute = 60;
h = 3600;
l = 1000000000;
ml = l / 1000;
cl = l / 100;
dl = l / 10;
hl = l * 100;
pa = 1;
kpa = 1000;
mpa = 1000000;
n = 1;
kn = 1000;
mn = 1000000;
g = 1
mg = 0.001;
cg = 0.01;
kg = 1000;
t = 1000000;
kt = t * 1000;
mt = kt * 1000;

def convert(i0, t0, t1, cat):
  if t0 == t1:
    return i0;
  i0 = float(i0);
  if cat == "speed":
    return _convertspeed(i0, t0, t1);
  elif cat == "distance":
    return _convertdistance(i0, t0, t1);
  elif cat == "time":
    return _converttime(i0, t0, t1);
  elif cat == "volume":
    return _convertvolume(i0, t0, t1);
  elif cat == "area":
    return _convertarea(i0, t0, t1);
  elif cat == "pressure":
    return _convertpressure(i0, t0, t1);

def _convertspeed(i, t0, t1):
  t0 = t0.split('/');
  t0 = _getvalue(t0[0]) / _getvalue(t0[1]);
  t1 = t1.split('/');
  t1 = _getvalue(t1[0]) / _getvalue(t1[1]);
  return i * (t0 / t1);
  
def _convertdistance(i, t0, t1):
  t0 = _getvalue(t0);
  t1 = _getvalue(t1);
  return i * (t0 / t1);

def _converttime(i, t0, t1):
  t0 = _getvalue(t0);
  t1 = _getvalue(t1);
  return i * (t0 / t1);
  
def _convertvolume(i, t0, t1):
  t0 = _getvalue(t0);
  t1 = _getvalue(t1);
  return i * (t0 / t1);

def _convertarea(i, t0, t1):
  t0 = _getvalue(t0);
  t1 = _getvalue(t1);
  return i * (t0 / t1);

def _convertpressure(i, t0, t1):
  t0 = _getvalue(t0);
  t1 = _getvalue(t1);
  return i * (t0 / t1);

def _getvalue(flag):
  if flag == "nm":
    return nm;
  elif flag == "mm":
    return mm;
  elif flag == "cm":
    return cm;
  elif flag == "dm":
    return dm;
  elif flag == "m":
    return m;
  elif flag == "ft":
    return ft;
  elif flag == "km":
    return km;
  elif flag == "s":
    return s;
  elif flag == "h":
    return h;
  elif flag == "min":
    return minute;
  elif flag == "ms":
    return ms;
  elif flag == "miles":
    return mile;
  elif flag == "in":
    return inch;
  elif flag == "yd":
    return yd;
  elif flag == "lea":
    return lea;
  elif flag == "l":
    return l;
  elif flag == "ml":
    return ml;
  elif flag == "cl":
    return cl;
  elif flag == "dl":
    return dl;
  elif flag == "hl":
    return hl;
  elif flag == "Pa":
    return pa;
  elif flag == "kPa":
    return kpa;
  elif flag == "MPa":
    return mpa;
  elif flag == "N":
    return n;
  elif flag == "kN":
    return kn;
  elif flag == "MN":
    return mn;
  elif flag == "t":
    return t;
  elif flag == "kt":
    return kt;
  elif flag == "Mt":
    return mt;
  elif flag[-1:] == "3":
    return _getextravalue3(flag[:-1]);
  elif flag[-1:] == "2":
    return _getextravalue2(flag[:-1]);
    
def _getextravalue3(flag):
  x = _getvalue(flag);
  #if x == 1:
  #  return 1;
  #else:
  #  i = 1000;
  #  j = 0;
  #  y = _zerocount(x);
  #  while j < y:
  #    i = i * 1000;
  #    j += 1;
  #  return i;
  return x * x * x;
    
def _getextravalue2(flag):
  x = _getvalue(flag);
  #if x == 1:
  #  return 1;
  #else:
  #  i = 1000;
  #  j = 0;
  #  y = _zerocount(x);
  #  while j < y:
  #    i = i * 100;
  #    j += 1;
  #  return i;
  return x * x;
    
def _zerocount(i):
  i = str(i);
  l = len(i);
  j = 1;
  zc = 0;
  while True:
    if j == 1:
      if i[-1:] == "0":
        zc += 1;
      else:
        break;
    else:
      if i[-j:-(j-1)] == "0":
        zc += 1;
      else:
        break;
    j += 1;
  return zc;


