
import imageio
def GenerateGIF(filenames,gifname):
    images=[]
    for filename in filenames:
        images.append(imageio.imread(filename))
    imageio.mimsave(gifname, images,duration=1)


def saveGif(nam,gifname):
    filename=['Images/start.jpg']
    nam=list(nam)
    for i in range(0,len(nam)):
        if nam[i]==" ":
            filename.append("Images/"+"space"+"_test.jpg")
            continue
        filename.append("Images/"+nam[i]+"_test.jpg")
    GenerateGIF(filename,gif)



nam=(input("Enter word for which you want to generate Gif : "))
nam=nam.upper()
gif=input("Enter gif filename with .gif extension : ")

saveGif(nam,gif)