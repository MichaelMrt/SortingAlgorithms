class Bubblesort:

    def sort(self,list):
       swap_in_bubblephase = True
       for phases in range(0,len(list)):        
        if swap_in_bubblephase == False:
           break
        else:
           swap_in_bubblephase = False

        for i in range(0,len(list)-1):
            if(list[i]>list[i+1]):
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
                swap_in_bubblephase = True
        if swap_in_bubblephase == True:
            print(list)

            

