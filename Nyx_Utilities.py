import glob
import os


class Nyx_File_Parse_Utils:

    @staticmethod
    def return_all_files_in_dir(filepath):
        try:
            for root, dirs, files in os.walk(filepath):
                file_name = []
                temp = []
                file_extension = []
                for file in files:
                    os.path.splitext(file)
                    if file not in file_name:
                        file_name.append(file)
                        if file not in temp:
                            temp.append(file[-4::1])
                            if file[-4::1] not in file_extension:
                                file_extension.append(file[-4::1])
                print("Error - found the following file extensions: \n" + str(file_extension))
                print("\n Error - found the following files: \n" + str(file_name))
        except Exception():
            raise Exception("The directory path is invalid!")

    @staticmethod
    def return_all_files_in_dir2(filepath):
        try:
            for root, dirs, files in os.walk(filepath):
                file_name = []
                temp = []
                file_extension = []
                root_list = []
                counter = 0
                i = 0
                for roots in dirs, root:
                    if roots not in root_list:
                        root_list.append(roots)
                        counter = i + 1
                        for file in files:
                            os.path.splitext(file)
                            if file not in file_name:  # add file to table file_name
                                file_name.append(file)
                                if file not in temp:  # temp = table
                                    filename, extension = os.path.splitext(file)
                                    if extension not in file_extension:  # add file_exc to table file_extension
                                        file_extension.append(extension)
                print("\nFound in dir number '" + str(counter) + "':\n" +
                      str(root_list[1]) +
                      "\nThe following files: \n" +
                      str(file_name) +
                      "\nAnd the following file extensions: \n" +
                      str(file_extension))
        except Exception():
            raise Exception("The directory path is invalid!")

    @staticmethod
    def check_if_path_exists(filepath):
        if not os.path.exists(filepath):
            raise Exception("Path doesn't exists!")
        else:
            return filepath

    @staticmethod
    def open_file(filepath):
        try:
            file = open(filepath, "r")  # get file object reference to the file
            file_data = file.read()  # read content of file to string
            return file_data
        except Exception():
            raise Exception("Failed to open file!")

    @staticmethod
    def find_word_in_txt(filepath, word):
        try:
            # count occurrences of single word and and lower+strip
            occurrences = filepath.strip().lower().count(word)
            print("Word count for " + "'" + str(word) + "'" + ": " + str(occurrences))
        except Exception():
            raise Exception("Word couldn't be found in file.")

    @staticmethod
    def find_word_list_in_txt(filepath, word_list):
        try:
            # count occurrences of every word in list and lower+strip
            for word in word_list:
                occurrences = filepath.strip().lower().count(word)
                print("Errors count for " + "'" + str(word) + "'" + ": " + str(occurrences))
        except Exception():
            raise Exception("Words couldn't be found in file.")

    @staticmethod
    def find_last_modified(filepath):
        try:
            # return path of matching pathname pattern
            list_of_files = glob.glob(filepath)  # * means all if need specific format then *.csv
            # find last modified
            latest_file = max(list_of_files, key=os.path.getctime)
            return latest_file
        except Exception():
            raise Exception("Could not find latest modified file.")

    @staticmethod
    def find_file_by_dir(filepath, filetype):
        try:
            for root, dirs, files in os.walk(filepath):  # walk through directory
                for file in files:
                    if file.endswith(filetype):
                        return os.path.join(root, file)  # return file and root
                        # print('File is in: ' + os.path.join(root)) #print only root
        except Exception():
            raise Exception("Could not find file by path.")


if __name__ == "__main__":
    # vars:
    error_list1 = ['errors', 'file', 'error', '']
    error1 = 'errors'
    filepath1 = r"C:\Users\shoog\Documents\Python work\Python work 12.8\Python\Browse txt\.pytest_cache"
    filename1 = "build_log_nrf52_ble_s112_10040_boot.txt"
    filetype1 = "*.txt"
    filepath2 = r"C:\Users\shoog\PycharmProjects\Jian\build_log_nrf52_ble_s112_10040_boot.txt"
    # functions:
    # filepath2 = Nyx_File_Parse_Utils.open_file(filepath2)
    # Nyx_File_Parse_Utils.find_word_in_txt(filepath2, error1)
    # Nyx_File_Parse_Utils.find_word_list_in_txt(filepath2, error_list1)
    Nyx_File_Parse_Utils.return_all_files_in_dir2(filepath1)
