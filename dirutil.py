import os
import hashlib


def get_directory_count(top_dir):
    # top_dir = r'/Volumes/ftp/UtahSGID_Vector'
    dircount = 0
    for root, dirs, files in os.walk(top_dir, topdown=True):
        for name in dirs:
            dir_path = os.path.join(root, name)
            print dir_path
            dircount += 1
    print dircount


def get_file_count(top_dir, ext, size_limit=None):
    file_count = 0
    for root, dirs, files in os.walk(top_dir, topdown=True):
        for name in files:
            dir_path = os.path.join(root, name)
            if name.endswith(ext):
                if size_limit:
                    if os.path.getsize(dir_path) <= size_limit:
                        file_count += 1
                else:
                    file_count += 1

    print 'count: {}, type: {}, size <= {}'.format(file_count, ext, size_limit)


def hash_files(file_list):
    hex_digest = []
    for f in file_list:
            file_path = f
            local_file_hash = hashlib.md5(open(file_path, 'rb').read()).hexdigest()
            hex_digest.append(local_file_hash)

    for h in hex_digest:
        print h


if __name__ == '__main__':
    # top_dir = r'/Volumes/ftp/UtahSGID_Vector'
    # get_file_count(top_dir, '.zip')

    files = [r'/Volumes/C/GisWork/drive_sgid/test_outputs/Trails_gdb.zip',
             r'./test/Trails_gdb.zip']
    hash_files(files)
