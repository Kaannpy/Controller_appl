import  random
import time
from os.path import split

class controller():
    def __init__(self,tv_status="Close",tv_volume=0,channel_list=["BBC,ATV"],channel="BBC",favorite_channel=[]):
        self.tv_status=tv_status
        self.tv_volume=tv_volume
        self.channel_list=channel_list
        self.channel=channel
        self.favorite_channel=favorite_channel

    def open_tv(self):
        if(self.tv_status=="Open"):
            print("Tv is already open...")
        else:
            print("Tv is being opening...")
            self.tv_status="Open"
    def close_tv(self):
        if(self.tv_status=="Close"):
            print("Tv is already close...")
        else:
            print("Tv is being closing...")
            self.tv_status="Close"
    def volume_settings(self):
        while True:
            volume=input("Volume up '+'\n and Volume down\n '-' Exit 'Exit' ")
            if(volume=="-"):
                if(self.tv_volume!=0):
                    self.tv_volume-=1
                    print("Volume:",self.tv_volume)

            elif(volume=="+"):
                if(self.tv_volume!=31):
                    self.tv_volume+=1
                    print("Volume:",self.tv_volume)

            else:
                print("Volume has been updated",self.tv_volume)
                break
    def add_channel(self,channel_name):
        if channel_name  not in  self.channel_list:
            print("Channel is being adding...")
            time.sleep(1)
            self.channel_list.append(channel_name)
            print("Channel has been added...")
        else:
            print("Channel is already has added...")

    def random_channel(self):
        random_number=random.randint(0,len(self.channel_list)-1)
        self.channel=self.channel_list[random_number]
        print("Current Channel:",self.channel)

    def __len__(self):
        return len(self.channel_list)

    def __str__(self):
        return "Tv status:{}\n Volume:{}\n Channel_List:{}\n,Current Channel:{}".format(self.tv_status,self.tv_volume,self.channel_list,self.channel)

    def delete_channel(self,channel_name):
        if(channel_name   in self.channel_list):

            print("Channel is being deleting...")
            time.sleep(1)
            self.channel_list.remove(channel_name)
            print("Channel has been deleted...")
        else:
            print("Channel has not been found...")
    def add_fav_channel(self,channel_name):
        if channel_name in self.channel_list  and channel_name not in self.favorite_channel:
            self.favorite_channel.append(channel_name)
            print("channel has been added to favorites...")
        else:
            print("it's already in favorites or does not exist...")

    def __str__(self):
        return "Favorite Channel list:{}".format(self.favorite_channel)

    def search_channel(self,search_term):
        found_channels=[channel for channel in self.channel_list if search_term.lower()in channel.lower()]

        if found_channels:
            for channel in found_channels:
             print("Channel has been found",self.channel_list)
        else:
            print("Channel has not been found or does not exist....")





controller1=controller()

print("""
   INFORMATION

   1.OPEN THE TV
   2.CLOSE THE TV
   3.VOLUME SETTINGS
   4.ADD CHANNEL
   5.LEARN CHANNEL COUNT
   6.PUT A RANDOM CHANNEL
   7.TV INFORMATION
   8.DELETE THE CHANNEL
   9.ADD TO FAVORITES
   10.SEE WHAT YOU HAVE IN FAVORİTES
   11.FIND A CHANNEL
   
   PRESS  "q" FOR  EXİT 


""")
while True:

    operation=input("select an operation :")
    if(operation=="q"):
        print("Terminating the program...")

    elif(operation=="1"):
        controller1.open_tv()
    elif(operation=="2"):
        controller1.close_tv()
    elif(operation=="3"):
        controller1.volume_settings()
    elif(operation=="4"):
        name_of_channels=input("Enter the channel names  separated by ','")
        channel_list=name_of_channels.split(",")
        for i in channel_list:
            controller1.add_channel(i)
    elif(operation=="5"):
        print("Channel count",len(controller1))
    elif(operation=="6"):
        controller1.random_channel()
    elif(operation=="7"):
        print(controller1)
    elif(operation=="8"):
        name_of_channel=input("Enter the channel name that you want to delete:")
        if(name_of_channel=="Exit"):
            continue
        controller1.delete_channel(name_of_channel)
    elif(operation=="9"):
        name_of_channel=input("Enter the channel name that you want to add in favorites:")
        if(name_of_channel=="Exit"):
            continue
        controller1.add_fav_channel(name_of_channel)
    elif(operation=="10"):
        print(controller1)
    elif(operation=="11"):
        found_channel=input("Enter the channel name that you want to find ")
        if (found_channel == "Exit"):
            continue
        controller1.search_channel(found_channel)

    else:
        print("unvalid operation...")







