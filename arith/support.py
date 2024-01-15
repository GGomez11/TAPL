class FileInfo:
    def __repr__(self):
        return '<Uknown file and line>:'

class Info(FileInfo):
    def __init__(self, file_name, line_num, char_pos):
        self._file_name = file_name
        self._line_num = line_num
        self._char_pos = char_pos

    def __repr__(self):
        return f'{self._file_name}: {self._line_num}.{self._char_pos}:'