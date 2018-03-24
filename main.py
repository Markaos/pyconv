#!/usr/bin/python3
import sys;
from converter import convert;

# print(format("1000 m/s = {} km/h", str(convert(1000, "m/s", "km/h", "speed"))));
if len(sys.argv) < 5:
  print("Syntax: " + sys.argv[0] + " <number> <first-type> <second-type> <category>");
  quit();

argv = sys.argv;
i = float(argv[1]);
t0 = argv[2];
t1 = argv[3];
c = argv[4];
string = str(i) + " " + t0 + " = {:.2f} " + t1;
string = string.format(convert(i, t0, t1, c));
print(string);
