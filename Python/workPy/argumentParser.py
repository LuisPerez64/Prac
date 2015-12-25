def main():
    FileList = list()
    CodeList = list()
    fileIn,codeIn = True, False
    
    while fileIn or codeIn:
        if fileIn:
            str='File'
        else:
            str='Code'
           
        print("Argument in %s. (Input '~' to terminate)" % str)            
        inp=input("Value: ")
        
        if inp == '~': #Either begin input of Code args, or quit
            if fileIn:
                fileIn = False
                codeIn = True
            else:
                break
            continue
            
        if fileIn:
            FileList.extend([inp])
        else:
            CodeList.extend([inp])

    compareArg(FileList, CodeList)

def compareArg(File, Code):
    for i in sorted(File):
        if i not in Code:
            print(i, ' in file not in code.')
    for i in sorted(Code):
        if i not in File:
            print(i, ' in code not in file.')

if __name__ == '__main__':
    main()
