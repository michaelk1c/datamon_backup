# datamon_backup
A script to rsync the contents of the datamon repos to the destination gcs bucket

## Steps:
1. fill in this google sheet with the list of datamon repos you'd want to backup
https://docs.google.com/spreadsheets/d/1cSySAbfm618mqP_U4iIf96xp1Zq-27Zg_e_bDjqTufU/edit#gid=0

2. mount the destination gcs bucket with gcsfuse
```
gcsfuse --implicit-dirs ctf-datamon-backup ~/mnt/bucket
```

3. run this script
```
poetry shell
python .
```

4. unmount gcsfuse
```
umount ~/mnt/bucket
```

## tools to install before running this script
- datamon2
- gcsfuse

## Execution
When you run it, it should look like this:
```
(datamon-backup-py3.8) ➜  datamon_backup (master) ✗ ./run.sh
+ gcsfuse --implicit-dirs ctf-datamon-backup /Users/mkang/mnt/bucket
2023/01/23 12:50:56.402897 Start gcsfuse/unknown (Go version go1.17.5) for app "" using mount point: /Users/mkang/mnt/bucket
2023/01/23 12:50:56.419819 Opening GCS connection...
2023/01/23 12:50:57.094061 Mounting file system "ctf-datamon-backup"...
2023/01/23 12:50:57.110959 File system has been successfully mounted.
+ python .
<<< run backup >>>
##########
datamon2 bundle mount --repo airport-JP --context dev --bundle 27zpshJwQDvUvDkqDvE1u4Vr64v --mount ~/mnt/datamon --daemonize
rsync -avr ~/mnt/datamon/ ~/mnt/bucket/airport-JP/27zpshJwQDvUvDkqDvE1u4Vr64v/
sending incremental file list
./

sent 98 bytes  received 22 bytes  240.00 bytes/sec
total size is 7,538  speedup is 62.82
umount ~/mnt/datamon
##########
datamon2 bundle mount --repo airport-exposure-us --context dev --bundle 1qRuzo3V3zthIq9sMGuO6szFlTu --mount ~/mnt/datamon --daemonize
rsync -avr ~/mnt/datamon/ ~/mnt/bucket/airport-exposure-us/1qRuzo3V3zthIq9sMGuO6szFlTu/
sending incremental file list
./

sent 88 bytes  received 22 bytes  220.00 bytes/sec
total size is 14,476  speedup is 131.60
umount ~/mnt/datamon
##########
datamon2 bundle mount --repo bridge-JP --context dev --bundle 25lyTKWXQKVyfNGb1w0ZY6lNLQv --mount ~/mnt/datamon --daemonize
rsync -avr ~/mnt/datamon/ ~/mnt/bucket/bridge-JP/25lyTKWXQKVyfNGb1w0ZY6lNLQv/
sending incremental file list
./

sent 89 bytes  received 22 bytes  222.00 bytes/sec
total size is 5,903,299  speedup is 53,182.87
umount ~/mnt/datamon
+ umount /Users/mkang/mnt/bucket
```
