class FileHandler:
    def write_to_file(self, filename, content):
        try:
            with open(filename, 'w') as file:
                file.write(content)
            print(f"Content written to {filename}")
        except Exception as e:
            print("Something went wrong:", e)
        finally:
            print("Write operation complete.\n")

    def append_to_file(self,filename,content):
        try:
            with open(filename,"a") as file:
                file.write(content+ "+\n")
            print(f"this is the new content")
        except Exception as e:
            print("Something went wrong",e)
        finally:
            print("Append operation complete.\n")

    def read_file(self, filename):
        try:
            with open(filename, 'r') as file:
                content = file.read()
                print("File Content:\n" + content)
        except FileNotFoundError:
            print(f"File '{filename}' not found!")
        finally:
            print("Read operation complete.\n")

    def write_data(self,filename,content):
        try:
            with open(filename,"w") as file:
                file.write(content)
            print(f"Content written to {filename}")
        except Exception as e:
            print("Something went wrong",e)
        finally:
            print("Great! The text has been written")



    def append_data(self,filename, content):
        try:
            with open(filename,"a") as file:
                file.write(content+"\n")
            print(f"Content append to {filename}")
        except Exception as e:
            print("Something went wrong",e)
        finally:
            print("Hoola! ,The text has been appended")

    def append_practice(self,filename,content):
        try:
            with open (filename,"a") as file:
                file.write(content + "\n")
            print(f"The new added to file name {filename}")
        except Exception as e:
            print(f"Something went wrong",e)
        finally:
            print("The code has been successfully run")

    def read_file(self,filename):
        try:
            with open (filename,"r") as file:
                content=file.read()
                print(f"Content of is :-" + content)
        except FileNotFoundError:
            print(f"File {filename} not found")
        finally:
            print(f"Read operation complete.\n")








obj=FileHandler()
# obj.write_to_file("filehandlig.txt","Hello this is fist content for this file")
# obj.write_to_file("filehandling.txt","Hello everyone")
# obj.append_to_file("filehandlig.txt","My name is Amit Mohan Sharma and i am from agra")
# obj.append_to_file("filehandlig.txt","Hello World,Hello everyone")
# obj.read_file("filehandlig.txt")
# obj.write_data("demo.txt","Bhaiya ,all is well")
# obj.append_data("demo.txt","Tere naam ,humne kiya hai")
# obj.append_practice("demo.txt","Jai Jawan Jai Kishan")
obj.read_file("demo.txt",)