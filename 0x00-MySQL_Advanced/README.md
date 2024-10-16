0x00. MySQL advanced
Back-end
SQL
MySQL
 Weight: 1


Requirements:

    - All my files will be executed on Ubuntu 18.04 LTS using MySQL 5.7 (version 5.7.30)
    - All my SQL queries should have a comment just before (i.e. syntax above)
    - All my files should start by a comment describing the task
    - All SQL keywords should be in uppercase (SELECT, WHERE…)
    - The length of your files will be tested using wc


Sample comments for my SQL file:

    $ cat my_script.sql
    -- 3 first students in the Batch ID=3
    -- because Batch 3 is the best!
    SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
    $


How to import a SQL dump:

$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$


NB:  I added a bash script namely setup.sh, to setup MySQL in docker container for Ubuntu 22.04 LTS