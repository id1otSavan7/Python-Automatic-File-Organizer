import os
import shutil

class file_organizer():
    def __init__(self, src):
        self.dir = os.path.expanduser("~") #Automatically sets directory to current user
        self.src = src 
        self.src_path = os.path.join(self.dir, self.src) #Combine them together to create a path

        #Create dictionary of possible extensions that exists in to your src.
        self.extensions = {
            #images
            ".jpg" : "Pictures",
            ".jpeg" : "Pictures",
            ".png" : "Pictures",
            ".bmp" : "Pictures",
            ".gif" : "Pictures",

            #audio
            ".mp3" : "Music",
            
            #video
            ".mp4" : "Videos",
            
            #documents
            ".pdf" : "Documents",
            ".docx" : "Documents",
            ".txt" : "Documents",
            ".pptx" : os.path.join("Documents", "Presentations"),
            ".xlsx" : os.path.join("Documents", "Spreadsheets"),

            #files
            ".exe" : os.path.join("Documents", "Installer"),
            ".msi" : os.path.join("Documents", "Installer"),
            ".zip" : os.path.join("Documents", "Compressed-Files"),
            ".7z" : os.path.join("Documents", "Compressed-Files"),
            ".rar" : os.path.join("Documents", "Compressed-Files"),
        }
    
    #Checks of corresponding directories from key values indicated in the dictionary exists...
    def process_file(self, filename):
        self.dir_name = self.extensions[self.file_ext] #Takes dict key value, then...
        self.dir_path = os.path.join(self.dir, self.dir_name) #Creates a path...
        os.makedirs(self.dir_path, exist_ok=True) #If dir does not exists create a new one, if it does...
        self.file_destination = os.path.join(self.dir_path, filename) #Create a target destination  
    
    #Moves file after being processed...
    def move_file(self, file):
        shutil.move(self.file_path, self.file_destination) #Uses shutil module to move file to target...
        print(f"System: Moved {file} to {self.dir_name} folder")
        
    #Function that does things...        
    def organize_files(self):
        for file in os.listdir(self.src_path): #Get files from src
            self.file_path = os.path.join(self.src_path, file) #Create a reference...
            if os.path.isfile(self.file_path): #Verify if it is a file
                self.file_ext = os.path.splitext(file)[1].lower() #Takes the extension string...
                if self.file_ext in self.extensions: #See if extension exists in the dictionary...
                    self.process_file(file) #Execute this...
                    self.move_file(file) #then this...
                else:
                    #If file has an unknown extension...
                    print(f"System: Skipped {file}. Unknown file extension.") 
            else:
                #if file was not a literal file (probably a folder or other things...).
                print(f"System: Skipped {file}. It is not a file.") 
    
    #Method to just run it all at once...
    def run(self):
        print("System: Organizing files...")
        self.organize_files()
        print("System: Files Organized successfully.")

#indicate your src...
source = "Downloads" #We can change this into input, to take user desired directory...
if __name__ == "__main__":
    app = file_organizer(source)
    try:
        app.run() #If there is no problem, then all is well...
    except:
        #Throws an exception if dir can't be found inside C:\Users\You\...
        print(f"System: The {source} folder can not be found at {app.dir}")
