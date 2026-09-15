### Lab 1

> mkdir my_dir
> cd my_dir
> touch my_file.txt
> chmod 777 my_file.txt
> cat my_file.txt
> cd ..
> mkdir another_dir
> cp my_dir/my_file.txt another_dir/
> rm my_dir/my_file.txt
> cd another_dir
> ls

my_file.txt

### Task: Create two directories and move all files instead of copying from one directory to another

> ls
> another_dir filename.json my_dir
> ls my_dir
> my_file.txt
> tar -czv my_dir
> a my_dir
> a my_dir/my_file.txt
> ??j?A
> 1
> E{??@?2i?#??jafS??????BAf2}?? ?????fIQ??iW??+??eK?? 1?ESUΧ?1GѤ??C<????>?Ǽ??????0???|?M???o?ҿ#??
> 91??G?d??7???m?% > ls
> another_dir filename.json my_dir
> ls -la
> total 56
> drwxr-xr-x 5 ataidzhirgalbaev staff 160 Sep 15 13:20 .
> drwxr-xr-x 4 ataidzhirgalbaev staff 128 Sep 15 13:15 ..
> drwxr-xr-x 2 ataidzhirgalbaev staff 64 Sep 15 13:21 another_dir
> -rw-r--r-- 1 ataidzhirgalbaev staff 27520 Sep 15 13:15 filename.json
> drwxr-xr-x 3 ataidzhirgalbaev staff 96 Sep 15 13:21 my_dir
> ls my_dir
> my_file.txt
> tar -czvf archive.tar.gz my_dir
> a my_dir
> a my_dir/my_file.txt
> ls
> another_dir archive.tar.gz filename.json my_dir
> touch output.txt
> mv output.txt output.md

### Curls

> curl https://jsonplaceholder.typicode.com/posts

[
{
"userId": 1,
"id": 1,
"title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
"body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
},
{
"userId": 1,
"id": 2,
"title": "qui est esse",
"body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
}

....

> curl -o filename.json https://jsonplaceholder.typicode.com/posts
> % Total % Received % Xferd Average Speed Time Time Time Current

                                 Dload  Upload   Total   Spent    Left  Speed

100 27520 0 27520 0 0 616k 0 --:--:-- --:--:-- --:--:-- 625k

> curl -I https://jsonplaceholder.typicode.com/posts

HTTP/2 200
date: Tue, 15 Sep 2026 07:15:40 GMT
content-type: application/json; charset=utf-8
access-control-allow-credentials: true
....

> curl -X POST -H "Content-Type: application/json" \
> -d '{"title": "foo", "body": "bar", "userId": 1}' \
> https://jsonplaceholder.typicode.com/posts

{
"title": "foo",
"body": "bar",
"userId": 1,
"id": 101
}
