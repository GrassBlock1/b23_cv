from b23_cv import get_single, get_batch

print("Bilibili Columns downloader")

print("This script is used to download articles from Bilibili and has batch/single modes. Refer to the README for "
      "more information.")


url = str(input("Please input a url:"))
output_folder = str(input("Please input a path to save passages (relative to this python script), default is 'output':")) or "output"

if url.__contains__('read/cv'):
    get_single.__main__(stdin_url=url, stdin_folder=output_folder)
else:
    get_batch.__main__(stdin_url=url, stdin_folder=output_folder)

