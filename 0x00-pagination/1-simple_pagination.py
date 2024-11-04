#!/usr/bin/env python3
"""
a function named index_range that takes two integer arguments page
and page_size.  :returns a tuple of size two containing a start
index and an end index corresponding to the range of indexes
to return in a list for those particular pagination parameters.
"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """return a tuple of size two containing a start index and an end index"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """return a page of the dataset"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        # Get the dataset
        data = self.dataset()

        # Calculate the start and end indexes using index_range
        start_index, end_index = index_range(page, page_size)

        # Return the appropriate page of the dataset (i.e. the dataset
        # at the start_index and end_index)
        if start_index >= len(data):
            return []

        return data[start_index:end_index]
