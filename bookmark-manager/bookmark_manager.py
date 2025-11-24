import sqlite3


class Bookmark:
    def __init__(self, id: int, user: str, video_id: str, timestamp: int, title: str):
        self.id = id
        self.user = user
        self.video_id = video_id
        self.timestamp = timestamp
        self.title = title


class BookmarkManager:
    def __init__(self, db_path: Path, user: str):
        self.path = db_path
        self.user = user
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def create_bookmarks_db(self):
        # create bookmarks table
        self.cursor.execute("CREATE TABLE IF NOT EXISTS bookmarks "
                            "(id INTEGER PRIMARY KEY, "
                            "user_id TEXT, "
                            "video_id TEXT,"
                            "bookmark_time INTEGER, "
                            "title TEXT)")
        # create users table
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users "
                            "(user_id TEXT UNIQUE PRIMARY KEY)")
        # create video table
        self.cursor.execute("CREATE TABLE IF NOT EXISTS videos "
                            "(video_id TEXT UNIQUE PRIMARY KEY, "
                            "path TEXT)")
        # create user_bookmarks table
        self.cursor.execute("CREATE TABLE IF NOT EXISTS user_bookmarks "
                            "(bookmark_id INTEGER, "
                            "user_id TEXT, "
                            "video_id TEXT)")

    def load_bookmarks_for_video(self, video_id: str) -> list(Bookmark):
        self.cursor.execute(f"SELECT * FROM bookmarks WHERE video_id = ?{video_id} AND user_id = {self.user}")
        bookmarks_data = self.cursor.fetchall()
        bookmarks = [Bookmark(id, user, video, time, title) for id, user, video, time, title in bookmarks_data]
        # convert to list of Bookmark() instances
        return sorted(bookmarks, key=lambda b: b.timestamp)

    def get_bookmark(self, bookmark_id) -> Bookmark:
        self.cursor.execute(f"SELECT * FROM bookmarks WHERE id = {bookmark_id}")
        id, user, video, time, title = self.cursor.fetchone()
        return Bookmark(id, user, video, time, title)

    def add_bookmark(self, bookmark: Bookmark) -> True | None:
        pass

    def delete_bookmark(self, bookmark: Bookmark) -> True | None:
        pass