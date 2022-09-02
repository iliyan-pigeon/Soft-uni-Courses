import math

series_name = input()
seasons_number = int(input())
episodes_number = int(input())
episode_duration = float(input())
advertisements_duration = episode_duration * 0.2
special_episode_bonus = 10
total_time_episode = advertisements_duration + episode_duration
one_season_duration = total_time_episode * episodes_number + 10
total_duration = math.floor(one_season_duration * seasons_number)
print(f"Total time needed to watch the {series_name} series is {total_duration} minutes.")