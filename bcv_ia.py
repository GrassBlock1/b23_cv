"""
    b23_cv - simple bilibili column downloader
    Copyright (C) 2024  Grassblock

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.


"""

from b23_cv import get_single, get_batch

print("Bilibili Columns downloader")

print(
    "This script is used to download articles from Bilibili and has batch/single modes. Refer to the README for "
    "more information.")

url = str(input("Please input a url:"))
output_folder = str(
    input(
        "Please input a path to save passages (relative to this python script), default is 'output':")) or "output"

if url.__contains__('read/cv'):
    get_single.__main__(stdin_url=url, stdin_folder=output_folder)
else:
    get_batch.__main__(stdin_url=url, stdin_folder=output_folder)
