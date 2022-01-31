import hashlib

class CHash:
    '''
    this class get two argument that first one is name 
    and second one is password's hash.
    this class hack User's password.
    be carefull ! :)
    '''


    def __init__(self,input_file_name,output_file_name):
        #set instance attribute
        self.input_file_name = input_file_name
        self.output_file_name = output_file_name

    def crack_sha256_4(self):

        for i in range(10000):
            text = str(i).zfill(4)
#             x=str(i).zfill(4)
            r_hash = hashlib.sha256(text.encode('utf-8')).hexdigest()

            if r_hash == str(self.output_file_name):
                print(f'Pass {self.input_file_name}: {str(i).zfill(4)}')


    def __str__(self):
        return f"this class hack password 1000 to 9999"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.input_file_name} , {self.output_file_name})"


if __name__ == '__main__':
    a = CHash("Amir",'6c6be40c2a563b401324a4e221da74080d0f4fd9425aaf18a771ede47c3109c0')
    a.crack_sha256_4()