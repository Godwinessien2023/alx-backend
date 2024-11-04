#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header row

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            # Index the first 1000 items in the dataset
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: truncated_dataset[i] for i in range(len(truncated_dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Returns a dictionary with pagination information."""
        # Assert that the index is within a valid range
        assert isinstance(index, int) and 0 <= index < len
        (self.indexed_dataset())

        data = self.indexed_dataset()
        data_keys = sorted(data.keys())  # Get the sorted list of indices
        current_index = index
        page_data = []

        # Collect the data for the current page
        while len(page_data) < page_size and current_index < len(data_keys):
            if current_index in data:
                page_data.append(data[current_index])
            current_index += 1

        # Calculate the next index
        next_index = current_index if current_index < len(data_keys) else None

        # Return the pagination information
        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(page_data),
            "data": page_data,
        }
