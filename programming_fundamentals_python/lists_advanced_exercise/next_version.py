version_list = [int(number) for number in input().split(".")]
version_list[2] += 1
if version_list[2] > 9:
    version_list[2] = 0
    version_list[1] += 1
    if version_list[1] > 9:
        version_list[1] = 0
        version_list[0] += 1
final_list = list(map(str, version_list))
latest_version = ".".join(final_list)
print(latest_version)
