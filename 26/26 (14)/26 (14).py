import datetime

secs = int(datetime.timedelta(days=7).total_seconds())
f = lambda x: x.split()
processes = list(map(f, open("26 (14).txt", "r").read().splitlines()[1:]))
f = lambda x: [int(x[0]), int(x[1])]
processes = list(map(f, processes))
start_time = 1633305600
end_time = start_time + secs
counter = 0
time_process = list(range(1, secs+1))

for i in processes:
    if (i[0] < start_time) and ((i[1] > start_time) or (i[1] == 0)):
        counter +=1
    if (i[0] >= start_time) and (i[0] <= end_time):
        time_process[i[0] - start_time] = time_process[i[0] - start_time] + 1
    if (i[1] >= start_time) and (i[1] <= end_time):
        time_process[i[1] - start_time] = time_process[i[1] - start_time] - 1

sum_time = 0
max_process = 0
for i in range(1, secs):
    counter += time_process[i]
    if counter > max_process:
        max_process = counter
        sum_time = 0
    if counter == max_process:
         sum_time += 1

print(max_process, sum_time)
