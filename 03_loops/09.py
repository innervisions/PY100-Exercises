## 09 - Finding Nemo
fish_list = ['Dory', 'Marlin', 'Gill', 'Nemo', 'Bruce']

# for fish in fish_list:
#     print(fish)
#     if fish == 'Nemo':
#         break

idx = 0
while idx < len(fish_list):
    print(fish_list[idx])
    if fish_list[idx] == 'Nemo':
        break
    idx += 1
