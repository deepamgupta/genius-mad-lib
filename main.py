from Stories import Story

storiesTitle = Story.storiesTitle

if __name__=="__main__":
    print("Hey! This is Genius, welcome to my MadLibs Game. Have Fun!!")

    while True:
        print("\nEnter the code of the Story you like ;)")
        for story in storiesTitle:
            print(story + " : " + storiesTitle[story])
        print(">>>")

        code = input()

        if code not in storiesTitle:
            print("\nWrong Code! Please Try Again...")
            continue

        elif code == "0":
            break

        else:
            madLib = Story(code)

    print("\nHave a nice Day :)")