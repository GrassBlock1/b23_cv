import argparse

from b23_cv import get_single, get_batch

parser = argparse.ArgumentParser(
    description='Download articles from Bilibili, refer to the README for more information.')
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
