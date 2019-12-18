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
        if s.isdigit():
            return int(s)
        elif ',' not in s and ('0x' in s or '0X' in s):
            return int(s, 16)
        elif s.count('.') == 1 and ',' not in s and '"' not in s and "'" not in s:
            return float(s.split('f')[0])
        elif ',' not in s and ('L"' in s or "L'" in s):
            str1 = s[2:len(s) - 1]
            return unicode(str1)
        elif len(s) == 3 and s[1].isalpha() and ('"' in s or "'" in s):
            return ord(s[1])
        elif ',' not in s and ('"' in s or "'" in s):
            return str(s[1:len(s) - 1])
        elif '{' and '}' in s:
            list1 = []
            str1 = s[1:len(s) - 1]
            index = str1.find('},')
            if index != -1:
                str1 = str1.replace('},', '}\t').split('\t')
                for i in str1:
                    list1.append(self.trans(i.strip()))
            else:
                str1 = str1.split(',')
                for i in str1:
                    list1.append(self.trans(i.strip()))
            return tuple(list1)
        else:
            raise TypeError

a = PyMacroParser()
print a.trans("{a}")

