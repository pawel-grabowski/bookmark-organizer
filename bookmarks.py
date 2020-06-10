# Python 2.7 version: https://github.com/ProactiveNode/Bookmark-Organizer/blob/master/bookmarkOrganizer.py

def read_mapping():
    
    mapping = {}
    with open("./input/mapping.txt","r", encoding='utf-8') as f:
        lines = f.readlines()
        
    for line in lines:
        line = line.strip('\n')
        line_splitted = line.split('|')
        print(line_splitted)
        key=line_splitted[0]

        if len(line_splitted)>1:
            folder=line_splitted[1]
        else: folder=key  
        
        mapping.update({key : folder})
        
    return mapping


#User inputs the websites that they want to have a bookmark folder with. It goes on until the user enters done.
def read_user_keywords():
    keywords = []
    
    while True:
        websiteName = input("Enter the website or type *done* to quit: ")
        if websiteName == "done":
            break
        keywords.append(websiteName)
        
    return keywords 

#%% MAIN CODE

#User inputs file name/path
filename = 'C:/Users/Paweł/Documents/Projekty/PyBookmarkOrganizer/input/bookmarks_10.06.2020.html'

mapping = read_mapping()
keywords = mapping.keys()

#Reads the HTML file and puts all of the data into linesHTML
with open(filename,"r", encoding='utf-8') as file_read:
    linesHTML = file_read.readlines()


#Gets the length of the keyword list and goes through each element in the keyword list.
for keyword in keywords:
    #Searches through linesHTML to find the website the user entered. If it has found it, then it gets put into 
    #the list_keyword list.
    keyword_lines = []
    for line in linesHTML:
        if keyword in line.lower():
            keyword_lines.append(line)

    #Removes the occurances of the website with linesHTML
    for keyword_line in keyword_lines:
        for line in linesHTML:
            if keyword_line in line:
                linesHTML.remove(line)
                break
        
        #Normalize indentation in output file
        keyword_line = keyword_line.strip()
        keyword_line = 8*" "+keyword_line      
    
    #Define HTML tags for folder structure
    startFolder = "<DL><p> \n    <DT><H3> " + keyword + "</H3> \n"
    endFolder = "</DL><p> \n"

    #Inserts the contents of list_keyword back into linesHTML so the folder for the bookmarks can be created.
    keyword_lines.insert(0,startFolder) # opening folder definition
    keyword_lines.insert(len(keyword_lines),endFolder) # ending folder definition
    linesHTML[9:9] = keyword_lines # first line after meta-data & opening actual  list, for folder definition

#Group for second level folders
groups=[]
placeholder_lines=[]
for keyword in keywords:
    if not mapping[keyword] in groups and mapping[keyword]!=keyword:
        groups.append(mapping[keyword])

# Add empty (temporary) folder for groups
for group in groups:
    startFolder = "<DL><p> \n    <DT><H3> " + group + "</H3> \n"
    endFolder = "</DL><p> \n"
    placeholder_lines.insert(len(placeholder_lines),startFolder) # opening folder definition
    placeholder_lines.insert(len(placeholder_lines),endFolder) # ending folder definition
    
linesHTML[9:9] = placeholder_lines # first line after meta-data & opening actual  list, for folder definition

#Creates a new HTML file that will include the folder of the bookmarks
newFilename = filename.replace(".html","_new.html")
with open(newFilename,"w", encoding='utf-8') as file_write:
    file_write.writelines(linesHTML)

