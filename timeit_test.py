from timeit import timeit

problem = '[15]3Sum.py'
s = fr"""
path = r'C:\Users\ditho\Projects\LeetCode\leetcode\editor\en\{problem}'
import importlib.util
spec = importlib.util.spec_from_file_location("Solution", path)
foo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(foo)
"""

num = 30
sol_in = [0,0,0]
t = timeit(f"s = foo.Solution.threeSum(None, {sol_in})", setup=s, number=num)
print(t/num)

