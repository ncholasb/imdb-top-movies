from bs4 import BeautifulSoup
import requests, re, concurrent.futures, time
import pandas as pd

MAX_THREADS = 10


def main():

    start_time = time.time()

    url = "http://www.imdb.com/chart/top"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    movies = soup.select("td.titleColumn")
    ratings = [
        b.attrs.get("data-value") for b in soup.select("td.posterColumn span[name=ir]")
    ]

    movie_details(movies, ratings)

    end_time = time.time()
    print(f"Total time taken: {end_time - start_time}. With {MAX_THREADS} threads.")


list = []


def movie_details(movies, ratings):
    for index in range(0, len(movies)):
        movie_string = movies[index].get_text()
        movie = " ".join(movie_string.split()).replace(".", "")
        movie_title = movie[len(str(index)) + 1 : -7]
        year = re.search("\((.*?)\)", movie_string).group(1)
        place = movie[: len(str(index)) - (len(movie))]
        data = {
            "place": place,
            "movie_title": movie_title,
            "year": year,
            "rating": ratings[index],
        }

        threads = min(MAX_THREADS, len(movies))
        with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
            list.append(data)
            pd.DataFrame(list).to_csv("out.csv", index=False)


if __name__ == "__main__":
    main()
