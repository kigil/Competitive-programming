import numpy as np

n, c = list(map(int, input().split(' ')))
x, v = [], []

for i in range(n):
  x_, v_ = list(map(int, input().split(' ')))
  x.append(x_)
  v.append(v_)
x = np.array(x)
v = np.array(v)
sum_v = np.cumsum(v)
inv_x = c - x[::-1]
inv_v = v[::-1]
sum_inv_v = np.cumsum(inv_v)

cal = sum_v - x
inv_cal = sum_inv_v - inv_x

cal_cummax = np.maximum.accumulate(cal)
inv_cal_cummax = np.maximum.accumulate(inv_cal)

fr_double_cal = sum_v - 2 * x + \
    np.insert(inv_cal_cummax[:-1], 0, 0)[::-1]
fl_double_cal = sum_inv_v - 2 * inv_x + \
    np.insert(cal_cummax[:-1], 0, 0)[::-1]

print(np.max(
    [0, cal.max(), inv_cal.max(), fr_double_cal.max(), fl_double_cal.max()]))
