import os

disk_space = ['100M', '200M', '500M', '2G']


# 标准化大小到字节；
def decode_batch_size(batch_str):
    if batch_str.endswith("K"):
        return int(batch_str[:-1])*1024

    if batch_str.endswith("M"):
        return int(batch_str[:-1])*1024*1024

    if batch_str.endswith("G"):
        return int(batch_str[:-1])*1024*1024*1024


# 获取文件夹下所有的文件列表；
def get_file_list(file_dir):
    file_list = []

    # 相比于listdir,利用walk可以遍历多级的子文件夹；
    for root, dirs, files in os.walk(file_dir):
        for name in files:
            file_list.append(os.path.join(root, name))

    file_list.sort()

    return file_list


