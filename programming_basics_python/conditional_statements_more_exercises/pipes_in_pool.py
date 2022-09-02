pool_volume_l = int(input())
flow_rate_one = int(input())
flow_rate_two = int(input())
worker_absence = float(input())
litres_more = 0
pool_fullness = 0
pipe_one_percent = 0
pipe_two_percent = 0
litres_flowed_one = flow_rate_one * worker_absence
litres_flowed_two = flow_rate_two * worker_absence
litres_flowed_combined = litres_flowed_one + litres_flowed_two
if pool_volume_l >= litres_flowed_combined:
    pool_fullness = litres_flowed_combined / pool_volume_l * 100
    pipe_one_percent = litres_flowed_one / litres_flowed_combined * 100
    pipe_two_percent = litres_flowed_two / litres_flowed_combined * 100
    print(f"The pool is {pool_fullness:.2f}% full. Pipe 1:\
{pipe_one_percent:.2f}%. Pipe 2: {pipe_two_percent:.2f}")
elif pool_volume_l < litres_flowed_combined:
    litres_more = abs(pool_volume_l - litres_flowed_combined)
    print(f"For {worker_absence:.2f}\
 hours the pool overflows with {litres_more:.2f} liters.")