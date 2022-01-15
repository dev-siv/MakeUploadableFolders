import os
import shutil

class MakeZip:
    def __init__(self, path, base_location) -> None:
        self.path = path
        self.base_location = base_location
    
    def get_file_path(self):
        if os.path.exists(self.path):
            full_paths = [os.path.join(self.path, f) for f in os.listdir(self.path)]
            print(f"There are {len(full_paths)} files present at path '{self.path}'")
            return full_paths

    def divide_into_100s(self):
        files_list = self.get_file_path()
        result = []
        if type(files_list) == list:
            number_folders = len(files_list) // 100 + 1
            start = 0
            end = 100
            while len(result) != number_folders:
                result.append(files_list[start:end])
                start = end
                end = end + 100
            print(f"Files are subdivided into {number_folders} folders")
            return result

    def make_folder_and_copy_files(self):
        sub_folders = self.divide_into_100s()
        try:
            main_pics = os.path.join(self.base_location, "Pics")
            os.mkdir(main_pics)
        except:
            pass
        for folder in sub_folders:
            folder_name = sub_folders.index(folder)
            try:
                folder_name = os.path.join(main_pics, str(folder_name))
                os.mkdir(os.path.join(main_pics, str(folder_name)))
            except FileExistsError:
                pass

            for files in folder:
                print(f"To copy from '{files}' to '{folder_name}'")
                shutil.copy(files, folder_name)

        print("Successfully copied!")
                


if __name__ == '__main__':
    path1 = r"" #enter main path
    folder_location = r""
    mz = MakeZip(path1, folder_location)
    # mz.get_file_path()
    # mz.divide_into_100s()
    mz.make_folder_and_copy_files()
