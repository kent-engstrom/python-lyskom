# Locking version of shelve
# $Id: lockingshelve.py,v 1.2 1999/07/26 13:29:26 kent Exp $
# (C) 1999 Kent Engstr�m. Released under GPL.
# NOTE! Just enough for the needs of komimportmail. Use with caution.

import shelve
import lockfile

class LockingShelve:
    def __init__(self, shelf_name):
        self.__shelf_name = shelf_name
        self.__lock = lockfile.Lock(shelf_name + ".lock")

    # Internal operations
    def __open_read(self):
        self.__lock.shared_lock()
        self.__shelf = shelve.open(self.__shelf_name)

    def __open_write(self):
        self.__lock.exclusive_lock()
        self.__shelf = shelve.open(self.__shelf_name)

    def __close(self):
        self.__shelf.close()
        self.__shelf = None
        self.__lock.unlock()

    # Locking interface for normal use
    def keys(self):
        self.__open_read()
        try:
            return self.__shelf.keys()
        finally:
            self.__close()
            
    def __getitem__(self, index):
        self.__open_read()
        try:
            return self.__shelf[index]
        finally:
            self.__close()
            
    def __setitem__(self, index, data):
        self.__open_write()
        try:
            self.__shelf[index] = data
            import time
        finally:
            self.__close()

    # Use these when you want to use the shelf object directly
    def exclusive_open(self):
        self.__open_write()
        return self.__shelf

    def exclusive_close(self):
        self.__close()
