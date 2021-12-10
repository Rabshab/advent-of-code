import statistics
import math

with open('input') as i:
  crabs = [int(x) for x in i.read().split(',')]

def task1():
  median = round(statistics.median(crabs))
  fuel_used = sum([abs(median - x) for x in crabs])
  print(fuel_used)

def task2():
  mean = math.floor(statistics.mean(crabs))
  steps = [range(abs(mean - x)) for x in crabs]
  fuel_steps = [[x+1 for x in step] for step in steps]
  total_fuel = sum([sum(step) for step in fuel_steps])
  print(total_fuel)

task1()
task2()