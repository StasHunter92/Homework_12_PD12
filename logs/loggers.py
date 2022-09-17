import logging

# logging config for search
logger_search = logging.getLogger("search_posts")
logger_search.setLevel(logging.INFO)
file_handler_search = logging.FileHandler("logs/search.log", encoding="utf-8")
file_handler_search.setLevel(logging.INFO)
logger_search.addHandler(file_handler_search)

# logging config for extension_error
logger_extensions = logging.getLogger("extension_error")
logger_extensions.setLevel(logging.INFO)
file_handler_extensions = logging.FileHandler("logs/extensions_error.log",
                                              encoding="utf-8")
file_handler_extensions.setLevel(logging.INFO)
logger_extensions.addHandler(file_handler_extensions)

# logging config for json_error
logger_json = logging.getLogger("json_error")
logger_json.setLevel(logging.ERROR)
file_handler_json = logging.FileHandler("logs/json_error.log", encoding="utf-8")
file_handler_json.setLevel(logging.ERROR)
logger_json.addHandler(file_handler_json)