> sudo nano /usr/local/bin/system_info

Password:

> sudo chmod +x /usr/local/bin/system_info

> system_info
> Hostname: Atais-MacBook-Air-2.local
> Current User: ataidzhirgalbaev
> Disk Space: Filesystem Size Used Avail Capacity iused ifree %iused Mounted on
> /dev/disk3s1s1 460Gi 12Gi 62Gi 16% 459k 654M 0% /
> devfs 223Ki 223Ki 0Bi 100% 773 0 100% /dev
> /dev/disk3s6 460Gi 3.0Gi 62Gi 5% 3 654M 0% /System/Volumes/VM
> /dev/disk3s2 460Gi 8.4Gi 62Gi 12% 1.5k 654M 0% /System/Volumes/Preboot
> /dev/disk3s4 460Gi 3.8Mi 62Gi 1% 65 654M 0% /System/Volumes/Update
> /dev/disk1s2 500Mi 6.0Mi 482Mi 2% 1 4.9M 0% /System/Volumes/xarts
> /dev/disk1s1 500Mi 5.8Mi 482Mi 2% 31 4.9M 0% /System/Volumes/iSCPreboot
> /dev/disk1s3 500Mi 1.4Mi 482Mi 1% 67 4.9M 0% /System/Volumes/Hardware
> /dev/disk3s5 460Gi 373Gi 62Gi 86% 3.2M 654M 0% /System/Volumes/Data
> map auto_home 0Bi 0Bi 0Bi 100% 0 0 - /System/Volumes/Data/home
> /dev/disk5s1 4.3Gi 4.2Gi 149Mi 97% 13 1.5M 0% /Library/Developer/CoreSimulator/Cryptex/Images/bundle/SimRuntimeBundle-1CB825DE-3CBD-45CF-ABF3-FCEBE851ACF7
> /dev/disk7s1 10Gi 9.8Gi 292Mi 98% 265k 3.0M 8% /Library/Developer/CoreSimulator/Volumes/watchOS_22R349
> /dev/disk9s1 8.0Gi 7.8Gi 239Mi 98% 13 2.4M 0% /Library/Developer/CoreSimulator/Cryptex/Images/bundle/SimRuntimeBundle-3188AF09-C5A6-49DB-A012-48683FD971C5
> /dev/disk11s1 18Gi 17Gi 461Mi 98% 444k 4.7M 9% /Library/Developer/CoreSimulator/Volumes/iOS_22A3351
> /dev/disk12s1 247Mi 245Mi 2.4Mi 100% 2.3k 4.3G 0% /Volumes/ProtonVPN
> sudo chmod +x /usr/local/bin/greeting

chmod: /usr/local/bin/greeting: No such file or directory

> sudo nano /usr/local/bin/greeting

> sudo chmod +x /usr/local/bin/greeting

> greeting
> Hello, Atai!
> date --help
> date: illegal option -- -
> usage: date [-jnRu] [-I[date|hours|minutes|seconds|ns]] [-f input_fmt]

            [ -z output_zone ] [-r filename|seconds] [-v[+|-]val[y|m|w|d|H|M|S]]
            [[[[mm]dd]HH]MM[[cc]yy][.SS] | new_date] [+output_fmt]

> sudo nano /usr/local/bin/current_time

> sudo chmod +x /usr/local/bin/current_time

> current_time
> Current time: 13:38.
> Work day ends after 4 hours and 22 minutes.
> sudo nano /usr/local/bin/count_word

> ls
> sudo chmod +x /usr/local/bin/count_word

> count_word ../lab1/filename.json lorem
> /usr/local/bin/count_word: line 1: !#/bin/bash: No such file or directory
> The word 'lorem' appears 0 times in ../lab1/filename.json.
> count_word ../lab1/filename.json minus
> /usr/local/bin/count_word: line 1: !#/bin/bash: No such file or directory
> The word 'minus' appears 8 times in ../lab1/filename.json.

> sudo nano /usr/local/bin/delete_empty_files

> touch empty.txt
> sudo chmod +x /usr/local/bin/delete_empty_files

> delete_empty_files .
> ./empty.txt
> ls
> output.md
