#!/usr/bin/env python3
import sqlite3
import functools

query_cache = {}

# Decorator for connection handling
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect("users.db")
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper


# Cache decorator
def cache_query(func):
    @functools.wraps(func)
    def wrapper(conn, query, *args, **kwargs):
        if query in query_cache:
            print("Using cached result for query.")
            return query_cache[query]
        result = func(conn, query, *args, **kwargs)
        query_cache[query] = result
        print("Caching result for query.")
        return result
    return wrapper


@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


if __name__ == "__main__":
    # First call -> caches
    users = fetch_users_with_cache(query="SELECT * FROM users")
    print(users)

    # Second call -> cached
    users_again = fetch_users_with_cache(query="SELECT * FROM users")
    print(users_again)
