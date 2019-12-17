class PyMacroParser:
    def __init__(self):
        self.data = []
        self.macro = ['#ifdef', '#ifndef', '#else', '#endif', '#define', '#undef']

    def load(self, f):
        try:
            source = open(f, 'r')
            my_stack = []

            # delete comment
            for line in source.readlines():
                str1 = ''
                index = line.find('/*')
                index1 = line.find('*/')
                if index == -1 and index1 == -1:
                    if len(my_stack) == 0:
                        if '//' in line:
                            str1 = line.split('//')[0]
                            self.data.append(str1)
                        else:
                            str1 = line.replace('\n', '')+' '
                            if str1 != ' ':
                                self.data.append(str1)
                    else:
                        continue
                elif index != -1 and index1 != -1:
                    while index != -1 and index1 != -1:
                        if line[index1 + 2] == ' ':
                            line = line.replace(line[index:index1 + 3], '')
                        else:
                            line = line.replace(line[index:index1 + 2], '')
                        index = line.find('/*')
                        index1 = line.find('*/')
                    self.data.append(line.replace('\n', ''))
                elif index == -1 or index1 == -1:
                    if index != -1:
                        str1 = line.split('/*')[0]
                        self.data.append(str1)
                        my_stack.append('/*')
                    elif index1 != -1:
                        my_stack.pop()

                # analyse data
                for line in self.data:
                    s = line.split(' ')[0]
                    if s not in self.macro:
                        raise SyntaxError
        except Exception:
            print 'FileError'
        finally:
            source.close()

    def preDefine(self, s):
        pass

    def dumpDict(self):
        pass

    def dump(self, f):
        pass

    def trans(self, s):
        pass

a = PyMacroParser()
a.load('a.cpp')
print a.data
