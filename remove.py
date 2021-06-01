INPUT = ("nhoJ (Griffith) nodnoL saw (an) (American) ,tsilevon "
         ",tsilanruoj (and) laicos .tsivitca A reenoip (of) laicremmoc "
         "noitcif (and) naciremA ,senizagam (he) saw eno (of) (the) tsrif "
         "(American) srohtua (to) emoceb (an) lanoitanretni ytirbelec "
         "(and) nrae a egral enutrof (from) .gnitirw")

CORRECT_ANSWER = "John Griffith London was an American novelist, journalist, and social activist. A pioneer of " \
                 "commercial fiction and American magazines, he was one of the first American authors to become an " \
                 "international celebrity and earn a large fortune from writing."

def fix_text(mystr):
    mystr=mystr.split() 

    list=[]
    for r in mystr:
        if (r[0]+ r[-1])=="()":
            list.extend(r[1:-1])
        else:
            list.extend(r[::-1]) 
    mystr=" ".join(list)
    return mystr

if __name__ == "__main__":
    print("Correct!" if fix_text(INPUT) == CORRECT_ANSWER else "Sorry, it does not match with the correct answer.")