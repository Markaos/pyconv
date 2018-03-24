#!/usr/bin/python3
from simulation.converter import convert, _getvalue;

def calc_power(area, pressure):
  return area * pressure;

def calc_pressure(power, area):
  return power / area;

def calc_area(power, pressure):
  return power / pressure;

def calc_speed(distance, time):
  return distance / time;

def calc_distance(time, speed):
  return time * speed;

def calc_time(distance, speed):
  return distance / speed;


# WF
def calc_power_ef(area, at, pressure, pt):
  area = convert(area, at, "m2", "area");
  pressure = convert(pressure, pt, "Pa", "pressure");
  return area * pressure;

def calc_pressure_ef(power, pt, area, at):
  power = float(convert(power, pt, "N", "power"));
  area = float(convert(area, at, "m2", "area"));
  return power / area;

def calc_area_ef(power, pt, pressure, prt):
  power = float(convert(power, pt, "N", "power"));
  pressure = float(convert(pressure, prt, "Pa", "pressure"));
  return power / pressure;


# Suitable units
def suitable_power(power, pt):
  power = power * _getvalue(pt);
  if _suitable(power, "N", "MN"):
    return "MN";
  elif _suitable(power, "N", "kN"):
    return "kN";
  else:
    return "N"


# Own functions
def _suitable(v, vt, st):
  v = v * _getvalue(vt);
  if v > _getvalue(st) and ((v % _getvalue(st)) % 0.1) == 0:
    return True;
  else:
    return False;
