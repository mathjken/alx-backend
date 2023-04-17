#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate for popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                rd = csv.reader(f)
                dataset = [rw for rw in rd]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Dataset indexed by sorting position, starting at 0
        """
        dataset = self.indexed_dataset()
        assert type(index) is int and index in range(len(dataset))
        rows_data = []
        first_pos = index
        next_pos = index + page_size
        while first_pos < next_pos:
            if first_pos in dataset.keys():
                rows_data.append(dataset[first_pos])
            else:
                next_pos += 1
            first_pos += 1
        return {
            "index": index,
            "data": rows_data,
            "page_size": len(rows_data),
            "next_index": next_pos
            }
