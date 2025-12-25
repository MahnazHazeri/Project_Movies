from enum import Enum


class MovieStatusType(str, Enum):
    WATCHED = "watched"
    WANT_TO_WATCH = "want_to_watch"
