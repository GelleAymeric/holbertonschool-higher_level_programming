#!/usr/bin/python3

import requests
import csv


def fetch_and_print_posts():
    """Fetch posts from the API and print them."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print(f"Statut code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(f"{post['title']}")


def fetch_and_save_posts():
    """Fetch posts from the API and save them to a CSV file."""
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        data_posts = [
            {'id': post['id'], 'title': post['title'], 'body': post['body']}
            for post in posts
        ]

        with open("posts.csv", "w", newline='') as csv_file:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()

            for post in data_posts:
                writer.writerow(post)


fetch_and_print_posts()
fetch_and_save_posts()
