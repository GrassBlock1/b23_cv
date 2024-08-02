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

import argparse

from b23_cv import get_single, get_batch

parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description="""
    Download articles from Bilibili, refer to the README for more information.\n\n
        b23_cv  Copyright (C) 2024  GrassBlock 
    This program comes with ABSOLUTELY NO WARRANTY; 
    This is free software, and you are welcome to redistribute it 
    under certain conditions; 
    refer to the LICENSE file for more information.
    """)
parser.add_argument('URL', metavar='URL', nargs=1, help='the URL of the '
                                                        'article/readlist or '
                                                        'the column')
parser.add_argument('--output', action='append_const',
                    const='folder', default="output",
                    help='the folder to be saved, default is "./output"')
args = parser.parse_args()

url = args.URL[0]
output_folder = args.output

if url.__contains__('read/cv'):
    get_single.__main__(stdin_url=url, stdin_folder=output_folder)
else:
    get_batch.__main__(stdin_url=url, stdin_folder=output_folder)
