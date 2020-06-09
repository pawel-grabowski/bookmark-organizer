# Python 2.7 version: https://github.com/ProactiveNode/Bookmark-Organizer/blob/master/bookmarkOrganizer.py

#User inputs file name/path
#     filename = raw_input("Please enter the bookmark HTML filename: ")
filename = 'C:/Users/Paweł/Documents/Projekty/PyBookmarkOrganizer/input/bookmarks_31.05.2020.html'
#User inputs the websites that they want to have a bookmark folder with. It goes on until the user enters done.
keyword = []
while True:
    websiteName = input("Enter the website or type *done* to quit: ")
    if websiteName == "done":
        break
    keyword.append(websiteName)
    

#Reads the HTML file and puts all of the data into linesHTML
with open(filename,"r", encoding='utf-8') as file_read:
    linesHTML = file_read.readlines()


#Gets the length of the keyword list and goes through each element in the keyword list.
for g in range(len(keyword)):
    #Searches through linesHTML to find the website the user entered. If it has found it, then it gets put into 
    #the list_keyword list.
    list_keyword = []
    for i in range(len(linesHTML)):
        if keyword[g] in linesHTML[i].lower():
            list_keyword.append(linesHTML[i])

    #Removes the occurances of the website with linesHTML
    for p in range(len(list_keyword)):
        for z in range(len(linesHTML)):
            if list_keyword[p] in linesHTML[z]:
                linesHTML.remove(linesHTML[z])
                break

    startFolder = "<DL><p> \n <DT><H3> " + keyword[g] + "</H3> \n"
    endFolder = "</DL><p> \n"
    #Inserts the contents of list_keyword back into linesHTML so the folder for the bookmarks can be created.
    list_keyword.insert(0,startFolder)
    list_keyword.insert(len(list_keyword),endFolder)
    linesHTML[9:9] = list_keyword
    
#Creates a new HTML file that will include the folder of the bookmarks
newFilename = filename.replace(".html","_new.html")
with open(newFilename,"w", encoding='utf-8') as file_write:
    file_write.writelines(linesHTML)
