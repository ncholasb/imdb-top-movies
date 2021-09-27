# IMDb - Top Movies

Python script for extract top 250 rated movies from [IMDb](https://www.imdb.com/chart/top)

The script use **Pandas** and **BeautifulSoup** to ensure that extraction will goes correctly.

Were used too, to test the speed of extraction, the number of **Threads**. Setted in _"MAX_THREADS"_.

<br />

Other libs used: _requests, re, concurrent.futures, time_.

<br />

---

<br />

After run the script, will be an output _(csv file)_ named **out.csv**. Which separe the 250 extracted movies by lines and columns _(place, movie_title, year and rating)_.

![image](https://user-images.githubusercontent.com/57227204/134988461-9d51942c-0f83-42d2-b768-581f0c3ef132.png)
